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
      <h4 v-if="widgetTitle" class="chart-title">{{widgetTitle}}</h4>
      <div class="chart ml-lg">
        <canvas :id="chartId" height="260" style="margin: auto"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import Chart from 'chart.js'
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
      indicatorData: [],
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
    indicators: [],
    withLegend: Boolean,
    widgetTitle: String,
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
      let promises = [];
      this.indicators.forEach(_indicator => {
        let promise = store.dispatch('getData', _indicator.Code_indicateur).then(data => {
          this.indicatorData.push(data);
        })
        promises.push(promise);
      });

      Promise.all(promises).then(() => {
        this.loading = false
        this.createChart()
      }).catch(_ => {
        this.loading = false
      })
    },

    updateData () {

      const self = this

      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      this.units.push(self.indicatorData[0].unite)

      self.labels = []
      self.indicators.forEach(_indcator => {
        self.labels.push(_indcator.Nom_indicateur)
      })

      self.dataset = []
      self.indicatorData.forEach(_indicatorData => {
        const geoObject = this.getGeoObject(geolevel, geocode, _indicatorData)
        self.dataset.push(geoObject.values.at(-1))
      })
    },

    getGeoObject (geolevel, geocode, data) {
      let geoObject
      if (geolevel === 'France') {
        geoObject = data.france[0]
      } else {
        geoObject = data[geolevel].find(obj => {
          return obj.code_level === geocode
        })
      }

      if (typeof geoObject === 'undefined') {
        if (geolevel === 'regions') {
          geoObject = this.getGeoObject('France', '01', this.indicateur_data)
          this.leftColProps.localisation = 'France entière'
          this.geoFallback = true
          this.geoFallbackMsg = 'Affichage des résultats au niveau national, faute de données au niveau régional'
        } else {
          const depObj = store.state.departements.find(obj => {
            return obj.value === geocode
          })
          geoObject = this.getGeoObject('regions', depObj.region_value, this.indicateur_data)
          this.leftColProps.localisation = depObj.region
          this.geoFallback = true
          this.geoFallbackMsg = 'Affichage des résultats au niveau régional, faute de données au niveau départemental'
          if (typeof geoObject === 'undefined') {
            geoObject = this.getGeoObject('France', '01', this.indicateur_data)
            this.leftColProps.localisation = 'France entière'
            this.geoFallback = true
            this.geoFallbackMsg = 'Affichage des résultats au niveau national, faute de données au niveau régional ou départemental'
          }
        }
      }
      return geoObject
    },

    resizeChart () {
      if (this.chart)
        this.chart.destroy()
      this.createChart()
    },

    updateChart () {
      if (this.chart)
        this.chart.destroy()
      this.createChart()
    },

    createChart () {
      const self = this

      this.updateData()

      const context = document.getElementById(self.chartId).getContext('2d')

      let values = [];
      const total = this.dataset.map(_item => _item.value).reduce((a, b) => a + b, 0);
      this.dataset.forEach(_item => values.push((_item.value / total * 100).toFixed(1)));         

      const datasets = [{
        data: values,
        backgroundColor: store.state.colors,
        borderWidth: 2,
        borderColor: "#fff"
      }];

      const plugins = {
        labels: [
          {
            render: 'percentage',
            position: 'border',
            textShadow: true,
            shadowBlur: 5,
            shadowColor: '#000',
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            fontStyle: 'normal',
            fontColor: '#fff',
            precision: 1,
            showActualPercentages: false
          }
        ]
      }

      if (!this.withLegend) [
        plugins.labels.push(
        {
          render: 'label',
          arc: false,
          fontColor: '#000',
          fontStyle: 'normal',
          position: 'outside',
          outsidePadding: 4,
          textMargin: 8
        })
      ]

      this.options = {
        legend: {
          display: this.withLegend,
          position: 'left'
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
        responsive: true,
        maintainAspectRatio: false,
        plugins: plugins
      };

      this.chart = new Chart(context, {
        type: 'pie',
        data: {
            labels: self.labels,
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

    window.addEventListener("resize", this.resizeChart);
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
