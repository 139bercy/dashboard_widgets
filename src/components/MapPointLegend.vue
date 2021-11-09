<template>
  <div class="fr-grid-row">
    <div class="l_col fr-col-11" data-box="number" v-if="indicateurs && indicateurs.length > 0 && !loading">
      <div class="indicateur_info">
        <div class="l_box_number_container" v-for="indicateur,index in indicateurs" :key="indicateur">
          <div class="fr-checkbox-group">
              <input
                type="checkbox"
                :id="'checkbox-' + indicateur"
                :name="indicateur"
                :checked="indicateurs.findIndex(i => i == indicateur) < 4"
                @change="updateSelected" />
              <label
                class="fr-label" :class="'color-' + (index + 1)"
                :for="'checkbox-' + indicateur">
                {{ indicateur }}  {{ nbPoints[indicateur] ? '(' + nbPoints[indicateur] + ')' : '' }}
              </label>
          </div>
        </div>
        <p></p>
          <div class="fr-text--sm fr-text--bold fr-mt-0 fr-mb-1w">
            <span :class="{'position-absolute' : $screen.breakpoint !== 'lg'}" v-if="logo">
              <img :src="logo" :alt="altLogo" width="60px"/>
            </span>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

import store from '@/store'
import { mixin } from '@/utils.js'
export default {
  name: 'MapPointLegend',
  mixins: [mixin],
  data () {
    return {
      nbPoints: [],
      loading: true
    }
  },
  props: {
    selecteur: String,
    legende: String,
    indicateurs: Array,
    logo: String,
    altLogo: String
  },
  methods: {
    updateSelected(event) {
      // console.log(event)
      const indicateurKey = event.target.name
      const indicateurStatus = event.target.checked
      // console.log(indicateurKey, indicateurStatus)
      this.$emit('indicateurSelected', indicateurKey, indicateurStatus)
    },
    async getData (indicateur) {
      // console.log(indicateur)
      const data = await store.dispatch('getData', indicateur)
      if (data && data.points) {
        // console.log(indicateur, data.points.length)
        this.nbPoints[indicateur] = data.points.length
      }
    },
  },

  async created () {
    await Promise.all(this.indicateurs.map(async indicateur => {
      return await this.getData(indicateur)
    }))
    this.loading = false
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
      .fr-label {
        font-size: xx-small;
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


  .fr-checkbox-group {
    .fr-label {
      &.color-0 {
        color: var(--map-point-color-0);
        &:checked {
          &label::before {
            background-color: var(--map-point-color-0);
          }
        }
      }
      &.color-1 {
        color: var(--map-point-color-1);
        &::before {
          border: 1px solid var(--map-point-color-1);
          background-color: var(--map-point-color-1) !important;
        }
      }
      &.color-2 {
        color: var(--map-point-color-2);
        &::before {
          border: 1px solid var(--map-point-color-2);
          background-color: var(--map-point-color-2) !important;
        }
      }
      &.color-3 {
        color: var(--map-point-color-3);
        &::before {
          border: 1px solid var(--map-point-color-3);
          background-color: var(--map-point-color-3) !important;
        }
      }
      &.color-4 {
        color: var(--map-point-color-4);
        &::before {
          border: 1px solid var(--map-point-color-4);
          background-color: var(--map-point-color-4) !important;
        }
      }
      &.color-5{
        color: var(--map-point-color-5);
        &::before {
          border: 1px solid var(--map-point-color-5);
          background-color: var(--map-point-color-5) !important;
        }
      }
      &.color-6{
        color: var(--map-point-color-6);
        &::before {
          border: 1px solid var(--map-point-color-6);
          background-color: var(--map-point-color-6) !important;
        }
      }
      &.color-7{
        color: var(--map-point-color-7);
        &::before {
          border: 1px solid var(--map-point-color-7);
          background-color: var(--map-point-color-7) !important;
        }
      }
      &.color-8{
        color: var(--map-point-color-8);
        &::before {
          border: 1px solid var(--map-point-color-8);
          background-color: var(--map-point-color-8) !important;
        }
      }
      &.color-9{
        color: var(--map-point-color-9);
        &::before {
          border: 1px solid var(--map-point-color-9);
          background-color: var(--map-point-color-9) !important;
        }
      }
      &.color-10{
        color: var(--map-point-color-10);
        &::before {
          border: 1px solid var(--map-point-color-10);
          background-color: var(--map-point-color-10) !important;
        }
      }
      &.color-11{
        color: var(--map-point-color-11);
        &::before {
          border: 1px solid var(--map-point-color-11);
          background-color: var(--map-point-color-11) !important;
        }
      }
      &.color-12{
        color: var(--map-point-color-12);
        &::before {
          border: 1px solid var(--map-point-color-12);
          background-color: var(--map-point-color-12) !important;
        }
      }
      &.color-13{
        color: var(--map-point-color-13);
        &::before {
          border: 1px solid var(--map-point-color-13);
          background-color: var(--map-point-color-13) !important;
        }
      }
      &.color-14{
        color: var(--map-point-color-14);
        &::before {
          border: 1px solid var(--map-point-color-14);
          background-color: var(--map-point-color-14) !important;
        }
      }
      &.color-15{
        color: var(--map-point-color-15);
        &::before {
          border: 1px solid var(--map-point-color-15);
          background-color: var(--map-point-color-15) !important;
        }
      }
      &.color-16{
        color: var(--map-point-color-16);
        &::before {
          border: 1px solid var(--map-point-color-16);
          background-color: var(--map-point-color-16) !important;
        }
      }
      &.color-17{
        color: var(--map-point-color-17);
        &::before {
          border: 1px solid var(--map-point-color-17);
          background-color: var(--map-point-color-17) !important;
        }
      }
      &.color-18{
        color: var(--map-point-color-18);
        &::before {
          border: 1px solid var(--map-point-color-18);
          background-color: var(--map-point-color-18) !important;
        }
      }
      &.color-19{
        color: var(--map-point-color-19);
        &::before {
          border: 1px solid var(--map-point-color-19);
          background-color: var(--map-point-color-19) !important;
        }
      }
      &.color-20{
        color: var(--map-point-color-20);
        &::before {
          border: 1px solid var(--map-point-color-20);
          background-color: var(--map-point-color-20) !important;
        }
      }
    }
  }

</style>
