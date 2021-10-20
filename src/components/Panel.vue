<template>
  <div :id="'panel_' + toJsonNameFormat(Titre_panneau)" class="panel">
    <div :class="{'full-page-lg': $screen.breakpoint === 'lg', 'only-one-element': onlyOneElement && !points}">
      <div class="lvl2-header fr-px-2w fr-px-md-3w fr-pt-3w">
        <h3>{{ Titre_panneau }}</h3>
      </div>
      <div class="fr-tabs">
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
            <line-map-panel :onglet="onglet" v-if="onglet.Graph || onglet.Carte"></line-map-panel>
            <MapPointPanel :onglet="onglet" v-if="onglet.Points ">
              <!-- && indicateur_data && this.indicateur_data.points -->
            </MapPointPanel>
          </div>
        </div>
      </div>
    </div>
    <div class="fr-accordion panel-accordion-extended" :class="{'mobile' : $screen.breakpoint === 'xs' || $screen.breakpoint === 'sm' }">
      <h3 class="fr-accordion__title">
        <button class="fr-accordion__btn fr-text--sm"
                :aria-expanded="accordionOpened"
                v-on:click="accordionOpened=!accordionOpened"
        >
          En savoir plus sur la mesure
        </button>
      </h3>
      <div class="fr-pl-2v fr-pr-2v fr-col-12" v-show="accordionOpened">
        <p class="description-mesure fr-mb-0 fr-text--sm fr-pb-1v">
          {{ onglets[0].Description_mesure }}
        </p>
        <p class="fr-text--xs fr-mb-3w fr-pb-1v">Source :
          {{source}}
          <a title="vers data.gouv.fr" v-bind:href="Lien_page_mesure"
             target="_blank" rel="noopener" data-section="nom_section"
             data-subsection="nom_subsection">
            Vers des fichiers d'open-data</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>

import { mixin } from '@/utils.js'
import LineMapPanel from './LineMapPanel'
import MapPointPanel from './MapPointPanel.vue'

export default {
  name: 'Panel',
  mixins: [mixin],
  components: {
    LineMapPanel,
    MapPointPanel
  },
  props: {
    index: String,
    Titre_panneau: String,
    Lien_page_mesure: String,
    source: String,
    onglets: Array
  },
  data() {
    return {
      currentOnglet: this.onglets[0],
      accordionOpened: false
    }
  },
  computed: {
    onlyOneElement() {
      return this.currentOnglet.Carte && !this.currentOnglet.Graph && !this.currentOnglet.Points
      || !this.currentOnglet.Carte && this.currentOnglet.Graph && !this.currentOnglet.Points
      || !this.currentOnglet.Carte && !this.currentOnglet.Graph && this.currentOnglet.Points
    },
    points() {
      return this.currentOnglet.Carte && !this.currentOnglet.Graph && !this.currentOnglet.Points
      || !this.currentOnglet.Carte && this.currentOnglet.Graph && !this.currentOnglet.Points
      || !this.currentOnglet.Carte && !this.currentOnglet.Graph && this.currentOnglet.Points
    }
  },
  methods: {}
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  // Gestion du positionnement sur grand écran (breakpoint lg)
  @media (min-width: 62em) {
    .full-page-lg {
      &:not(.only-one-element) {
        height: 97vh;
        max-height: 97vh;
        overflow: hidden;
      }
      &.only-one-element {
        height: 45vh;
        max-height: 45vh;
        overflow: hidden;
      }
      & > .fr-tabs {
        height: calc(100% - 60px);
        max-height: calc(100% - 60px);
        .fr-tabs__panel--selected {
          height: calc(100% - 60px);
          max-height: calc(100% - 60px);
          > div {
            height: 100%;
            max-height: 100%;
          }
        }
      }
    }
  }
  // Gestion de la bordure autour d'un panel
  .fr-tabs {
    transition: none 0s ease 0s;
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
      padding-top: 2.0rem !important;
      padding-bottom: 0.5rem !important;
    }
    &:after {
      box-shadow: inset 1px 0 var(--boxshadow), inset -1px 0 0 var(--boxshadow) !important;
    }
  }
  .fr-accordion {
    &.mobile {
      margin-left: calc(50% - 50vw);
      margin-right: calc(50% - 50vw);
    }
    box-shadow: inset 1px -1px var(--boxshadow), inset -1px 0 0 var(--boxshadow) !important;
    // Fin de gestion de la bordure autour d'un panel
    .description-mesure {
      text-align: justify;
      margin-top: 1rem;
    }
  }
</style>
