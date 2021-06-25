import Vue from 'vue'

import store from './store'
import { getData } from './import.js'

// import Map from './components/Map'
import DataBox from './components/DataBox'
import LineChart from './components/LineChart'
import MultiLineChart from './components/MultiLineChart'
import BarChart from './components/BarChart'
import MapChart from './components/MapChart'
import GeoList from './components/GeoList'
import LineMapPanel from './components/LineMapPanel'
import PanelList from './components/PanelList'
import PageContent from './components/PageContent'
import MenuContent from './components/MenuContent'

import vueCustomElement from 'vue-custom-element'
Vue.use(getData(store))

Vue.config.productionTip = false

Vue.use(vueCustomElement)

// Vue.customElement('da-map', Map)
Vue.customElement('data-box', DataBox)
Vue.customElement('line-chart', LineChart)
Vue.customElement('multiline-chart', MultiLineChart)
Vue.customElement('bar-chart', BarChart)
Vue.customElement('map-chart', MapChart)
Vue.customElement('geo-list', GeoList)
Vue.customElement('line-map-panel', LineMapPanel)
Vue.customElement('panel-list', PanelList)
Vue.customElement('page-content', PageContent)
Vue.customElement('menu-content', MenuContent)
