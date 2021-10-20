<template>

  <div class="fr-grid-row">
    <div class="l_col fr-col-11" data-box="number" v-if="indicateurs && indicateurs.length > 0">
      <div class="indicateur_info">
        <p class="fr-text--sm fr-text--bold fr-mt-0 fr-mb-1w">
          {{ selecteur }}
        </p>
        <div class="l_box_number_container">
          <select class="fr-select fr-text--sm fr-mb-0 fr-py-1v" name="select" @change="updateSelected">
            <option v-for="v in indicateurs" :value="v" :key="v">{{ v }}</option>
          </select>
        </div>
      </div>
    </div>
    <div data-box="number" v-if="nbPoints">
      <div class="indicateur_info">
        <p class="fr-text--sm fr-text--bold fr-mt-0 fr-mb-1w">
          {{ legende }}
        </p>
        <div class="l_box_number_container">
          <p class="fr-text--lg fr-text--bold fr-mb-1v">
            {{ convertFloatToHuman(nbPoints) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { mixin } from '@/utils.js'
export default {
  name: 'MapPointLegend',
  mixins: [mixin],
  data () {
    return {
      indicateur: undefined,
      nbPoints: undefined
    }
  },
  props: {
    selecteur: String,
    legende: String,
    indicateurs: Array
  },
  methods: {
    updateSelected(event) {
      this.indicateur = event.target.value
      this.$emit('indicateurSelected', event.target.value)
      this.getData()
    },
    async getData () {
      // store.dispatch('getData', this.indicateur).then(data => {
        // this.nbPoints = indicateur_data.points.length
      // })
      // TODO
      await fetch("impact.data.json")
        .then(res => res.json())
        .then(data => {
          // this.loading = false
          const indicateur_data = data.find(d => d.code == this.indicateur)
          if (indicateur_data) {
            this.nbPoints = JSON.parse(indicateur_data.points).length
          }
        })

    },
  },

  created () {
    this.indicateur = this.indicateurs[0]
    this.getData()
  }

}
</script>

<style scoped lang="scss">
  @import "../../css/overload-fonts.css";
  .l_col{
    .flex{
      display: inline-flex;
      align-items: center;
    }
    .l_box_number_container {
      display: flex;
      justify-content: space-between;
    }
    .scale{
      .scale_container{
        height: 1.5rem;
        background-color: red;
        background: linear-gradient(90deg, rgba(255, 199, 0,1) 0%, rgba(113, 88, 69, 1) 100%);
      }
      div:last-child {
        display:flex;
        justify-content: space-between;
      }
    }

    @media (min-width: 36em) {
      .l_box_number_container {
        display: block;
        justify-content: unset;
      }
    }
  }

  .position-absolute {
    position: absolute
  }

</style>
