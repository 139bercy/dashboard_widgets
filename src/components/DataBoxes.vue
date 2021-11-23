<template>
  <!-- class="chart-map-panel" :class="{'panel-full-page-lg': $screen.breakpoint === 'lg', 'only-one-element' : onlyOneElement}" -->
  <div>
    <div v-if="indicateur_data && !loading" class="fr-grid-row add-padding">
      <div class="fr-col-12 fr-col-md-6 fr-col-lg-4"
        :class="{'fr-p-2w': onglet.indicateurs.length > 3, 'fr-p-3w': onglet.indicateurs.length <= 3}"
        v-for="(indicateur, indexIndicateur) in onglet.indicateurs" :key="indexIndicateur">
        <DataBox
          :indicateur="getIndicateurCode(indicateur)" :unit="getIndicateurUnit(indicateur)">
        </DataBox>
      </div>
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
import DataBox from './DataBox.vue'
import { mixin } from '@/utils.js'

export default {
  name: 'ChartMapPanel',

  mixins: [mixin],
  components: {
    DataBox
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
    selectedGeoLevel() {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode() {
      return store.state.user.selectedGeoCode
    },
    selectedGeoLabel() {
      return store.state.user.selectedGeoLabel
    },
    onlyOneElement() {
      return this.onglet.Carte && !this.onglet.Graph && !this.onglet.Bar
      || !this.onglet.Carte && this.onglet.Graph && !this.onglet.Bar
      || !this.onglet.Carte && !this.onglet.Graph && this.onglet.Bar
    }
  },
  methods: {
    getIndicateurCode(indicateur) {
      return indicateur.Code_indicateur
    },
    getIndicateurUnit(indicateur) {
      return indicateur["Unité_Evol"]
    },
    async getData() {
      const self = this
      this.loading = true
      const promises = this.onglet.indicateurs.map(function (indicateur) {
        return store.dispatch('getData', self.getIndicateurCode(indicateur)).then(data => {
          self.indicateur_data = data
        })
      })

      Promise.all(promises).then(_ => {
        this.loading = false
      }).catch(_ => {
        this.loading = false
      })
    },
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
<style scoped lang="scss">

.add-padding {
  padding: 0.75rem;
}
</style>
