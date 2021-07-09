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
      /*
      if (state.promises[indicator]) {
        return state.promises[indicator]
      }
      const url = `${state.data.url}` // /${indicator}.json`
      const promise = fetch(url).then(res => {
        console.debug(res.json())
        return res.json()
      }).then(data => {
        console.debug(data)
        commit('setData', { indicator: indicator, data: data })
        return data
      })
      commit('setPromise', { indicator: indicator, promise: promise })
      return promise
      */
      function getUsers(url) {
        return fetch(url)
      }
      
      const test = getUsers(`https://data.economie.gouv.fr/api/datasets/1.0/relance-tableau-de-bord/records/b26b6dc600d499c5b65ecf1b818520c8d5d586f7`);
      test.then(response => response.json())
     .then(data => {
          console.log(data);
          console.log(JSON.parse(data.fields.data))
     })
     .catch(error => {
          // handle error
     });

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
