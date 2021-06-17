import Vue from 'vue'

import store from './store'
import { getData } from './import.js'
Vue.use(getData(store))

//import Map from './components/Map'
import DataBox from './components/DataBox'
import LineChart from './components/LineChart'
import MultiLineChart from './components/MultiLineChart'
import BarChart from './components/BarChart'
import MapChart from './components/MapChart'
import GeoList from './components/GeoList'
import TopRow from './components/TopRow'
import Complete_panel from './components/Complete_panel'

Vue.config.productionTip = false

import vueCustomElement from 'vue-custom-element'

Vue.use(vueCustomElement)

//Vue.customElement('da-map', Map)
Vue.customElement('data-box', DataBox)
Vue.customElement('line-chart', LineChart)
Vue.customElement('multiline-chart', MultiLineChart)
Vue.customElement('bar-chart', BarChart)
Vue.customElement('map-chart', MapChart)
Vue.customElement('geo-list', GeoList)
Vue.customElement('top-row', TopRow)
Vue.customElement('complete-panel', Complete_panel)