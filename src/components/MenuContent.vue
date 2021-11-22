<template>
  <scrollactive
    active-class="fr-sidemenu__item--active"
    id="menu-france-relance"
    class="fr-sidemenu fr-sidemenu--sticky-full-height fr-pr-0"
    role="navigation"
    aria-label="Menu latéral"
  >
    <div class="fr-sidemenu__inner">
      <button
        class="fr-sidemenu__btn"
        aria-controls="fr-sidemenu-wrapper"
        :aria-expanded="showMenu"
        v-on:click="showMenu = !showMenu"
      >
        Dans cette rubrique
      </button>
      <div
        class="fr-collapse fr-pt-0 fr-pt-md-4w fr-pb-md-11w"
        id="fr-sidemenu-wrapper"
        v-show="showMenu || $screen.breakpoint !== 'sm'"
        :class="{
          'fr-collapse--expanded': showMenu || $screen.breakpoint !== 'sm',
        }"
      >
      <!-- <img src="https://www.agence-francaise-anticorruption.gouv.fr/files/2018-11/logo-afa.png" alt="Flowers in Chania"> -->
        <div class="fr-sidemenu__title">
          Affiner la recherche par territoire :
        </div>
        <geo-list></geo-list>
        <div class="fr-sidemenu__title">Naviguer par volet :</div>

        <ul class="fr-sidemenu__list" v-for="volet in volets" :key="volet">
          <li class="fr-sidemenu__item">
            <button
              class="fr-sidemenu__btn"
              :aria-expanded="voletOpened[volet]"
              v-on:click="toggleMenuList(volet)"
            >
              Volet {{ volet }}
            </button>
            <ul class="fr-sidemenu__list" v-show="voletOpened[volet]">
              <li
                class="fr-sidemenu__item fr-sidemenu__link scrollactive-item"
                v-for="(panneau, index) in panneauxByVolets[volet]"
                :key="index"
                :data-section-selector="
                  '#panel_' + toJsonNameFormat(panneau.Titre_panneau)
                "
              >
                {{ panneau.Titre_panneau }}
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </scrollactive>
</template>

<script>
import { mixin } from '@/utils.js'
import GeoList from '@/components/GeoList'

export default {
  name: 'MenuContent',
  components: {
    GeoList,
  },
  mixins: [mixin],
  props: {
    panneaux: Array,
  },
  data() {
    return {
      volets: [],
      voletOpened: [],
      panneauxByVolets: [],
      activeVolet: null,
      activePanneau: null,
      showMenu: false,
    };
  },
  mounted() {
    this.processPanneaux();
  },
  methods: {
    processPanneaux() {
      if (this.panneaux.length > 0) {
        this.volets = [];
        this.panneauxByVolets = [];
        this.panneaux.forEach((panneau) => {
          if (!this.volets.includes(panneau.Volet)) {
            this.volets.push(panneau.Volet);
            this.panneauxByVolets[panneau.Volet] = [];
            this.toggleMenuList(panneau.Volet, false);
          }
          this.panneauxByVolets[panneau.Volet].push(panneau);
        });
        this.toggleMenuList(this.panneaux[0].Volet, true);
        this.activeVolet = this.panneaux[0].Volet;
        this.activePanneau = 0;
      }
    },
    toggleMenuList(volet, value) {
      if (value !== undefined) {
        this.$set(this.voletOpened, volet, value);
      } else {
        this.$set(this.voletOpened, volet, !this.voletOpened[volet]);
      }
    },
    setSelected(volet, indexPanneau) {
      this.activeVolet = volet;
      this.toggleMenuList(volet, true);
      this.activePanneau = indexPanneau;
    },
  },
  watch: {
    panneaux: function () {
      this.processPanneaux();
    },
  },
};
</script>

<style lang="scss">
@use "sass:meta";

#menu-france-relance {
  .fr-select {
    box-shadow: inset 0 -2px 0 0 var(--bf500-plain);
    //-moz-appearance: none;
    background: var(--beige);
  }

  button.fr-link {
    border: solid 1px var(--w-bf500);
  }

  .fr-collapse--expanded {
    --collapse: -564px;
    max-height: none;
  }
}
</style>
<style scoped lang="scss">
// Fix incompatibility between DSFR and vue-scrollactive
.fr-sidemenu__link {
  cursor: pointer;
}
.fr-sidemenu__item--active.fr-sidemenu__link {
  color: var(--bf500);
  box-shadow: inset 1px 0 var(--boxshadow);
}
</style>
