<template>
  <div class="line-map-panel" :class="{'panel-full-page-lg': $screen.breakpoint === 'lg'}">
    <div v-if="indicateur_data && !loading" class="fr-grid-row">
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColProps"
                v-if="$screen.breakpoint === 'lg'"></left-col>
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeChart"
                v-if="$screen.breakpoint !== 'lg'"></left-col>
      <div class="container fr-col-12 fr-col-lg-9" v-if="onglet.indicateurs.length > 0 && onglet.Graph">
        <line-chart
            class="chart-container"
            interpolation="monotone"
            :indicateur="indicateurName1"
            :top-col="false"
            :left-col="false"
            v-if="indicateur_data && !indicateur_data2">
        </line-chart>
        <multi-line-chart
            class="chart-container"
            interpolation="monotone"
            :indicateur1="indicateurName1"
            :indicateur2="indicateurName2"
            :top-col="false"
            :left-col="false"
            v-if="indicateur_data2">
        </multi-line-chart>
        <map-chart
            class="map-container fr-col-12"
            :indicateur="indicateurName1"
            :top-col="false"
            :left-col="false"
            :bottom-col="false"
            :DOMTOMBottom="true"
            v-if="onglet.Carte && indicateur_data">
        </map-chart>
      </div>
      <left-col class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeMap"
                v-if="$screen.breakpoint !== 'lg'"></left-col>
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
import MapChart from './MapChart.vue'
import { mixin } from '@/utils.js'
import LeftCol from './LeftCol'

export default {
  name: 'LineMapPanel',

  mixins: [mixin],
  components: {
    // LineCol,
    LeftCol,
    LineChart,
    MultiLineChart,
    MapChart
  },
  props: {
    index: String,
    Nom_mesure_GP: String,
    Lien_page_mesure: String,
    onglet: Object
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
        isMap: true,
        date: null,
        localisation: null,
        currentValues: [],
        currentDate: null,
        names: null,
        evolcodes: null,
        evolvalues: null
      },
    }
  },
  computed: {
    selectedGeoLevel() {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode() {
      return store.state.user.selectedGeoCode
    },
    selectedGeoLabel() {
      return store.state.user.selectedGeoLabel
    },
    indicateurName1() {
      return this.onglet.indicateurs[0].Nom_indicateur_propilot
    },
    indicateurName2() {
      return this.onglet.indicateurs[1].Nom_indicateur_propilot
    },
    leftColPropsNotLargeChart() {
      return {
        date: this.leftColProps.date,
        localisation: this.leftColProps.localisation,
        currentValues: this.leftColProps.currentValues,
        currentDate: this.leftColProps.currentDate,
        names: this.leftColProps.names,
        evolcodes: this.leftColProps.evolcodes,
        evolvalues: this.leftColProps.evolvalues
      }
    },
    leftColPropsNotLargeMap() {
      return {
        min: this.leftColProps.min,
        max: this.leftColProps.max,
        isMap: true
      }
    }
  },
  methods: {
    async getData() {
      this.loading = true
      const promise1 = store.dispatch('getData', this.indicateurName1).then(data => {
        this.indicateur_data = data
      })

      let promise2;
      if (this.onglet.indicateurs.length === 2) {
        promise2 = store.dispatch('getData', this.indicateurName2).then(data => {
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

      this.leftColProps.localisation = this.selectedGeoLabel

      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      let geoObject
      let geoObject2

      if (geolevel === 'France') {
        geoObject = this.indicateur_data.france[0]
        if (this.indicateur_data2) {
          geoObject2 = this.indicateur_data2.france[0]
        }
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
      // this.units.length = 0
      this.leftColProps.currentValues = []
      this.leftColProps.evolcodes = []
      this.leftColProps.evolvalues = []

      this.leftColProps.names.push(this.indicateur_data.nom)
      if (this.indicateur_data2) {
        this.leftColProps.names.push(this.indicateur_data2.nom)
      }
      // this.units.push(this.indicateur_data.unite, this.indicateur_data2.unite)
      this.leftColProps.currentValues.push(geoObject.last_value)
      if (this.indicateur_data2) {
        this.leftColProps.currentValues.push(geoObject2.last_value)
      }
      this.leftColProps.currentDate = this.convertDateToHuman(geoObject.last_date)
      this.leftColProps.evolcodes.push(geoObject.evol_color, geoObject2.evol_color)
      this.leftColProps.evolvalues.push(geoObject.evol_percentage, geoObject2.evol_percentage)

      this.labels.length = 0
      this.dataset.length = 0
      this.dataset2.length = 0

      geoObject.values.forEach(function (d) {
        self.labels.push(self.convertDateToHuman(d.date))
        self.dataset.push((d.value))

        const correspondingValue = geoObject2.values.find(obj => {
          return obj.date === d.date
        })
        if (correspondingValue) {
          self.dataset2.push(correspondingValue.value)
        }
      })
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
  .panel-full-page-lg {
    height: 100%;
    max-height: 100%;

    > div {
      height: 100%;
      max-height: 100%;
    }

    .container {
      height: 100%;
      max-height: 100%;
    }

    .chart-container {
      height: 40%;
      max-height: 40%;

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

    .map-container {
      height: 65%;
      max-height: 65%;

      > div {
        height: 100%;
        max-height: 100%;

        > div {
          height: 100%;
          max-height: 100%;

          > .france_container {
            height: 80%;
            max-height: 80%;

            .svg {
              max-height: 80%;
              margin-left: 0;
              margin-right: 0;
            }
          }
        }

        .om_container {
          svg {
            max-height: 30%;
          }
        }
      }
    }
  }
</style>
