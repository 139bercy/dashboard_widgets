<template>
  <div>
    <div class="chart_container" v-if="onglet.indicateurs.length > 0 && onglet.Graph">
      <line-chart
          interpolation="monotone"
          :indicateur="indicateurName1"
          :top-col="false"
          :left-col="true"
          v-if="onglet.indicateurs.length === 1">
      </line-chart>
      <multi-line-chart
          class="chart_container"
          interpolation="monotone"
          :indicateur1="indicateurName1"
          :indicateur2="indicateurName2"
          :top-col="false"
          :left-col="true"
          v-if="onglet.indicateurs.length === 2">
      </multi-line-chart>
    </div>
    <div class="fr-grid-row">

      <left-col :class="{'map-legend': $screen.breakpoint == 'lg'}" class="fr-col-2" v-bind="leftColProps"></left-col>
      <map-chart
          class="fr-col-12"
          :indicateur="indicateurName1"
          :top-col="false"
          :left-col="false"
          :bottom-col="false"
          :DOMTOMBottom="false"
          v-if="onglet.Carte">
      </map-chart>
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
  data () {
    return {
      indicateur_data: undefined,
      indicateur_data2: undefined,
      dataset: [],
      dataset2: [],
      leftColProps: {
        min: 0,
        max: 0,
        isMap: true
      }
    }
  },
  computed: {
    selectedGeoLevel () {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode () {
      return store.state.user.selectedGeoCode
    },
    selectedGeoLabel () {
      return store.state.user.selectedGeoLabel
    },
    indicateurName1 () {
      return this.toJsonNameFormat(this.onglet.indicateurs[0].Nom_indicateur_propilot)
    },
    indicateurName2 () {
      return this.toJsonNameFormat(this.onglet.indicateurs[1].Nom_indicateur_propilot)
    }
  },
  methods: {
    async getData () {
      store.dispatch('getData', this.toJsonNameFormat(this.onglet.indicateurs[0].Nom_indicateur_propilot)).then(data => {
        this.indicateur_data = data
        this.updateData()
      })
    },
    updateData () {
      const values = []

      this.indicateur_data.departements.forEach(function (d) {
        values.push(parseInt(d.last_value))
      })

      this.scaleMin = Math.min.apply(null, values)
      this.scaleMax = Math.max.apply(null, values)

      this.leftColProps.min = this.scaleMin
      this.leftColProps.max = this.scaleMax
    }
  },
  created () {
    this.getData()
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.map-legend {
  margin-bottom: -75px;
}

</style>
