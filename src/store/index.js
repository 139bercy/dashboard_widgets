import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const BASE_URL = 'http://localhost:8080/json'

export default new Vuex.Store({
  state: {
    dep: [],
    reg: [],
    promises: {},
    data: {},
    user: {
      selectedGeoLevel: 'France',
      selectedGeoCode: '01',
      selectedGeoLabel: 'France entière'
    }
  },
  actions: {
    getData ({ commit, state }, indicator) {
      if (state.promises[indicator]) {
        return state.promises[indicator]
      }
      const url = `${state.data.url || BASE_URL}/${indicator}.json`
      const promise = fetch(url).then(res => {
        return res.json()
      }).then(data => {
        commit('setData', { indicator: indicator, data: data })
        return data
      })
      commit('setPromise', { indicator: indicator, promise: promise })
      return promise
    }
  },
  mutations: {
    setPromise (state, payload) {
      state.promises[payload.indicator] = payload.promise
    },
    setData (state, payload) {
      state.data[payload.indicator] = payload.data
    },
    initDep (state, dep) {
      state.dep = dep
    },
    initReg (state, reg) {
      state.reg = reg
    },
    setUserChoices (state, payload) {
      state.user.selectedGeoLevel = payload.level
      state.user.selectedGeoCode = payload.code
      state.user.selectedGeoLabel = payload.label
    },
    setUrl (state, url) {
      console.log("inside store")
      state.data.url = url
    }
  }
})
