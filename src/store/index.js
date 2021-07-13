import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


function encodeIndicatorName(indicator) {
  return encodeURIComponent('%' + indicator.substring(indicator.length -4, indicator.length) + '%')
}

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

      // console.log(indicator)
      // console.log(encodeURIComponent(indicator))
      // const url = `${state.data.url || BASE_URL}/${indicator}.json`
      const url = `https://data.economie.gouv.fr/api/v2/catalog/datasets/relance-tableau-de-bord/exports/json?where=nom%20LIKE%20'${encodeIndicatorName(indicator)}'`
      const promise = fetch(url).then(res => {
        return res.json()
      }).then(result => {
        // Récupération des données en traitant le format fourni par data.economie
        if (!result || result.length !== 1) {
          return null
        }
        result[0].france = JSON.parse(result[0].france);
        result[0].regions = JSON.parse(result[0].regions);
        result[0].departements = JSON.parse(result[0].departements);
        console.log(result[0])
        return result[0]
      }).then(data => {
        commit('setData', { indicator: indicator, data: data })
        return data
      }).catch(response => {
        console.log(response)
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
    }
  }
})
