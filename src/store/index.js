import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// const BASE_URL = 'http://localhost:8080/json' // not needed initialize in index.html

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
      console.log("GET DATA index.js " + indicator)
      function fetchUrl(url) {
        return fetch(url)
      }

      // const url = `${state.data.url}` // /${indicator}.json`
      const url = "https://data.economie.gouv.fr/api/datasets/1.0/relance-tableau-de-bord/records/b26b6dc600d499c5b65ecf1b818520c8d5d586f7";
      const promise = fetchUrl(url);

      promise.then(res => {
        res.json()
        console.log("RESPONCEEEEEEEE")
        console.log(res.json())
        return res.json()})
      .then(data => {
        let datas = JSON.parse(data.fields.data)
        datas.json()
        console.log("TTTTTTTTTTTTTTT")
        commit('setData', { indicator: indicator, data: datas })
        return datas
      }).catch( error =>  console.log(error));
      
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
      state.data.url = "https://data.economie.gouv.fr/api/datasets/1.0/relance-tableau-de-bord" ///records/b26b6dc600d499c5b65ecf1b818520c8d5d586f7"
    }
  }
})
