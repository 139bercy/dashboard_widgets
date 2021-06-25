<template>
  <div>
    <div v-for="(panneau, index) in panneaux" :key="index">
      <panel v-bind:index="index + ''" v-bind="panneau"></panel>
    </div>
  </div>
</template>
<script>
import Panel from './Panel.vue'

export default {
  name: 'PanelList',
  components: {
    Panel
  },
  props: {
    configuration: String
  },
  data () {
    return {
      panneaux: {}
    }
  },
  mounted () {
    fetch(this.configuration)
      .then(res => res.json())
      .then(data => {
        this.panneaux = data
      })
  }
}
</script>
