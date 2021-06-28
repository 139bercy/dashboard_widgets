<template>
  <nav class="fr-sidemenu fr-sidemenu--sticky-full-height fr-pr-0" role="navigation"
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

export default {
  name: 'MenuContent',
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
  methods: {
    toggleMenuList (volet, value) {
      if (value !== undefined) {
        this.$set(this.voletOpened, volet, value)
      } else {
        this.$set(this.voletOpened, volet, !this.voletOpened[volet])
      }
    }
  }
}

</script>

<style scoped lang="scss">

</style>
