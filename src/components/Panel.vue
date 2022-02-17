<template>
  <div :id="'panel_' + toJsonNameFormat(Titre_panneau)" class="panel">
    <div :class="{'full-page-lg': $screen.breakpoint === 'lg', 'flex-data-boxes': onlyBoxes}">
      <div class="lvl2-header fr-px-2w fr-px-md-3w fr-pt-3w">
        <h3>{{ Titre_panneau }}</h3>
      </div>
      <div class="fr-tabs" :class="{'box-shadow-without-descrption-mesure': !onglets[0].Description_mesure}">
        <ul class="fr-tabs__list" role="tablist" aria-label="changer d'onglet">
          <li role="presentation" v-for="(onglet, indexOnglet) in onglets" :key="indexOnglet"
              :is-selected="currentOnglet === onglet">
            <button class="fr-tabs__tab" v-on:click="currentOnglet=onglet"
                    :tabindex="indexOnglet" role="tab"
                    :aria-selected="currentOnglet === onglet"
                    :aria-controls="'tabpanel-' + indexOnglet + '-panel'"
            >
              {{ onglet.Titre_onglet }}
            </button>
          </li>
        </ul>

        <div :id="'tabpanel-' + indexOnglet + '-panel'"
             class="fr-tabs__panel fr-pt-2w fr-mt-3w"
             :class="{'fr-tabs__panel--selected' : currentOnglet.indicateurs.length > 0 && currentOnglet === onglet}"
             v-for="(onglet, indexOnglet) in onglets" :key="indexOnglet"
             role="tabpanel"
             :tabindex="currentOnglet === onglet ? 1 : 0"
             :aria-selected="currentOnglet === onglet ? 1 : 0">
          <div v-if="currentOnglet.indicateurs.length > 0 && currentOnglet === onglet">
            <ChartMapPanel
              :onglet="onglet"
              :logo="logo" :alt-logo="altLogo"
              :project-configuration="projectConfiguration"
              :line-chart-configuration="lineChartConfiguration"
              :bar-chart-configuration="barChartConfiguration"
              :map-chart-configuration="mapChartConfiguration"
              v-if="chartPanel">
            </ChartMapPanel>
            <MapPointPanel
              :onglet="onglet"
              :logo="logo" :alt-logo="altLogo"
              v-if="onglet.Points">
            </MapPointPanel>
            <DataBoxes
              :onglet="onglet"
              :logo="logo" :alt-logo="altLogo"
              v-if="onglet.Box && !onglet.Graph && !onglet.Bar">
            </DataBoxes>
          </div>
        </div>
      </div>
    </div>
    <div
      class="fr-accordion panel-accordion-extended"
      :class="{'mobile' : $screen.breakpoint === 'xs' || $screen.breakpoint === 'sm' }"
      v-if="onglets[0].Description_mesure">
      <h3 class="fr-accordion__title">
        <button class="fr-accordion__btn fr-text--sm"
                :aria-expanded="accordionOpened"
                v-on:click="accordionOpened=!accordionOpened"
        >
          <!-- En savoir plus sur la mesure -->
          {{accordéon}}
        </button>
      </h3>
      <div class="fr-col-12" v-show="accordionOpened">
        <p class="description-mesure fr-mb-0 fr-text--sm">
          {{ onglets[0].Description_mesure }}
        </p>
        <p class="fr-text--xs">Source :
          {{source}}.
          <a title="Sources et références" v-bind:href="Lien_page_mesure"
             target="_blank" rel="noopener" data-section="nom_section"
             data-subsection="nom_subsection">
            {{titre_page_mesure}}</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>

import { mixin } from '@/utils.js'
import ChartMapPanel from './ChartMapPanel'
import MapPointPanel from './MapPointPanel.vue'
import DataBoxes from './DataBoxes.vue'

export default {
  name: 'Panel',
  mixins: [mixin],
  components: {
    ChartMapPanel,
    MapPointPanel,
    DataBoxes
  },
  props: {
    index: String,
    Titre_panneau: String,
    Lien_page_mesure: String,
    titre_page_mesure: String,
    source: String,
    accordéon: String,
    onglets: Array,
    logo: String,
    altLogo: String,
    projectConfiguration: Object,
    lineChartConfiguration: Object,
    barChartConfiguration: Object,
    mapChartConfiguration: Object
  },
  data() {
    return {
      currentOnglet: this.onglets[0],
      accordionOpened: false
    }
  },
  computed: {
    chartPanel() {
      return this.currentOnglet.Carte
        || this.currentOnglet.Graph
        || this.currentOnglet.Bar
        || this.currentOnglet.Pie
        || this.currentOnglet.Table
        || this.currentOnglet.Info
    },
    onlyBoxes() {
      return this.currentOnglet.Box && !this.currentOnglet.Graph
    },
    points() {
      return this.currentOnglet.Points
    }
  },
  methods: {}
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  // Gestion du positionnement sur grand écran (breakpoint lg)
  
  // Gestion de la bordure autour d'un panel
  .fr-tabs {
    transition: none 0s ease 0s;

    &.box-shadow-without-descrption-mesure {
      box-shadow:  0px 1px var(--boxshadow);
    }
    .fr-tabs__list {
      &::after {
        box-shadow: inset 1px -1px 0 0 var(--boxshadow), inset -1px 0 0 var(--boxshadow);
      }
      > li {
        margin-left: 0 !important;
        &[is-selected="true"] {
          box-shadow: inset 1px 0 var(--boxshadow), inset -1px 0 var(--boxshadow), inset 0 1px var(--boxshadow);
        }
        .fr-tabs__tab {
          &[aria-selected="true"] {
            box-shadow: none;
          }
          &[aria-selected="true"]:after {
            box-shadow: none;
          }
          &:not([aria-selected="true"]) {
            box-shadow: inset 0 -1px var(--boxshadow);
          }
          &::after {
            box-shadow: none;
          }
        }
        &:not(:last-of-type) {
          margin-right: 0 !important;
        }
        &:first-of-type::before {
          box-shadow: inset 1px -1px var(--boxshadow);
        }
        &:not(:first-of-type)::before {
          box-shadow: none;
        }
        &:not(:last-of-type)::after {
          //box-shadow: -1px 0 var(--boxshadow);
          box-shadow: none;
        }
        &:last-child {
          padding-right: 0;
        }
        &::after {
          box-shadow: none;
        }
      }
    }
    .fr-tabs__panel {
      padding: 20px;
    }
    &:after {
      box-shadow: inset 1px 0 var(--boxshadow), inset -1px 0 0 var(--boxshadow) !important;
    }
  }

  .fr-accordion {
    box-shadow: inset 1px -1px var(--boxshadow), inset -1px 0 0 var(--boxshadow) !important;
    // Fin de gestion de la bordure autour d'un panel
    .description-mesure {
      text-align: justify;
    }

    &.panel-accordion-extended {
      border-top: 1px dashed #818080;

      .fr-accordion__title {
        border-bottom: 1px dashed #818080;
        padding: 0;
        button {
          font-weight: bold;
          padding: 10px 20px;
        }
      }

      > div {
        padding: 20px;
        p {
          margin: 0;
          text-align: justify;
        }
        p:first-child {
          margin-bottom: 10px !important;
        }
      }
    }
  }

  

  

  
</style>
