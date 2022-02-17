<template>

  <div class="widget_container fr-grid-row" :class="(loading)?'loading':''" :data-display="display" :data-position="widgetPosition" :id="widgetId">
    <LeftCol v-bind="leftColProps" v-if="leftCol || leftCol === undefined"></LeftCol>
    <div class="r_col fr-col-12" :class="{'fr-col-lg-9': leftCol}">
      <h4 v-if="widgetTitle" class="chart-title">{{widgetTitle}}</h4>
      <div class="chart">
        <canvas :id="chartId"></canvas>
      </div>
    </div>
  </div>

</template>

<script>
import store from '@/store'
import Chart from 'chart.js'
import 'chartjs-plugin-labels'
import LeftCol from '@/components/LeftCol'
import { mixin, hexToRgb } from '@/utils.js'

export default {
  name: 'MultiLineChart',
  components: {
    LeftCol
  },
  mixins: [mixin],
  data () {
    return {
      indicatorData: [],
      labels: [],
      datasets: [],
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
      legendLeftMargin: 0
    }
  },
  props: {
    indicators: [],
    widgetTitle: String,
    widgetPosition: [Boolean, Number],
    withValues: Boolean,
    leftCol: {
      type: Boolean,
      default: true
    },
    lineChartConfiguration: Object
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
      return this.leftCol || this.leftCol === undefined ? 'margin-left: ' + this.legendLeftMargin + 'px' : ''
    },

  },
  methods: {

    async getData () {
      let promises = [];
      this.indicatorData = [];
      this.indicators.sort((a, b) => a.Code_indicateur.localeCompare(b.Code_indicateur))
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

      this.leftColProps.localisation = this.selectedGeoLabel

      const geolevel = this.selectedGeoLevel
      const geocode = this.selectedGeoCode

      let geoObjects = []
      self.indicatorData.sort((a, b) => a.code.localeCompare(b.code))
      this.indicatorData.forEach(_indicatorData => {
        let geoObject
        if (geolevel === 'France') {
          geoObject = _indicatorData.france[0]
        }
        else {
          geoObject = _indicatorData[geolevel].find(_geoObject => {
            return _geoObject.code_level === geocode
          })
        }

        if (geoObject) {
          geoObjects.push(geoObject)
        }

        this.units.push(_indicatorData.unite)
      })

      self.labels = []
      self.datasets = []

      let dataset = []
      geoObjects[0].values.forEach(_item => {
        self.labels.push(self.convertDateToHuman(_item.date))
        dataset.push((_item.value))
      })
      self.datasets.push(dataset)
      
      geoObjects.shift()
      geoObjects.forEach(_geoObject => {
        let otherDataset = []
        self.labels.forEach(_date => {
          const item = _geoObject.values.find(_item => {
            return self.convertDateToHuman(_item.date) === _date
          })
          if (item) {
            otherDataset.push(item.value)
          }
        })
        
        self.datasets.push(otherDataset)
      })

    },

    updateChart () {
      if (this.chart)
        this.chart.destroy()
      this.createChart()
    },

    resizeChart(e) {
      if (this.chart)
        this.chart.destroy()
      this.createChart()
    },

    createChart () {
      const self = this

      this.updateData()

      const context = document.getElementById(self.chartId).getContext('2d')

      let datasets = [];
      self.datasets.forEach((_dataset, _index) => {
        const hexaColor = store.state.colors[_index]
        const rgbColor = hexToRgb(hexaColor)
        datasets.push({
          data: _dataset,
          cubicInterpolationMode: "monotone",
          borderColor: hexaColor,
          backgroundColor: 'rgba(' + rgbColor.r + ', ' + rgbColor.g + ', ' + rgbColor.b + ', 0.05)',
          pointBackgroundColor: hexaColor,
          pointBorderColor: hexaColor,
          borderWidth: 1,
          pointRadius: 2
        })
      })

      this.chart = new Chart(context, {
        type: 'line',
        data: {
          labels: self.labels,
          datasets: datasets
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [{
              gridLines: {
                color: '#e5e5e5',
                borderDash: [3]
              },
              ticks: {
                autoSkip: true,
                maxTicksLimit: self.labels.length > 10
                  ? Math.round(self.labels.length / 2)
                  : self.labels.length,
                maxRotation: 0,
                minRotation: 0,
                callback: function (value) {
                  return value.toString().substring(3, 5) + '/' + value.toString().substring(8, 10)
                }
              }
            }],
            yAxes: [{
              gridLines: {
                color: '#e5e5e5',
                borderDash: [3]
              },
              ticks: {
                autoSkip: true,
                maxTicksLimit: 5,
                max: this.getMaxTick(self.datasets),
                callback: function (value) {
                  value = parseFloat(value)
                  if (value / 1000000000 >= 1) {
                    return Intl.NumberFormat().format(value / 1000000000) + ' Mrds'
                  } else if (value / 1000000 >= 1) {
                    return Intl.NumberFormat().format(value / 1000000) + ' M'
                  } else if (value / 1000 >= 1) {
                    return Intl.NumberFormat().format(value / 1000) + ' K'
                  }
                  return Intl.NumberFormat().format(value)
                }
              }
            }]
          },
          legend: {
            display: false
          },
          hover: {
            animationDuration: 0
          },
          animation: {
            easing: 'easeInOutBack',
            onComplete: function () {
              if (!self.withValues)
                return
              let context = this.chart.ctx;
              context.font = '12px Arial, Helvetica, sans-serif',
              context.fillStyle = "#777";
              context.textAlign = "center";
              context.textBaseline = "bottom";
              this.data.datasets.forEach(function (dataset) {
                for (var i = 0; i < dataset.data.length; i++) {
                    var model = dataset._meta[Object.keys(dataset._meta)[0]].data[i]._model;
                    var xPos = model.x;
                    var yPos = model.y - 5;

                    context.fillText(dataset.data[i], xPos, yPos);     
                }
              })
            }
          },
          tooltips: {
            displayColors: false,
            backgroundColor: '#6b6b6b',
            callbacks: {
              label: function (tooltipItems) {
                const int = self.convertFloatToHuman(tooltipItems.value)
                return int + ' ' + self.units[tooltipItems.datasetIndex]
              },
              title: function (tooltipItems) {
                return tooltipItems[0].label
              },
              labelTextColor: function () {
                return '#eeeeee'
              }
            }
          }
        }
      })
    },

    getMaxTick(datasets) {
      const maxValue = Math.max(...datasets.flat());
      const maxValueStr = Math.round(maxValue).toString();
      const maxValueLength = maxValueStr.length;
      const maxValueToAdd = Math.pow(10, maxValueLength - 1);
      const maxTick = Math.floor((maxValue + maxValueToAdd)/maxValueToAdd)*maxValueToAdd;

      return maxTick;
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
  }

}
</script>

<style scoped lang="scss">

.widget_container {
  .ml-lg {
    margin-left: 0;
  }

  @media (min-width: 62em) {
    .ml-lg {
      margin-left: 3rem;
    }
  }
  @media (max-width: 62em) {
    .chart .flex {
      margin-left: 0 !important
    }
  }

  .r_col {
    align-self: center;

    .flex {
      display: flex;

      .legende_dot {
        width: 1rem;
        height: 1rem;
        border-radius: 50%;
        background-color: var(--bg500-plain);
        display: inline-block;
        margin-top: 0.25rem;

        &[data-serie="2"] {
          background-color: #007c3a;
        }
      }
    }
  }

  .chart canvas {
    max-width: 100%;
  }

}

</style>
