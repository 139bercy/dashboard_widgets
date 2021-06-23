<template>

  <div class="fr-col-12 fr-col-lg-3">
    
    <div class="flex fr-mt-2w">
      <p class="fr-text--sm fr-text--bold fr-mt-0 fr-mb-1w" style="text-align: right;">{{names[0]}}</p>
    </div> 
    <div class="flex fr-mb-1w" style="float: right;">
      <p class="fr-text--bold fr-mb-1v" style="font-size: vw; margin-right: 15px; vertical-align: middle;">{{convertNumberToHuman(values[0])}}</p>
      <span class="legende_line1"></span>
    </div>

    <div class="flex fr-mt-2w">
      <p class="fr-text--sm fr-text--bold fr-mt-0 fr-mb-1w" style="text-align: right;">{{names[1]}}</p>
    </div> 
    <div class="flex fr-mb-1w" style="float: right;">
      <p class="fr-text--bold fr-mb-1v" style="font-size: vw; margin-right: 15px">{{convertNumberToHuman(values[1])}}</p>
      <span class="legende_line2"></span>
    </div>


  </div>  

</template>

<script>

import store from '@/store'

export default {
  name: 'LeftCol',

  data(){
    return {
      isDown:[false,false],
      isGreen:[false,false],
      isRed:[false,false],
      isBlue:[false,false],
      units:[]
    }
  },
  props: {
    date: String,
    localisation: String,
    values: Array,
    names: Array,
    evolcodes: Array,
    evolvalues : Array,
    min: Number,
    max: Number,
    map: Boolean
  },
  computed: {

  },
  methods: {

    convertNumberToHuman(float){
      return parseFloat(float).toLocaleString()
    },

    testEvolStyle(){
      var self = this
      this.names.forEach(function(n,i){
        if(self.evolcodes[i]=="green"){
          self.isGreen[i] = true
          self.isRed[i] = false
          self.isBlue[i] = false
          self.evolvalues[i] > 0 ? self.isDown[i] = false : self.isDown[i] = true
        }else if(self.evolcodes[i]=="red"){
          self.isGreen[i] = false
          self.isRed[i] = true
          self.isBlue[i] = false
          self.evolvalues[i] > 0 ? self.isDown[i] = false : self.isDown[i] = true
        }else{
          self.isGreen[i] = false
          self.isRed[i] = false
          self.isBlue[i] = true
          self.isDown[i] = false
        }
      })
    }

  },

  watch:{
    evolcodes:function(){
      this.testEvolStyle()
    },
    evolvalues:function(){
      this.testEvolStyle()
    }
  },

  created(){
    this.testEvolStyle()
  },

  capitalize(string){
    if(string){
      return string.charAt(0).toUpperCase() + string.slice(1)
    }
  },

  updateData() {

    var self = this

    var geolevel = this.selectedGeoLevel
    var geocode = this.selectedGeoCode

    this.localGeoLabel = this.selectedGeoLabel

    var geoObject

    geoObject = this.getGeoObject(geolevel, geocode)

    if (typeof geoObject === 'undefined') {
      if (geolevel == 'regions') {
        geoObject = this.getGeoObject("France", "01")
        this.localGeoLabel = "France entière"
        this.geoFallback = true
        this.geoFallbackMsg = "Affichage des résultats au niveau national, faute de données au niveau régional"
      } else {
        var depObj = store.state.dep.find(obj => {
          return obj["value"] === geocode
        })
        geoObject = this.getGeoObject("regions", depObj["region_value"])
        this.localGeoLabel = depObj["region"]
        this.geoFallback = true
        this.geoFallbackMsg = "Affichage des résultats au niveau régional, faute de données au niveau départemental"
        if (typeof geoObject === 'undefined') {
          geoObject = this.getGeoObject("France", "01")
          this.localGeoLabel = "France entière"
          this.geoFallback = true
          this.geoFallbackMsg = "Affichage des résultats au niveau national, faute de données au niveau régional ou départemental"
        }
      }
    }

    this.names.length = 0
    this.units.length = 0
    this.currentValues.length = 0
    this.evolcodes.length = 0
    this.evolvalues.length = 0

    this.names.push(this.indicateur_data["nom"])
    this.units.push(this.indicateur_data["unite"])
    this.currentValues.push(geoObject["last_value"])
    this.currentDate = this.convertDateToHuman(geoObject["last_date"])
    this.evolcodes.push(geoObject["evol_color"])
    this.evolvalues.push(geoObject["evol_percentage"])

    this.labels.length = 0
    this.dataset.length = 0

    geoObject["values"].forEach(function (d) {
      self.labels.push(self.convertDateToHuman(d["date"]))
      self.dataset.push((d["value"]))
    })
  },

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  /* overload fonts path, to delete when parent has access */
  @import "../../public/css/overload-fonts.css";
  @import "../../public/css/dsfr.min.css";

  .l_col{

    .sep, .sep-viz {
      border-bottom:1px solid #E5E5E5;
    }

    @media (min-width: 62em) {
      .sep-viz {
        display: none;
      }
    }

    .l_box_title{
      color: #6b6b6b;
    }
    .flex{
      display: inline-flex;
      align-items: center;
    }
    .l_box_number_container {
      display: flex;
      justify-content: space-between;
      .expandable {
        height: 10px;
        font-size: calc(1% + 10vh);
      }
      .l_box_trend {
        &.down {
          .trend_ico {
            transform: rotate(90deg);
          }
        }
        &.green {
          color: #357941;
          background-color: #d9ffeb;
          .trend_ico {
            path {
              fill: #357941;
            }
          }
        }
        &.red {
          color: #d80600;
          background-color: #fff4f3;
          .trend_ico {
            path {
              fill: #d80600;
            }
          }
        }
        &.blue {
          color: #0768d5;
          background-color: #f0f7ff;
          .trend_ico {
            path {
              fill: #0768d5;
            }
          }
        }
      } 
    }
    .scale{
      .scale_container{
        height: 1.5rem;
        background-color: red;
        background: linear-gradient(90deg, rgba(255, 199, 0,1) 0%, rgba(113, 88, 69, 1) 100%);
      }
      div:last-child {
        display:flex;
        justify-content: space-between;
      }
    }

    @media (min-width: 36em) {
      .l_box_number_container {
        display: block;
        justify-content: unset;
      }
    }
  }

  .flex {
    display: flex;
    align-items: center;
    .legende_line1{
      width: 1.5rem;
      height: 0.2rem;
      background-color: #000091;
      margin-top: 0rem;
      &[data-serie="2"]{
        background-color: #007c3a;
      }
    }
    .legende_line1{
      width: 1.5rem;
      height: 0.3rem;
      background-color: #000091;
      margin-top: 0rem;
    }
    .legende_line2{
      width: 1.5rem;
      height: 0.3rem;
      background-color: #007c3a;
      margin-top: 0rem;
    }
  }


</style>
