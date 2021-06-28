<template>
  <div class="fr-container">
    <div class="fr-grid-row">

      <div class="fr-col-12 fr-col-md-4 fr-col-lg-3">
        <menu-content :panneaux="panneaux"></menu-content>
      </div>
      <div class="fr-col-12 fr-col-md-8 fr-col-lg-7 fr-col-offset-md-1 fr-mb-6w">

        <div style="position:relative; width:100%; height:0; padding-top:50%;">
          <img style="position:absolute; top:0; left:0; width:100%;" src="Logo-France-Relance.png" alt="Logo FR">
        </div>

        <p class="fr-text&#45;&#45;lead fr-mt-10w fr-mb-0 ">
          Retrouvez par mois et par département l'état d'avancement des mesures phares de France Relance.
        </p>

        <panel-list :panneaux="panneaux"></panel-list>

      </div>

    </div>
  </div>
</template>

<script>
import store from '@/store'
import MenuContent from '@/components/MenuContent'
import PanelList from '@/components/PanelList'

export default {
  name: 'PageContent',
  components: {
    MenuContent,
    PanelList
  },
  props: {
    configuration: String,
    dataUrl: String
  },
  data () {
    return {
      panneaux: []
    }
  },
  methods: {
    async getData () {
      console.log(this.dataUrl);
      store.commit('setUrl', this.dataUrl)
      fetch(this.configuration)
          .then(res => res.json())
          .then(data => {
            this.panneaux = data
          })
    }
  }
  ,
  created () {
    this.getData()
  }
}
</script>

<style scoped lang="scss">
.fr-container[data-fr-theme=dark i] {
  --bf500: #9a9aff;
  --bf500-plain: #000091;
  --w-bf500: #000091;
  --bf300-plain: #9a9aff;
  --bf200-bf300: #9a9aff;
  --bf100-g750: #2a2a2a;
  --t-plain: transparent;
  --t-w: #fff;
  --g800: #fff;
  --g700: #f0f0f0;
  --g600: #e7e7e7;
  --g500: #cecece;
  --g400: #9c9c9c;
  --g300: #6a6a6a;
  --g200: #383838;
  --g100: #2a2a2a;
  --w: #1e1e1e;
  --beige: #2a2a2a;
  --g800-plain: #1e1e1e;
  --g600-g400: #cecece;
  --g400-t: transparent;
  --g100-g800: #1e1e1e;
  --w-g750: #2a2a2a;
  --focus: #5398ff;
  --info: #2b8bf7;
  --success: #00eb5e;
  --error: #f33;
  --rm300: #383838;
  --rm500: #f7bfc3;
  --scroll-shadow: #1e1e1e;
  --overlay: hsla(0, 0%, 80.8%, 0.32)
}

.fr-container {
  --bf500: #000000;
  --bf500-plain: #000091;
  --w-bf500: #fff;
  --bf300-plain: #9a9aff;
  --bf200-bf300: #ececff;
  --bf100-g750: #f5f5ff;
  --t-plain: transparent;
  --t-w: transparent;
  --g800: #1e1e1e;
  --g700: #383838;
  --g600: #6a6a6a;
  --g500: #9c9c9c;
  --g400: #cecece;
  --g300: #e7e7e7;
  --g200: #f0f0f0;
  --g100: #f8f8f8;
  --w: #fff;
  --beige: #f9f8f6;
  --g800-plain: #1e1e1e;
  --g600-g400: #6a6a6a;
  --g400-t: #cecece;
  --g100-g800: #f8f8f8;
  --w-g750: #fff;
  --focus: #2a7ffe;
  --info: #0762c8;
  --success: #008941;
  --error: #e10600;
  --rm300: #f7bfc3;
  --rm500: #e1000f;
  --scroll-shadow: rgba(30, 30, 30, 0.16);
  --overlay: hsla(0, 0%, 61.2%, 0.32)
}

.fr-container:not([data-fr-theme=dark i]) [class*="--scheme-light-"],
.fr-container:not([data-fr-theme=dark i]) [class*=fr-scheme-light] {
  --bf500: #000091;
  --bf500-plain: #000091;
  --w-bf500: #fff;
  --bf300-plain: #9a9aff;
  --bf200-bf300: #ececff;
  --bf100-g750: #f5f5ff;
  --t-plain: transparent;
  --t-w: transparent;
  --g800: #1e1e1e;
  --g700: #383838;
  --g600: #6a6a6a;
  --g500: #9c9c9c;
  --g400: #cecece;
  --g300: #e7e7e7;
  --g200: #f0f0f0;
  --g100: #f8f8f8;
  --w: #fff;
  --beige: #f9f8f6;
  --g800-plain: #1e1e1e;
  --g600-g400: #6a6a6a;
  --g400-t: #cecece;
  --g100-g800: #f8f8f8;
  --w-g750: #fff;
  --focus: #2a7ffe;
  --info: #0762c8;
  --success: #008941;
  --error: #e10600;
  --rm300: #f7bfc3;
  --rm500: #e1000f;
  --scroll-shadow: rgba(30, 30, 30, 0.16);
  --overlay: hsla(0, 0%, 61.2%, 0.32)
}

.fr-container:not([data-fr-theme=dark i]) [class*="--scheme-dark-"],
.fr-container:not([data-fr-theme=dark i]) [class*=fr-scheme-dark] {
  --bf500: #9a9aff;
  --w-bf500: #000091;
  --bf200-bf300: #9a9aff;
  --bf100-g750: #2a2a2a;
  --t-w: #fff;
  --g800: #fff;
  --g700: #f0f0f0;
  --g600: #e7e7e7;
  --g500: #cecece;
  --g400: #9c9c9c;
  --g300: #6a6a6a;
  --g200: #383838;
  --g100: #2a2a2a;
  --w: #1e1e1e;
  --beige: #2a2a2a;
  --g600-g400: #cecece;
  --g400-t: transparent;
  --g100-g800: #1e1e1e;
  --w-g750: #2a2a2a;
  --focus: #5398ff;
  --info: #2b8bf7;
  --success: #00eb5e;
  --error: #f33;
  --rm300: #383838;
  --rm500: #f7bfc3;
  --scroll-shadow: #1e1e1e;
  --overlay: hsla(0, 0%, 80.8%, 0.32)
}
</style>
