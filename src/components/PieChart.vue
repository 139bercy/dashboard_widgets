<template>

  <div class="widget_container fr-grid-row" :class="(loading)?'loading':''" :data-display="display" :data-position="widgetPosition" :id="widgetId">
      <div class="fr-warning" v-if="geoFallback">
        <div class="scheme-border">
            <span class="fr-fi-information-fill fr-px-1w fr-py-3v" aria-hidden="true"></span>
        </div>
        <p class="fr-text--sm fr-mb-0 fr-p-3v">{{geoFallbackMsg}}
        </p>
    </div>
    <LeftCol v-bind="leftColProps" v-if="leftCol"></LeftCol>
    <div class="r_col fr-col-12" :class="{'fr-col-lg-9': leftCol}">
      <div class="chart ml-lg">
        <canvas :id="chartId" height="260" style="margin: auto"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import Chart from 'chart.js'
import moment from 'moment'
import 'chartjs-plugin-colorschemes'
import 'chartjs-plugin-labels'
import LeftCol from '@/components/LeftCol'
import { mixin } from '@/utils.js'
export default {
  name: 'PieChart',
  mixins: [mixin],
  components: {
    LeftCol
  },
  data () {
    return {
      indicateur_data: undefined,
      labels: [],
      dataset: [],
      widgetId: '',
      chartId: '',
      display: '',
      leftColProps: {
        localisation: '',
        currentValues: [],
        currentDate: '',
        names: [],
        evolcodes: [],
        evolvalues: [],
        isMap: false,
        date: ''
      },
      units: [],
      chart: undefined,
      loading: true,
      legendLeftMargin: 0,
      geoFallback: false,
      geoFallbackMsg: ''
    }
  },
  props: {
    indicateur: String,
    widgetPosition: [Boolean, Number],
    leftCol: {
      type: Boolean,
      default: true
    },
    barChartConfiguration: Object
  },
  computed: {
    selectedGeoLevel () {
      return store.state.user.selectedGeoLevel
    },
    selectedGeoCode () {
      return store.state.user.selectedGeoCode
    },
    selectedGeoLabel () {
      return store.state.user.selectedGeoLabel
    },
    style () {
      return 'margin-left: ' + this.legendLeftMargin + 'px'
    },

  },
  methods: {

    async getData () {
      store.dispatch('getData', this.indicateur).then(data => {
        this.indicateur_data = data
        this.loading = false
        this.createChart()
      })
    },

    updateData () {
      const self = this

      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      this.leftColProps.localisation = this.selectedGeoLabel

      let geoObject

      geoObject = this.getGeoObject(geolevel, geocode)
      if (!geoObject) return
      this.leftColProps.date = this.convertDateToHuman(geoObject.last_date)

      this.leftColProps.names.length = 0
      this.units.length = 0
      this.leftColProps.currentValues.length = 0
      this.leftColProps.evolcodes.length = 0
      this.leftColProps.evolvalues.length = 0

      this.leftColProps.names.push(this.indicateur_data.nom)
      this.units.push(this.indicateur_data.unite)
      this.leftColProps.currentValues.push(geoObject.last_value)
      this.leftColProps.currentDate = this.convertDateToHuman(geoObject.last_date)
      this.leftColProps.evolcodes.push(geoObject.evol_color)
      this.leftColProps.evolvalues.push(geoObject.evol_percentage)

      this.labels.length = 0
      this.dataset.length = 0

      geoObject.values.forEach(function (d) {
        self.labels.push(self.convertDateToHuman(d.date))
        self.dataset.push((d.value))
      })
    },

    getGeoObject (geolevel, geocode) {
      let geoObject
      if (geolevel === 'France') {
        geoObject = this.indicateur_data.france[0]
      } else {
        geoObject = this.indicateur_data[geolevel].find(obj => {
          return obj.code_level === geocode
        })
      }

      if (typeof geoObject === 'undefined') {
        if (geolevel === 'regions') {
          geoObject = this.getGeoObject('France', '01')
          this.leftColProps.localisation = 'France entière'
          this.geoFallback = true
          this.geoFallbackMsg = 'Affichage des résultats au niveau national, faute de données au niveau régional'
        } else {
          const depObj = store.state.departements.find(obj => {
            return obj.value === geocode
          })
          geoObject = this.getGeoObject('regions', depObj.region_value)
          this.leftColProps.localisation = depObj.region
          this.geoFallback = true
          this.geoFallbackMsg = 'Affichage des résultats au niveau régional, faute de données au niveau départemental'
          if (typeof geoObject === 'undefined') {
            geoObject = this.getGeoObject('France', '01')
            this.leftColProps.localisation = 'France entière'
            this.geoFallback = true
            this.geoFallbackMsg = 'Affichage des résultats au niveau national, faute de données au niveau régional ou départemental'
          }
        }
      }
      return geoObject
    },

    updateChart () {
      this.updateData()
      this.chart.destroy()
      this.createChart()
    },

    createChart () {
      const self = this

      this.updateData()

      const context = document.getElementById(self.chartId).getContext('2d')

      let labels = [];
      this.labels.forEach(_label => labels.push(moment(_label, "DD/MM/YYYY").format('YYYY')));

      let values = [];
      const total = this.dataset.reduce((a, b) => a + b, 0);
      this.dataset.forEach(_value => values.push((_value / total * 100).toFixed(1)));

      const datasets = [{
        data: values,
        borderWidth: 2,
        borderColor: "#fff"
      }];

      this.options = {
        legend: {
          display: false
        },
        tooltips: {
          displayColors: true,
          backgroundColor: '#6b6b6b',
          callbacks: {
            title: function(tooltipItem, data) {
              return data['labels'][tooltipItem[0]['index']];
            },
            label: function(tooltipItem, data) {
              return ' ' + data['datasets'][0]['data'][tooltipItem['index']] + '% ' + self.units[0];
            },
            afterLabel: function(tooltipItem, data) {
            }
          }
        },
        responsive: false,
        maintainAspectRatio: false,
        plugins: {
          labels: [
            {
              render: 'label',
              arc: false,
              fontColor: '#000',
              fontStyle: 'normal',
              position: 'outside',
              outsidePadding: 4,
              textMargin: 8
            },
            {
              render: 'percentage',
              position: 'border',
              textShadow: true,
              fontStyle: 'normal',
              fontColor: '#fff',
              precision: 1,
              showActualPercentages: false
            }
          ],
          colorschemes: {
            scheme: 'brewer.SetOne9'
          }
        }
      };

      this.chart = new Chart(context, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: this.options
      });
    }

  },

  watch: {
    selectedGeoCode: function () {
      this.updateChart()
    },
    selectedGeoLevel: function () {
      this.updateChart()
    }
  },

  created () {
    this.chartId = 'myChart' + Math.floor(Math.random() * (1000))
    this.widgetId = 'widget' + Math.floor(Math.random() * (1000))
    this.getData()
  },

  mounted () {
    document.getElementById(this.widgetId).offsetWidth > 486 ? this.display = 'big' : this.display = 'small'
    // 502px to break
  }

}
</script>

<style scoped lang="scss">

  .widget_container{
    .fr-warning {
      display: flex;
      min-width: 100%;
      margin: 0 0 0.75rem;
      background-color: var(--w);
      width: 100%;
      .scheme-border {
          min-width: 2.5rem;
          background-color: #0768d5;
          display: flex;
          justify-content: center;
      }
      span {
          display: block;
          color: var(--w);
      }
      p {
          border: solid 1px #0768d5;
          width: 100%;

      }
    }
    @media (max-width: 62em) {
      .chart .flex {
        margin-left:0!important
      }
    }
    .r_col {
      align-self:center;
      .flex{
        display: flex;
        .legende_dot{
          width: 1rem;
          height: 1rem;
          min-width: 1rem;
          border-radius: 50%;
          background-color: var(--bg500-plain);
          display: inline-block;
          margin-top: 0.25rem;
        }
      }
    }

    .chart canvas {
      max-width:100%;
    }

  }

</style>
