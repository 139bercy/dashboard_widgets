<template>
  <div class="chart-map-panel" :class="{'panel-full-page-lg': $screen.breakpoint === 'lg', 'only-one-element' : onlyOneElement}">
    <div v-if="indicateur_data && !loading" class="fr-grid-row">
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColProps" :logo="logo" :alt-logo="altLogo"
                v-if="$screen.breakpoint === 'lg' && this.indicateur_data && this.indicateur_data.departements"></left-col>
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeChart"
                v-if="$screen.breakpoint === 'lg' && this.indicateur_data && !this.indicateur_data.departements"></left-col>
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeChart"
                v-if="$screen.breakpoint !== 'lg'"></left-col>
      <div class="line-map-container fr-col-12 fr-col-lg-9" v-if="onglet.indicateurs.length > 0">
        <LineChart
            class="chart-container"
            :line-chart-configuration="lineChartConfiguration"
            :indicateur="indicateurCode1"
            :left-col="false"
            v-if="indicateur_data && !indicateur_data2 && onglet.Graph">
        </LineChart>
        <MultiLineChart
            class="chart-container"
            :line-chart-configuration="lineChartConfiguration"
            :indicateur1="indicateurCode1"
            :indicateur2="indicateurCode2"
            :left-col="false"
            v-if="indicateur_data2 && onglet.Graph">
        </MultiLineChart>
        <BarChart
            class="chart-container"
            :bar-chart-configuration="barChartConfiguration"
            :indicateur="indicateurCode1"
            :left-col="false"
            v-if="indicateur_data && !indicateur_data2 && onglet.Bar">
        </BarChart>
        <MultiBarChart
            class="chart-container"
            :bar-chart-configuration="barChartConfiguration"
            :indicateur1="indicateurCode1"
            :indicateur2="indicateurCode2"
            :left-col="false"
            v-if="indicateur_data2 && onglet.Bar">
        </MultiBarChart>
        <MapChart
            class="map-container fr-col-12"
            :indicateur="indicateurCode1"
            :left-col="false"
            :DOMTOMBottom="true"
            :min-geo-level="onglet.MinGeoLevel"
            v-if="onglet.Carte && indicateur_data && this.indicateur_data[onglet.MinGeoLevel]">
        </MapChart>
      </div>
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeMap"
                v-if="$screen.breakpoint !== 'lg' && this.indicateur_data && this.indicateur_data.departements && onglet.Carte"></left-col>
    </div>
    <div v-else-if="loading">
      Récupération des données en cours
    </div>
    <div v-else>
      Impossible de récupérer les données
    </div>
  </div>
</template>

<script>

import store from '@/store'
import LineChart from './LineChart.vue'
import MultiLineChart from './MultiLineChart.vue'
import BarChart from './BarChart.vue'
import MultiBarChart from './MultiBarChart.vue'
import MapChart from './MapChart.vue'
import { mixin } from '@/utils.js'
import LeftCol from './LeftCol'

export default {
  name: 'ChartMapPanel',

  mixins: [mixin],
  components: {
    LeftCol,
    LineChart,
    BarChart,
    MultiLineChart,
    MultiBarChart,
    MapChart
  },
  props: {
    index: String,
    Titre_panneau: String,
    Lien_page_mesure: String,
    onglet: Object,
    logo: String,
    altLogo: String,
    lineChartConfiguration: Object,
    barChartConfiguration: Object
  },
  data() {
    return {
      loading: true,
      indicateur_data: undefined,
      indicateur_data2: undefined,
      dataset: [],
      dataset2: [],
      leftColProps: {
        min: 0,
        max: 0,
        date: null,
        localisation: null,
        currentValues: [],
        currentDate: null,
        names: null,
        evolcodes: null,
        evolvalues: null,
        isMap: false,
        isBox: false,
        units: [],
        unitsEvol: []
      },
    }
  },
  computed: {
    selectedGeoLevel () {
      if (store.state.user.geoLevelOrder.indexOf(this.definedMinGeoLevel) > store.state.user.geoLevelOrder.indexOf(store.state.user.selectedGeoLevel)) {
        return this.definedMinGeoLevel
      }
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
    definedMinGeoLevel () {
      if (this.indicateur_data && this.indicateur_data[this.onglet.MinGeoLevel]) {
        return this.onglet.MinGeoLevel
      }
      return store.state.user.geoLevelOrder[store.state.user.geoLevelOrder.indexOf(this.onglet.MinGeoLevel) + 1]
    },
    indicateurCode1() {
      return this.onglet.indicateurs[0].Code_indicateur
    },
    indicateurCode2() {
      return this.onglet.indicateurs[1].Code_indicateur
    },
    indicateurName1() {
      return this.onglet.indicateurs[0].Titre_indicateur
    },
    indicateurName2() {
      return this.onglet.indicateurs[1].Titre_indicateur
    },
    leftColPropsNotLargeChart() {
      return {
        date: this.leftColProps.date,
        localisation: this.leftColProps.localisation,
        currentValues: this.leftColProps.currentValues,
        currentDate: this.leftColProps.currentDate,
        names: this.leftColProps.names,
        evolcodes: this.leftColProps.evolcodes,
        evolvalues: this.leftColProps.evolvalues,
        units: this.leftColProps.units,
        unitsEvol: this.leftColProps.unitsEvol,
        logo: this.logo,
        altLogo: this.altLogo,
        isBox: this.leftColProps.isBox
      }
    },
    leftColPropsNotLargeMap() {
      return {
        min: this.leftColProps.min,
        max: this.leftColProps.max,
        isMap: true,
        isBox: false,
        logo: this.logo,
        altLogo: this.altLogo
      }
    },
    onlyOneElement() {
      return this.onglet.Carte && !this.onglet.Graph && !this.onglet.Bar
      || !this.onglet.Carte && this.onglet.Graph && !this.onglet.Bar
      || !this.onglet.Carte && !this.onglet.Graph && this.onglet.Bar
    }
  },
  methods: {
    async getData() {
      this.loading = true
      const promise1 = store.dispatch('getData', this.indicateurCode1).then(data => {
        this.indicateur_data = data
      })

      let promise2;
      if (this.onglet.indicateurs.length === 2) {
        promise2 = store.dispatch('getData', this.indicateurCode2).then(data => {
          this.indicateur_data2 = data
        })
      } else {
        promise2 = Promise.resolve();
      }

      Promise.all([promise1, promise2]).then(_ => {
        this.updateData()
        this.loading = false
      }).catch(_ => {
        this.loading = false
      })
    },
    updateData() {
      if (this.indicateur_data === null) {
        return;
      }
      this.updateDataForLegend()
      if (this.indicateur_data.departements !== null) {
        this.updateDataForLegendMap();
      }
    },
    updateDataForLegend() {
      const self = this
      if (this.indicateur_data === null) {
        return;
      }
      let oldLocalisation = this.leftColProps.localisation
      this.leftColProps.localisation = this.selectedGeoLabel

      this.leftColProps.isBox = this.onglet.Box

      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      let geoObject
      let geoObject2

      if (geolevel === 'France' || !this.indicateur_data[geolevel]) {
        geoObject = this.indicateur_data.france[0]
        if (this.indicateur_data2) {
          geoObject2 = this.indicateur_data2.france[0]
        }
        this.leftColProps.localisation = oldLocalisation ?? this.leftColProps.localisation
      } else {
        geoObject = this.indicateur_data[geolevel].find(obj => {
          return obj.code_level === geocode
        })
        if (this.indicateur_data2) {
          geoObject2 = this.indicateur_data2[geolevel].find(obj => {
            return obj.code_level === geocode
          })
        }
      }

      this.leftColProps.date = this.convertDateToHuman(geoObject.last_date)

      this.leftColProps.names = []
      this.leftColProps.units = []
      this.leftColProps.currentValues = []
      this.leftColProps.evolcodes = []
      this.leftColProps.evolvalues = []
      this.leftColProps.unitsEvol = []

      this.leftColProps.names.push(this.indicateurName1)
      this.leftColProps.units.push(this.onglet.indicateurs[0]["Unité_GP"])
      this.leftColProps.unitsEvol.push(this.onglet.indicateurs[0]["Unité_Evol"])
      this.leftColProps.currentValues.push(geoObject.last_value)
      if (this.indicateur_data2) {
        this.leftColProps.names.push(this.indicateurName2)
        this.leftColProps.units.push(this.onglet.indicateurs[1]["Unité_GP"])
        this.leftColProps.unitsEvol.push(this.onglet.indicateurs[1]["Unité_Evol"])
        this.leftColProps.currentValues.push(geoObject2.last_value)
      }
      this.leftColProps.currentDate = this.convertDateToHuman(geoObject.last_date)
      this.leftColProps.evolcodes.push(geoObject.evol_color)
      this.leftColProps.evolvalues.push(geoObject.evol_percentage)
      if (geoObject2) {
        this.leftColProps.evolcodes.push(geoObject2.evol_color)
        this.leftColProps.evolvalues.push(geoObject2.evol_percentage)
      }

      this.labels = []
      this.dataset = []
      this.dataset2 = []

      geoObject.values.forEach(function (d) {
        self.labels.push(self.convertDateToHuman(d.date))
        self.dataset.push((d.value))

        if (geoObject2) {
          const correspondingValue = geoObject2.values.find(obj => {
            return obj.date === d.date
          })
          if (correspondingValue) {
            self.dataset2.push(correspondingValue.value)
          }
        }
      })
    },
    updateDataForLegendMap() {
      if (this.indicateur_data === null || this.indicateur_data.departements === null) {
        return;
      }

      // Gestion de la légende de la map
      const values = []
      this.indicateur_data.departements.forEach(function (d) {
        if (d !== null && d.last_value !== null) {
          values.push(parseInt(d.last_value))
        }
      })

      this.leftColProps.min = Math.min.apply(null, values)
      this.leftColProps.max = Math.max.apply(null, values)
      this.leftColProps.isMap = this.onglet.Carte
    }
  },
  created() {
    this.getData()
  },
  watch: {
    selectedGeoCode: function () {
      this.updateData()
    },
    selectedGeoLevel: function () {
      this.updateData()
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.chart-map-panel {
  .map-legend {
    height: 100%;
    overflow: auto;
  }
  &.panel-full-page-lg {
    height: 100%;
    max-height: 100%;
    .line-map-container {
      height: 100%;
      max-height: 100%;
    }
    > div {
      height: 100%;
      max-height: 100%;
    }
    .chart-container {
      > div {
        height: 100%;
        max-height: 100%;
        > .chart {
          max-height: 100%;
          height: 100%;
          canvas {
            height: 100%;
            max-height: 100%;
          }
        }
      }
    }
    &.only-one-element {
      height: 100%;
      max-height: 100%;
      .chart-container {
        height: 100%;
        max-height: 100%;
      }
    }
    &:not(.only-one-element) {
      .chart-container {
        height: 30%;
        max-height: 30%;
      }
      .map-container {
        height: 70%;
        max-height: 70%;
        > div {
          height: 100%;
          max-height: 100%;
          > div {
            height: 100%;
            max-height: 100%;
            > .france_container {
              height: 70%;
              max-height: 70%;
              .svg {
                max-height: 70%;
                margin-left: 0;
                margin-right: 0;
              }
            }
          }
          .om_container {
            svg {
              max-height: 35%;
            }
          }
        }
      }
    }
  }
}
</style>
