<template>
  <nav id="menu-france-relance" class="fr-sidemenu fr-sidemenu--sticky-full-height fr-pr-0" role="navigation"
       aria-label="Menu latéral">
    <div class="fr-sidemenu__inner">
      <div class="fr-collapse fr-pt-0 fr-pt-md-4w fr-pb-md-11w" id="fr-sidemenu-wrapper">
        <div class="fr-sidemenu__title">Affiner la recherche par territoire :</div>
        <geo-list></geo-list>
        <div class="fr-sidemenu__title">Naviguer par volet :</div>
        <ul class="fr-sidemenu__list" v-for="volet in volets" :key="volet">

          <li class="fr-sidemenu__item">
            <button class="fr-sidemenu__btn"
                    :aria-expanded="voletOpened[volet]"
                    v-on:click="toggleMenuList(volet)"
            >
              Volet {{ volet }}
            </button>
              <ul class="fr-sidemenu__list" v-show="voletOpened[volet]">
                <li class="fr-sidemenu__item fr-sidemenu__item"
                    v-for="(panneau, index) in panneauxByVolets[volet]" :key="index"
                >
                  <a class="fr-sidemenu__link" data-section="volet_cohesion"
                     data-name="point_de_situation"
                     :href="'#panel_' + toJsonNameFormat(panneau.Nom_mesure_GP)"
                     target="_self">
                    {{ panneau.Nom_mesure_GP }}
                  </a>
                </li>
              </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mixin } from '@/utils.js'
import GeoList from '@/components/GeoList'

export default {
  name: 'MenuContent',
  components: {
    GeoList
  },
  mixins: [mixin],
  props: {
    panneaux: Array
  },
  data () {
    return {
      volets: [],
      voletOpened: [],
      panneauxByVolets: []
    }
  },
  mounted () {
    this.processPanneaux()
  },
  methods: {
    processPanneaux () {
      if (this.panneaux.length > 0) {
        this.volets = []
        this.panneauxByVolets = []
        this.panneaux.forEach((panneau) => {
          if (!this.volets.includes(panneau.Volet)) {
            this.volets.push(panneau.Volet)
            this.panneauxByVolets[panneau.Volet] = []
            this.toggleMenuList(panneau.Volet, false)
            this[panneau.Volet + 'Opened'] = false
          }
          this.panneauxByVolets[panneau.Volet].push(panneau)
        })
        this.toggleMenuList(this.panneaux[0].Volet, true)
      }
    },
    toggleMenuList (volet, value) {
      if (value !== undefined) {
        this.$set(this.voletOpened, volet, value)
      } else {
        this.$set(this.voletOpened, volet, !this.voletOpened[volet])
      }
    }
  },
  watch: {
    panneaux: function () {
      this.processPanneaux()
    }
  }
}

</script>

<style lang="scss">
#menu-france-relance .fr-select {
  box-shadow: inset 0 -2px 0 0 var(--bf500-plain);
  //-moz-appearance: none;
  background: var(--beige);
}

#menu-france-relance button.fr-link {
  border: solid 1px var(--w-bf500);
}

#menu-france-relance  .fr-accordion {
    box-shadow: 0 0 0 0 var(--boxcountour), 0 0 0 0 var(--boxcountour)
}
</style>
<style scoped lang="scss">
</style>
