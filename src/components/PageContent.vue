<template style="margin: 0;">
  <div class="page-content fr-container">
    <div class="fr-grid-row">

      <div class="fr-col-12 fr-col-md-4 fr-col-lg-3" v-if="displaySearch">
        <menu-content :panneaux="panneaux"></menu-content>
      </div>
      <div class="fr-col-12 fr-col-md-7 fr-col-lg-7 fr-ml-md-6w fr-mb-6w">
        <div v-html="descriptionContent"></div>

        <div v-for="(panneau, index) in panneaux" :key="index">
          <panel
            v-bind:index="index + ''"
            v-bind="panneau"
            :logo="logo"
            :alt-logo="altLogo"
            :line-chart-configuration="lineChartConfigurationContent"
            :bar-chart-configuration="barChartConfigurationContent">
          </panel>
        </div>

        <SourceLinks class="fr-col-12 fr-col-md-12 fr-col-lg-12 fr-mt-3w" :source-links="sourceLinks"/>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import MenuContent from '@/components/MenuContent'
import Panel from '@/components/Panel'
import SourceLinks from '@/components/SourceLinks'

export default {
  name: 'PageContent',
  components: {
    MenuContent,
    Panel,
    SourceLinks
  },
  props: {
    customRootCss: String,
    configuration: String,
    dataset: String,
    displaySearch: Boolean,
    description: String,
    sourceLinks: String,
    logo: String,
    altLogo: String,
    lineChartConfiguration: String,
    barChartConfiguration: String
  },
  data() {
    return {
      panneaux: [],
      descriptionContent: '',
      lineChartConfigurationContent: {},
      barChartConfigurationContent: {}
    }
  },
  methods: {
    async getData() {
      store.commit('setDataset', this.dataset)
      await fetch(this.configuration)
          .then(res => res.json())
          .then(data => {
            this.panneaux = data
          })
      if (this.description!== undefined && this.description !== '') {
        const self = this
        await fetch(this.description)
          .then(res => res.text())
          // hack pour intégrer le nombre d'indicateurs dans la description
          .then(data => this.descriptionContent = data.replace("{{ panneaux.length }}", this.panneaux.length))
      }
      if (this.lineChartConfiguration!== undefined && this.lineChartConfiguration !== '') {
        const self = this
        try {
          this.lineChartConfigurationContent = JSON.parse(
            await fetch(this.lineChartConfiguration)
              .then(res => res.text())
          )
        } catch (e) {
          console.error(e)
        }
      }
      if (this.barChartConfiguration!== undefined && this.barChartConfiguration !== '') {
        const self = this
        try {
          this.barChartConfigurationContent = JSON.parse(
            await fetch(this.barChartConfiguration)
              .then(res => res.text())
          )
        } catch (e) {
          console.error(e)
        }
      }
    }
  }
  ,
  created() {
    this.getData()
  },
  mounted () {
    if(this.customRootCss && this.customRootCss != '') {
      var element = document.createElement("link");
      element.setAttribute("rel", "stylesheet");
      element.setAttribute("type", "text/css");
      element.setAttribute("href", this.customRootCss);
      document.getElementsByTagName("head")[0].appendChild(element);
    }
  }
}
</script>

<style scoped lang="css">

</style>

<style lang="scss">

@import "../../css/hack.dsfr.min.scss";
@import "../../css/overload-fonts.css";

.page-content {
  @include dsfr;
}

</style>
