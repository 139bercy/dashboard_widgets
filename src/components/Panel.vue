<template>
  <div :id="'panel_' + toJsonNameFormat(Nom_mesure_GP)" class="fr-mt-6w">
    <div class="lvl2-header fr-px-2w fr-px-md-3w fr-pt-3w">
      <h3>{{ Nom_mesure_GP }}</h3>
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
            {{ onglet.Nom_indicateur_GP }}
          </button>
        </li>
      </ul>

      <div :id="'tabpanel-' + currentIndexOnglet + '-panel'"
           class="fr-tabs__panel fr-tabs__panel--selected fr-pt-2w fr-mt-3w"
           v-for="(onglet, indexOnglet) in onglets" :key="indexOnglet">
        <div v-if="currentOnglet.indicateurs.length > 0 && currentOnglet.Graph && currentOnglet === onglet">
          <line-map-panel :onglet="onglet"></line-map-panel>
        </div>
      </div>
    </div>
    <div class="fr-accordion fr-col-12">
      <h3 class="fr-accordion__title">
        <button class="fr-accordion__btn fr-text--sm"
                :aria-expanded="accordionOpened"
                v-on:click="accordionOpened=!accordionOpened"
        >
          En savoir plus sur la mesure :
        </button>
      </h3>
      <div class="fr-pl-2v fr-pr-2v fr-col-12" v-show="accordionOpened">
        <p class="description-mesure fr-mb-0 fr-text--sm fr-pb-1v">
          {{ onglets[0].Description_mesure }}
        </p>
        <p class="fr-text--xs fr-mb-3w fr-pb-1v">Source :
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

export default {
  name: 'Panel',
  mixins: [mixin],
  components: {
    LineMapPanel
  },
  props: {
    index: String,
    Nom_mesure_GP: String,
    Lien_page_mesure: String,
    onglets: Array
  },
  data() {
    return {
      currentIndexOnglet: 0,
      currentOnglet: this.onglets[0],
      accordionOpened: false
    }
  },
  methods: {}
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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

}

.fr-tabs::after {
  box-shadow: inset 1px 0 var(--boxshadow), inset -1px 0 0 var(--boxshadow);
}

.fr-accordion {
  box-shadow: inset 1px -1px var(--bf500), inset -1px 0 0 var(--boxshadow);

  .description-mesure {
    text-align: justify;
  }
}

</style>
