<template>

  <div class="fr-mt-6w">
    <a class="anchor" :id="panel_id"></a>
    <div class="lvl2-header fr-px-2w fr-px-md-3w fr-pt-3w">
        <h3> Modernisation de la filière (BPI)
        </h3>
        <p class="fr-text--xs fr-mb-3w">Source :
            <a title="vers data.gouv.fr" :href="source_http" target="_blank" rel="noopener" data-section="nom_section" data-subsection="nom_subsection">
            Vers des fichiers d'open-data</a>
        </p>
    </div>

    <div class="fr-tabs" style="transition: none 0s ease 0s;">

        <ul class="fr-tabs__list" role="tablist" aria-label="changer d'onglet">
            <li role="presentation">
                <button id="tabpanel-2-1" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tabpanel-2-1-panel">Nombre d'entreprises
            </button>
            </li>
            <li role="presentation">
                <button id="tabpanel-2-2" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tabpanel-2-2-panel">Montant total de l'investissement ainsi déclenché
            </button>
            </li>
        </ul>

        <div id="tabpanel-2-1-panel" class="fr-tabs__panel fr-tabs__panel--selected fr-p-3w" role="tabpanel" aria-labelledby="tabpanel-2-1" tabindex="0">
            <div style="margin-bottom: 2rem">
                <multiline-chart :indicateur1="indicateur1" :indicateur2="indicateur1bis"></multiline-chart>
            </div>
            <map-chart :indicateur="indicateur1"></map-chart>

            <section class="fr-accordion">
                <h3 class="fr-accordion__title">
                  <button class="fr-accordion__btn fr-text--sm" aria-expanded="false" aria-controls="accordion1">
                    En savoir plus sur la mesure :
                  </button>
                </h3>
                <div class="fr-collapse fr-mx-0" id="accordion1">
                    <p class="fr-mb-0 fr-text--sm" :text="Propriétés_mesure">
                    </p>
                </div>
            </section>

        </div>

        <div id="tabpanel-2-2-panel" class="fr-tabs__panel fr-p-7w" role="tabpanel" aria-labelledby="tabpanel-2-2" tabindex="1">
            <div style="margin-bottom: 2rem">
                <multiline-chart :indicateur1="indicateur2" :indicateur2="indicateur2bis"></multiline-chart>
            </div>
            <map-chart :indicateur="indicateur2"></map-chart>

            <section class="fr-accordion">
                <h3 class="fr-accordion__title">
                  <button class="fr-accordion__btn fr-text--sm" aria-expanded="false" aria-controls="accordion2">
                    En savoir plus sur la mesure :
                  </button>
                </h3>
                <div class="fr-collapse fr-mx-0" id="accordion2">
                    <p class="fr-mb-0 fr-text--sm" :text="Propriétés_mesure">
                    </p>
                </div>
            </section>

        </div>

    </div>
  </div>

</template>

<script>


export default {
  name: 'BigPanel',
  components: {
  },
  data(){
    return {

    }
  },
  props: {
    panel_id: String,
    source_http: String,
    indicateur1: String,
    indicateur1bis: String,
    indicateur2: String,
    indicateur2bis: String,
    Propriétés_mesure: String,
  },
  computed: {
  },
  methods: {
  },

  watch: {
  },
  

  created(){
  },

  mounted(){
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  
  /* overload fonts path, to delete when parent has access */
  @import "../../public/css/overload-fonts.css";
  @import "../../public/css/dsfr.min.css";

  a {
      color: orange;
  }
  
  body {
      background-color: #f9f8f6;
  }
  
  .chart_container {
      max-width: 750px;
      margin: 0 auto 50px;
  }
  
  .geo_container {
      max-width: 200px;
      margin: 0 auto 50px;
  }
  
</style>
