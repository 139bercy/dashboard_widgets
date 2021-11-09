<template>
  <div class="map-point-panel" v-if="!loading">
    <div v-if="indicateurs.length > 0" class="fr-grid-row">
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

      <div class="map-container fr-col-12 fr-col-lg-9" v-if="indicateurs.length > 0">
        <MapPoint class="map-container fr-col-12" :indicateurs="indicateurs" :activatedIndicateurs="activatedIndicateurs">
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
      dataset: [],
      indicateurs: [],
      activatedIndicateurs: [],
      loading: true
    }
  },
  methods: {
    async getData (indicateur) {
      const data = await store.dispatch('getData', indicateur)
      return data && data.points ? data.points.length : 0
    },
    selectIndicateur(value, activated) {
      let activatedIndicateurs = this.activatedIndicateurs.filter(key => key !== value);
      if (activated) {
        activatedIndicateurs = activatedIndicateurs.concat(value)
      }
      this.activatedIndicateurs = activatedIndicateurs
    },
  },
  async created() {
    let indicateurs = this.onglet.indicateurs[0].Code_indicateur.split('|')
    let indicateursVides = [];
    (await Promise.all(indicateurs.map(async indicateur => {
      return await this.getData(indicateur)
    }))).forEach((nbPoints, index) => {
      if (nbPoints === 0) {
        indicateursVides.push(index)
      }
    })
    this.indicateurs = indicateurs.filter((_, i) => !indicateursVides.includes(i))


    this.activatedIndicateurs = [].concat(this.indicateurs).splice(0,4)
    // console.log(this.activatedIndicateurs.join('\t|\t'))
    this.loading = false
  },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.map-point-panel {
  min-height: 300px;
  height: 100%;
  max-height: 100%;
  .map-container {
    min-height: 300px;
    height: 100%;
    max-height: 100%;
  }
  > div {
    min-height: 300px;
    height: 100%;
    max-height: 100%;
  }
  .map-legend {
    height: 100%;
    overflow: auto;
  }
}
</style>
