<template>
  <div class="map-point-panel">
    <div v-if="indicateur_data && !loading" class="fr-grid-row">
      <MapPointLegend class="map-legend fr-col-12 fr-col-lg-3"
        :logo="logo" :alt-logo="altLogo"
        :indicateurs="indicateurs"
        :selecteur="onglet.Titre_onglet"
        :legende="onglet.indicateurs[0].Titre_indicateur"
        @indicateurSelected="selectIndicateur"
        v-if="$screen.breakpoint === 'lg'">
      </MapPointLegend>
                 <!-- && this.indicateur_data && this.indicateur_data.departements -->
      <!-- <MapPointLegend class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeChart"
                v-if="$screen.breakpoint === 'lg' && this.indicateur_data && !this.indicateur_data.departements"></MapPointLegend>
      <MapPointLegend class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeChart"
                v-if="$screen.breakpoint !== 'lg'"></MapPointLegend> -->
      <div class="map-container fr-col-12 fr-col-lg-9" v-if="onglet.indicateurs.length > 0">
        <MapPoint class="map-container fr-col-12" :indicateur="indicateur">
            <!-- v-if="indicateur_data && this.indicateur_data.points" -->
        </MapPoint>
      </div>
      <!-- <MapPointLegend class="map-legend fr-col-12 fr-col-lg-3" v-bind="leftColPropsNotLargeMap"
                v-if="$screen.breakpoint !== 'lg' && this.indicateur_data && this.indicateur_data.departements"></MapPointLegend> -->
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
import { mixin } from '@/utils.js'
import MapPoint from './MapPoint.vue'
import MapPointLegend from './MapPointLegend.vue'

export default {
  name: 'MapPointPanel',
  mixins: [mixin],
  components: {
    MapPoint,
    MapPointLegend
  },
  props: {
    index: String,
    Titre_panneau: String,
    Lien_page_mesure: String,
    onglet: Object,
    logo: String,
    altLogo: String
  },
  data() {
    return {
      loading: false,
      indicateur_data: [],
      dataset: [],
      indicateur: undefined
    }
  },
  computed: {
    indicateurs() {
      return this.onglet.indicateurs[0].Code_indicateur.split(',')
    },
  },
  methods: {
    selectIndicateur(value) {
      this.indicateur = value
    },
  },
  created() {
    this.indicateur = this.indicateurs[0]
  },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.map-point-panel {
  height: 100%;
  max-height: 100%;
  .map-container {
    height: 100%;
    max-height: 100%;
  }
  > div {
    height: 100%;
    max-height: 100%;
  }
}
</style>
