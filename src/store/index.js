import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    departements: [],
    regions: [],
    promises: {},
    data: {},
    user: {
      selectedGeoLevel: 'France',
      selectedGeoCode: '01',
      selectedGeoLabel: 'France entière',
      geoLevelOrder: ["departements", "regions", "France"]
    },
    dataset: 'relance-tableau-de-bord'
  },
  actions: {
    getData ({ commit, state }, indicator) {
      if (state.promises[indicator]) {
        return state.promises[indicator]
      }

      const url = `https://data.economie.gouv.fr/api/v2/catalog/datasets/${state.dataset}/exports/json?limit=-1&pretty=false&where=code%20LIKE%20'${indicator}'`
      // const url = `https://data.economie.gouv.fr/api/v2/catalog/datasets/plan-de-relance-tableau-de-bord/exports/json?where=code%20LIKE%20'${indicator}'&limit=-1&pretty=false`
      const promise = fetch(url).then(res => {
        return res.json()
      }).then(result => {
        // console.log(result)
        // return result
        // Récupération des données en traitant le format fourni par data.economie
        if (!result || result.length !== 1) {
          return null
        }
        if (result[0].france) {
          result[0].france = JSON.parse(result[0].france);
        }
        if (result[0].regions) {
          result[0].regions = JSON.parse(result[0].regions);
        }
        if (result[0].departements) {
          result[0].departements = JSON.parse(result[0].departements);
        }
        if (result[0].points) {
          result[0].points = JSON.parse(result[0].points);
        }
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
      state.departements = dep
    },
    initReg (state, reg) {
      state.regions = reg
    },
    setUserChoices (state, payload) {
      state.user.selectedGeoLevel = payload.level
      state.user.selectedGeoCode = payload.code
      state.user.selectedGeoLabel = payload.label
    },
    setDataset (state, dataset) {
      state.dataset = dataset
    }
  }
})
