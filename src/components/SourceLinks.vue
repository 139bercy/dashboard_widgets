<template>
  <div>
    <a target="_parent" class="fr-link fr-col-sm-12 fr-col-md-6" href="https://github.com/139bercy/dashboard_widgets/">Code source de la page</a>
    <a target="_parent" class="fr-link fr-col-sm-12 fr-col-md-6" v-if="sourceLinks !== undefined" :href="sourceLinks">Code source du traitement des données</a>
  </div>
</template>


<script>
export default {
  name: 'SourceLinks',
  props: {
    sourceLinks: String
  }
}
</script>

<style scoped lang="scss">
  .fr-link {
    // color: var(--g500) !important;
    font-size: small !important;
  }
</style>
