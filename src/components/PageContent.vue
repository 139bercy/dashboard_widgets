<template>
  <div class="fr-container">
    <div class="fr-grid-row">

      <div class="fr-col-12 fr-col-md-4 fr-col-lg-3">
        <menu-content configuration="dashboard-configuration.json"></menu-content>
      </div>
      <div class="fr-col-12 fr-col-md-8 fr-col-lg-7 fr-col-offset-md-1 fr-mb-6w">

        <div style="position:relative; width:100%; height:0; padding-top:50%;">
          <img style="position:absolute; top:0; left:0; width:100%;" src="Logo-France-Relance.png" alt="Logo FR">
        </div>

        <p class="fr-text&#45;&#45;lead fr-mt-10w fr-mb-0 ">
          Retrouvez par mois et par département l'état d'avancement des mesures phares de France Relance.
        </p>

        <panel-list configuration="dashboard-configuration.json"></panel-list>

      </div>

    </div>
  </div>
</template>
<script>
// import '../../js/core.nomodule'
// import '../../js/accordions.nomodule'

import MenuContent from '@/components/MenuContent'

export default {
  name: 'PageContent',
  components: {
    MenuContent
  }
}
</script>
