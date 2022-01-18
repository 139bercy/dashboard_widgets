<template>

  <div class="widget_container fr-grid-row" :class="(loading)?'loading':''" :data-display="display" :id="widgetId">
    <LeftCol v-bind="leftColProps" v-if="leftCol || leftCol === undefined"></LeftCol>
    <div class="r_col fr-col-12" :class="{'fr-col-lg-9': leftCol}">
      <div class="" :class="{'map fr-col-12': DOMTOMBottom, 'm-lg': leftCol, 'fr-grid-row': !DOMTOMBottom}">
        <div class="map_tooltip" v-if="tooltip.display" :style="{top:tooltip.top,left:tooltip.left}">
          <div class="tooltip_header">{{ convertDateToHuman(tooltip.date) }}</div>
          <div class="tooltip_body">
            <div class="tooltip_place">{{ tooltip.place }}</div>
            <div class="tooltip_value">{{ convertStringToLocaleNumber(tooltip.value) }} {{ units[0] }}</div>
          </div>
        </div>
        <div class="no_select" :class="{'france_container': DOMTOMBottom, 'fr-col-9' : !DOMTOMBottom}">
          <FranceByDepartments :onenter="displayTooltip" :onleave="hideTooltip" v-show="this.definedMinGeoLevel == 'departements'"></FranceByDepartments>
          <FranceByRegions :onenter="displayTooltip" :onleave="hideTooltip" v-show="this.definedMinGeoLevel == 'regions'"></FranceByRegions>
        </div>
        <div :class="{'fr-col-1' : !DOMTOMBottom}"></div>
        <div class="om_container no_select" :class="{'fr-grid-row': DOMTOMBottom, 'fr-col-2' : !DOMTOMBottom}">
          <div class="om fr-col-4 fr-col-sm">
            <span class="fr-text--xs fr-my-1w">Guadeloupe</span>
            <guadeloupe :onenter="displayTooltip" :onleave="hideTooltip"></guadeloupe>
          </div>
          <div class="om fr-col-4 fr-col-sm">
            <span class="fr-text--xs fr-my-1w">Martinique</span>
            <martinique :onenter="displayTooltip" :onleave="hideTooltip"></martinique>
          </div>
          <div class="om fr-col-4 fr-col-sm">
            <span class="fr-text--xs fr-my-1w">Guyane</span>
            <guyane :onenter="displayTooltip" :onleave="hideTooltip"></guyane>
          </div>
          <div class="om fr-col-4 fr-col-sm">
            <span class="fr-text--xs fr-my-1w">La Réunion</span>
            <reunion :onenter="displayTooltip" :onleave="hideTooltip"></reunion>
          </div>
          <div class="om fr-col-4 fr-col-sm">
            <span class="fr-text--xs fr-my-1w">Mayotte</span>
            <mayotte :onenter="displayTooltip" :onleave="hideTooltip"></mayotte>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import LeftCol from '@/components/LeftCol'
import maps from '@/components/maps'
import * as d3 from 'd3-scale'
import { isMobile } from 'mobile-device-detect'
import { mixin } from '@/utils.js'

export default {
  name: 'MapChart',
  mixins: [mixin],
  components: {
    LeftCol,
    ...maps
  },
  data () {
    return {
      indicateur_data: undefined,
      labels: [],
      dataset: [],
      widgetId: '',
      chartId: '',
      display: '',
      leftColProps: {
        localisation: '',
        currentValues: [],
        currentDate: '',
        names: [],
        evolcodes: [],
        evolvalues: [],
        min: 0,
        max: 0,
        isMap: true,
        date: ''
      },
      scaleMin: 0,
      scaleMax: 0,
      units: [],
      chart: undefined,
      loading: true,
      legendLeftMargin: 0,
      geoFallback: false,
      geoFallbackMsg: '',
      tooltip: {
        top: '0px',
        left: '0px',
        display: false,
        value: 0,
        date: '',
        place: ''
      }
    }
  },
  props: {
    indicateur: String,
    leftCol: {
      type: Boolean,
      default: true
    },
    DOMTOMBottom: {
      type: Boolean,
      default: true
    },
    minGeoLevel: String
  },
  computed: {
    selectedGeoLevel () {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode () {
      if (store.state.user.geoLevelOrder.indexOf(this.definedMinGeoLevel) > store.state.user.geoLevelOrder.indexOf(store.state.user.selectedGeoLevel)) {
        const departement = store.state.departements.find(function (departement) {
          if (self.selectedGeoLevel === "France") {
            return true
          } else if (self.selectedGeoLevel === "regions") {
            return store.state.user.selectedGeoCode === departement.region_value
          } else {
            return store.state.user.selectedGeoCode === departement.value
          }
        })
        if (this.selectedGeoLevel === "France") {
          return "France entière"
        } else if (this.selectedGeoLevel === "regions") {
          return departement.region_value
        }
        return departement.value
      }
      return store.state.user.selectedGeoCode
    },
    selectedGeoLabel () {
      if (store.state.user.geoLevelOrder.indexOf(this.definedMinGeoLevel) > store.state.user.geoLevelOrder.indexOf(store.state.user.selectedGeoLevel)) {
        const departement = store.state.departements.find(function (departement) {
          if (self.selectedGeoLevel === "France") {
            return true
          } else if (self.selectedGeoLevel === "regions") {
            return store.state.user.selectedGeoCode === departement.region_value
          } else {
            return store.state.user.selectedGeoCode === departement.value
          }
        })
        if (this.selectedGeoLevel === "France") {
          return "France entière"
        } else if (this.selectedGeoLevel === "regions") {
          const region = store.state.regions.find(function (region) {
            return region.value === departement.region_value
          })
          return region.label
        }
        return departement.label
      }
      return store.state.user.selectedGeoLabel
    },
    style () {
      return 'margin-left: ' + this.legendLeftMargin + 'px'
    },
    definedMinGeoLevel () {
      if (this.indicateur_data && this.indicateur_data[this.minGeoLevel]) {
        return this.minGeoLevel
      }
      return store.state.user.geoLevelOrder[store.state.user.geoLevelOrder.indexOf(this.minGeoLevel) + 1]
    }

  },
  methods: {
    async getData () {
      store.dispatch('getData', this.indicateur).then(data => {
        this.indicateur_data = data
        this.loading = false
        this.updateMap()
      })
    },
    updateData () {
      const self = this

      const selectedLevel = self.selectedGeoLevel
      const selectedCode = self.selectedGeoCode
      const geoObject = this.getGeoObject(selectedLevel, selectedCode)

      this.leftColProps.localisation = selectedLevel
      this.leftColProps.date = this.convertDateToHuman(geoObject.last_date)

      this.leftColProps.names.length = 0
      this.units.length = 0
      this.leftColProps.currentValues.length = 0
      this.leftColProps.evolcodes.length = 0
      this.leftColProps.evolvalues.length = 0

      this.leftColProps.names.push(this.indicateur_data.nom)
      this.units.push(this.indicateur_data.unite)
      this.leftColProps.currentValues.push(geoObject.last_value)
      this.leftColProps.currentDate = this.convertDateToHuman(geoObject.last_date)
      this.leftColProps.evolcodes.push(geoObject.evol_color)
      this.leftColProps.evolvalues.push(geoObject.evol_percentage)

      const values = []
      this.indicateur_data[this.definedMinGeoLevel].forEach(function (d) {
        values.push(parseInt(d.last_value))
      })

      this.scaleMin = Math.min.apply(null, values)
      this.scaleMax = Math.max.apply(null, values)

      this.leftColProps.min = this.scaleMin
      this.leftColProps.max = this.scaleMax

      const color = d3.scaleLinear().domain([this.scaleMin, this.scaleMax]).range(['#ffc700', '#715845'])
      const widget = document.getElementById(this.widgetId)
      const isRegion = self.definedMinGeoLevel === 'regions'
      const isRegionSelection = selectedLevel === 'regions'
      const isDepartment = self.definedMinGeoLevel === 'departements'
      const isDepartmentSelection = selectedLevel === 'departements'
      const locationSelector = isDepartment ? 'department': 'region'
      const data = isDepartment ? store.state.departements : store.state.regions

      data.forEach(function (location) {
        widget
          .querySelectorAll("[data-" + locationSelector + "='" + location.value + "']")
          .forEach(function(locationObject) {
            const value = self.indicateur_data[self.definedMinGeoLevel].find(function (v) {
              return v.code_level === location.value
            })

            if (selectedLevel === 'France' 
              || (isRegion && isRegionSelection && location.value === selectedCode)
              || (isDepartment && isDepartmentSelection && location.value === selectedCode)
              || (isDepartment && isRegionSelection && location.region_value === selectedCode)) {
              locationObject.setAttribute('fill', color(value.last_value))
            }
            else {
              locationObject.setAttribute('fill', 'rgba(247, 237, 211, 0.72)')
            }
          })
      })
    },

    getGeoObject (geolevel, geocode) {
      let geoObject
      if (geolevel === 'France') {
        geoObject = this.indicateur_data.france[0]
      } else {
        geoObject = this.indicateur_data[geolevel].find(obj => {
          return obj.code_level === geocode
        })
      }
      return geoObject
    },

    updateMap () {
      this.updateData()
    },

    displayTooltip (e) {
      if (isMobile) return

      const level = this.definedMinGeoLevel

      const locationId = level == 'departements'
        ? e.target.dataset.department
        : e.target.dataset.region

      const location = store.state[level].find(obj => {
        return obj.value == locationId
      })
      const locationData = this.indicateur_data[level].find(obj => {
        return obj.code_level === location.value
      })

      this.tooltip.value = locationData.last_value
      this.tooltip.date = locationData.last_date
      this.tooltip.place = location.label
      this.tooltip.top = (e.target.getBoundingClientRect().top - 75) + 'px'
      this.tooltip.left = (e.target.getBoundingClientRect().left + 15) + 'px'
      this.tooltip.display = true
    },

    hideTooltip () {
      if (isMobile) return
      this.tooltip.display = false
    }
  },

  watch: {
    selectedGeoCode: function () {
      this.updateData()
    },
    selectedGeoLevel: function () {
      this.updateData()
    }
  },

  created () {
    this.chartId = 'myChart' + Math.floor(Math.random() * (1000))
    this.widgetId = 'widget' + Math.floor(Math.random() * (1000))
    this.getData()
  }
}

</script>

<style scoped lang="scss">

.no_select {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

.widget_container {
  .m-lg {
    margin-left: 0;
    margin-top: 1.5rem;
  }

  .map {
    display: flex;
    flex-direction: column;
    align-items: center;

    .france_container {
      height: 100%;

      svg {
        height: 100%;
        width: 100%;

        g {
          cursor: pointer;
        }
      }
    }

    .om_container {
      width: 100%;

      .om {
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #616161;

        span {
          display: block;
          white-space: nowrap;
        }

        g {
          cursor: pointer;
        }
      }
    }
  }

  .map_tooltip {
    width: 165px;
    height: auto;
    background-color: white;
    position: fixed;
    z-index: 999;
    border-radius: 4px;
    box-shadow: 0 8px 16px 0 rgba(22, 22, 22, 0.12), 0 8px 16px -16px rgba(22, 22, 22, 0.32);
    text-align: left;
    pointer-events: none;
    font-size: 0.75rem;

    .tooltip_header {
      width: 100%;
      height: 30px;
      background-color: #f6f6f6;
      color: #6b6b6b;
      padding-left: 5px;
      padding-top: 3px;
    }

    .tooltip_body {
      padding-left: 5px;
      padding-bottom: 5px;
      line-height: 1.67;

      .tooltip_place {
        color: #242424;
      }

      .tooltip_value {
        color: #242424;
        font-weight: bold;
      }
    }
  }

  @media (min-width: 62em) {
    .m-lg {
      margin-left: 3rem;
      margin-top: 0
    }
    .map {
      height: 100%;
      max-height: 100%;
    }
  }
  @media (max-width: 62em) {
    .chart .flex {
      margin-left: 0 !important
    }
    .map {
      width: 100%;
    }
  }

  .r_col {
    align-self: stretch;

    .flex {
      display: flex;
      align-items: center;
    }
  }

}

</style>
