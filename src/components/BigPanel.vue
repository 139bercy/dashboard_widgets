<template>
  
  <div :id="panel_id" class="fr-mt-6w">
    <a class="anchor"></a>
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
              <button id="tabpanel-1" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true">Nombre d'entreprises
          </button>
          </li>
          <li role="presentation">
              <button id="tabpanel-2" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" v-if="card_onglet>=2">Montant total de l'investissement
          </button>
          </li>
          <li role="presentation">
              <button id="tabpanel-3" class="fr-tabs__tab" tabindex="-2" role="tab" aria-selected="false" v-if="card_onglet>=3">Montant total de l'investissement
          </button>
          </li>
      </ul>

      <div id="tabpanel-1-panel" class="fr-tabs__panel fr-tabs__panel--selected fr-p-3w" role="tabpanel" aria-labelledby="tabpanel-1" tabindex="0">
        <div style="margin-bottom: 2rem">
            <line-chart :indicateur="indicateur1" v-if="card_line1==1"></line-chart>
            <multiline-chart :indicateur1="indicateur1" :indicateur2="indicateur1bis" v-if="card_line1==2"></multiline-chart>
        </div>
        <map-chart :indicateur="indicateur1" v-if="map1"></map-chart>

        <section class="fr-accordion">
            <h3 class="fr-accordion__title">
              <button id="accordion1-1" class="fr-accordion__btn fr-text--sm" aria-expanded="false">
                En savoir plus sur la mesure :
              </button>
            </h3>
            <div class="fr-collapse fr-mx-0" id="accordion1-2">
                <p class="fr-mb-0 fr-text--sm">
                  {{Propriétés_mesure}}
                </p>
            </div>
        </section>
      </div>

      <!-- Onglet 2 -->

      <div id="tabpanel-2-panel" class="fr-tabs__panel fr-p-3w" role="tabpanel" aria-labelledby="tabpanel-2" tabindex="-1" v-if="card_onglet>=2">
        <div style="margin-bottom: 2rem">
            <line-chart :indicateur="indicateur2" v-if="card_line2==1"></line-chart>
            <multiline-chart :indicateur1="indicateur2" :indicateur2="indicateur2bis" v-if="card_line2==2"></multiline-chart>
        </div>
        <map-chart :indicateur="indicateur2" v-if="map2"></map-chart>

        
        <section class="fr-accordion">
            <h3 class="fr-accordion__title">
              <button id="accordion2-1" class="fr-accordion__btn fr-text--sm" aria-expanded="false">
                En savoir plus sur la mesure :
              </button>
            </h3>
            <div class="fr-collapse fr-mx-0" id="accordion2-2">
                <p class="fr-mb-0 fr-text--sm">
                  {{Propriétés_mesure}}
                </p>
            </div>
        </section>
      </div>

      <!-- Onglet 3 -->

      <div id="tabpanel-3-panel" class="fr-tabs__panel fr-p-3w" role="tabpanel" aria-labelledby="tabpanel-3" tabindex="-2" v-if="card_onglet>=3">
        <div style="margin-bottom: 2rem">
            <line-chart :indicateur="indicateur3" v-if="card_line3==1"></line-chart>
            <multiline-chart :indicateur="indicateur3" :indicateur2="indicateur3bis" v-if="card_line3==2"></multiline-chart>
        </div>
        <map-chart :indicateur="indicateur3" v-if="map2"></map-chart>      

        <section class="fr-accordion">
            <h3 class="fr-accordion__title">
              <button id="accordion3-1" class="fr-accordion__btn fr-text--sm" aria-expanded="false">
                En savoir plus sur la mesure :
              </button>
            </h3>
            <div class="fr-collapse fr-mx-0" id="accordion3-2">
                <p class="fr-mb-0 fr-text--sm">
                  {{Propriétés_mesure}}
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

  props: {
    panel_id: String,
    source_http: String,
    indicateur1: String,
    indicateur1bis: String,
    indicateur2: String,
    indicateur2bis: String,
    indicateur3: String,
    indicateur3bis: String,
    Propriétés_mesure: String,
    card_line1: Number,
    card_line2: Number,
    card_line3: Number,
    card_onglet: Number,
    map1: Boolean,
    map2: Boolean,
    map3: Boolean,
  },
  
  data(){

    return {
    };
    
  },

  actions: {

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
    
    var tabpanel_id1 = 'tabpanel1' + this.panel_id;
    document.getElementById('tabpanel-1').setAttribute('aria-controls', tabpanel_id1);
    document.getElementById('tabpanel-1-panel').setAttribute('id', tabpanel_id1);
    var accordion_id1 = 'accordion1' + this.panel_id;
    document.getElementById('accordion1-1').setAttribute('aria-controls', accordion_id1);
    document.getElementById('accordion1-2').setAttribute('id', accordion_id1);
    if (this.card_onglet >= 2) {
      var tabpanel_id2 = 'tabpanel2' + this.panel_id;
      document.getElementById('tabpanel-2').setAttribute('aria-controls', tabpanel_id2);
      document.getElementById('tabpanel-2-panel').setAttribute('id', tabpanel_id2);
      var accordion_id2 = "accordion2" + this.panel_id;
      document.getElementById('accordion2-1').setAttribute('aria-controls', accordion_id2);
      document.getElementById('accordion2-2').setAttribute('id', accordion_id2);
    }
    if (this.card_onglet>= 3) {
      var tabpanel_id3 = 'tabpanel3' + this.panel_id;
      document.getElementById('tabpanel-3').setAttribute('aria-controls', tabpanel_id3);
      document.getElementById('tabpanel-3-panel').setAttribute('id', tabpanel_id3);
      var accordion_id3 = "accordion3" + this.panel_id;
      document.getElementById('accordion3-1').setAttribute('aria-controls', accordion_id3);
      document.getElementById('accordion3-2').setAttribute('id', accordion_id3);
    } 
  }

};

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
