<template>

  <div class="widget_container fr-grid-row fr-warning" :class="(loading)?'loading':''" :data-display="display" :data-position="widgetPosition" :id="widgetId">
     <div :id="chartId" class="scheme-border">
        <span aria-hidden="true" class="fr-fi-information-line"></span>
        <p class="fr-text--sm fr-mb-0 fr-mt-2v"></p>
      </div>
  </div>
</template>

<script>
import store from '@/store'
import { mixin } from '@/utils.js'
export default {
  name: 'Table',
  mixins: [mixin],
  components: {
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
    widgetTitle: String,
    widgetContent: String
  },

  created () {
    this.chartId = 'myChart' + Math.floor(Math.random() * (1000))
    this.widgetId = 'widget' + Math.floor(Math.random() * (1000))
  },

  updated () {
    const info = document.getElementById(this.chartId)
    if (info) {
      const infoTitle = info.getElementsByTagName('span')[0]
      infoTitle.innerHTML = ''
      const infoTitleText = document.createTextNode(this.widgetTitle)

      const infoContent = info.getElementsByTagName('p')[0]
      infoContent.innerHTML = ''
      const infoContentText = document.createTextNode(this.widgetContent)

      infoTitle.appendChild(infoTitleText)
      infoContent.appendChild(infoContentText)
    }
  },

  mounted () {
    document.getElementById(this.widgetId).offsetWidth > 486 ? this.display = 'big' : this.display = 'small'
    // 502px to break
  }

}
</script>

<style scoped lang="scss">

  .widget_container {
    background: #f6f6ff;

    .fr-fi-information-line::before {
      margin-right: 5px;
      color: #000091;
    }

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
