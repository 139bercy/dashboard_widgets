<template>

  <div class="data_box" :data-display="display" :id="widgetId" v-bind:class="{'green':isGreen,'red':isRed, 'loading':loading}">

    <p class="l_box_title fr-text--xs fr-mb-0">Mise à jour : {{currentDate}}</p>
    <p class="fr-text--sm fr-text--bold fr-my-1w">{{indicatorName}}</p>
    <p class="fr-text--sm fr-mb-1w" v-if="(!testIfNaN(evolvalue))">{{convertFloatToHumanDataBox(currentValue)}} {{indicatorUnit}}</p>
  </div>

</template>

<script>
import store from '@/store'
import { mixin } from '@/utils.js'

export default {
  name: 'DataBox',
  mixins: [mixin],
  data () {
    return {
      display: '',
      indicateur_data: undefined,
      currentValue: '',
      currentDate: '',
      name: '',
      unit: '',
      evolcode: '',
      evolvalue: '',
      evolunit: '',
      isDown: false,
      isGreen: false,
      isRed: false,
      isBlue: false,
      showEvolIcon: true,
      loading: true
    }
  },
  props: {
    indicator: String,
    indicatorName: String,
    indicatorUnit: String
  },
  computed: {
    selectedGeoLevel () {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode () {
      return store.state.user.selectedGeoCode
    }
  },
  methods: {

    testEvolStyle () {
      this.showEvolIcon = false
      if (this.evolcode === 'green') {
        this.isGreen = true
        this.isRed = false
        this.isBlue = false
        this.evolvalue > 0 ? this.isDown = false : this.isDown = true
      } else if (this.evolcode === 'red') {
        this.isGreen = false
        this.isRed = true
        this.isBlue = false
        this.evolvalue > 0 ? this.isDown = false : this.isDown = true
      } else if (this.evolcode === 'None') {
        this.isGreen = false
        this.isRed = false
        this.isBlue = false
        this.isDown = false
        this.showEvolIcon = false
      } else {
        this.isGreen = false
        this.isRed = false
        this.isBlue = true
        this.isDown = false
      }
    },

    updateData () {
      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      let geoObject

      if (geolevel === 'France') {
        geoObject = this.indicateur_data.france[0]
        this.localisation = 'France entière'
      } else {
        this.localisation = geocode

        geoObject = this.indicateur_data[geolevel].find(obj => {
          return obj.code_level === geocode
        })
      }

      this.evolunit = this.indicateur_data.evol_unite
      this.currentValue = this.indicateur_data.france[0].last_value
      this.currentValue = geoObject.last_value
      this.currentDate = this.convertDateToHuman(geoObject.last_date)
      this.evolcode = geoObject.evol_color
      this.evolvalue = geoObject.evol_percentage
    },

    async getData () {
      store.dispatch('getData', this.indicator).then(data => {
        this.indicateur_data = data
        this.loading = false
        this.updateData()
      })
    }

  },

  watch: {
    selectedGeoCode: function () {
      this.updateData()
    },
    selectedGeoLevel: function () {
      this.updateData()
    },
    evolcode: function () {
      this.testEvolStyle()
    },
    evolvalue: function () {
      this.testEvolStyle()
    }
  },

  created () {
    this.widgetId = 'widget' + Math.floor(Math.random() * (1000))
    this.getData()
  }

}
</script>

<!-- TODO #d80600 valeur réelle pour &red, le temps de corriger les données sur data.economie -->

<style scoped lang="scss">

  .data_box{
    background-color: white;
    box-shadow: 0 1px 8px 1px rgba(22, 22, 22, 0.04), 0 2px 8px -4px rgba(22, 22, 22, 0.04);
    height: 100%;

    .l_box_title{
      color: #6b6b6b;
    }

    &.green{
      border-bottom: 5px solid #007c3a;
    }
    &.red{
      border-bottom: 5px solid #b4b4f0;
    }
    .evol_box{
      display: inline-flex;
      align-items: center;

      &.down{
        .trend_ico{
          transform: rotate(90deg);
        }
      }
      &.green{
        color:#007c3a;
        background-color: #d9ffeb;
        .trend_ico{
          path{
            fill:#357941;
          }
        }
      }
      &.red{
        color:#d80600;
        background-color: #fff4f3;
        .trend_ico{
          path{
            fill:#d80600;
          }
        }
      }
      &.blue{
        color:#0768d5;
        background-color: #f0f7ff;
        .trend_ico{
          path{
            fill:#0768d5;
          }
        }
      }
    }
  }

</style>
