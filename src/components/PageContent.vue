<template style="margin: 0;">
  <div class="page-content fr-container">
    <div class="fr-grid-row">

      <div class="fr-col-12 fr-col-md-4 fr-col-lg-3" v-if="displaySearch">
        <menu-content :panneaux="panneaux"></menu-content>
      </div>
      <div class="fr-col-12 fr-col-md-7 fr-col-lg-7 fr-ml-md-6w fr-mb-6w">
        <div v-html="descriptionContent"></div>

        <div v-for="(panneau, index) in panneaux" :key="index">
          <panel v-bind:index="index + ''" v-bind="panneau"></panel>
        </div>

        <SourceLinks class="fr-col-12 fr-col-md-12 fr-col-lg-12 fr-mt-3w" :source-links="sourceLinks"/>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store'
import MenuContent from '@/components/MenuContent'
import Panel from '@/components/Panel'
import SourceLinks from '@/components/SourceLinks'

export default {
  name: 'PageContent',
  components: {
    MenuContent,
    Panel,
    SourceLinks
  },
  props: {
    configuration: String,
    dataset: String,
    displaySearch: Boolean,
    description: String,
    sourceLinks: String
  },
  data() {
    return {
      panneaux: [],
      descriptionContent: ''
    }
  },
  methods: {
    async getData() {
      store.commit('setDataset', this.dataset)
      await fetch(this.configuration)
          .then(res => res.json())
          .then(data => {
            this.panneaux = data
          })
      if (this.description!== undefined && this.description !== '') {
        const self = this
        await fetch(this.description)
          .then(res => res.text())
          // hack pour intégrer le nombre d'indicateurs dans la description
          .then(data => this.descriptionContent = data.replace("{{ panneaux.length }}", this.panneaux.length))
      }
    }
  }
  ,
  created() {
    this.getData()
  }
}
</script>

<style scoped lang="css">

</style>

<style lang="scss">

@import "../../css/hack.dsfr.min.scss";
@import "../../css/overload-fonts.css";
.page-content {

  /* overload fonts path, to delete when parent has access */
  @include dsfr;

  --bf500: #009100;
  --bf500-plain: #039103;
  --w-bf500: #fff;
  --bf300-plain: #9a9aff;
  --bf200-bf300: #ececff;
  --bf100-g750: #f7fff5;
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
  --overlay: hsla(0, 0%, 61.2%, 0.32);
  --boxshadow: #29b829;
  --boxcountour: #17b9084b;
}

.page-content[data-fr-theme=dark i] {
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

.page-content:not([data-fr-theme=dark i]) [class*="--scheme-light-"],
.page-content:not([data-fr-theme=dark i]) [class*=fr-scheme-light] {
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

.page-content:not([data-fr-theme=dark i]) [class*="--scheme-dark-"],
.page-content:not([data-fr-theme=dark i]) [class*=fr-scheme-dark] {
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

.page-content:not([data-fr-theme="dark" i]) .fr-tabs__tab:not([aria-selected="true"]) {
  --color-hover: rgba(187, 255, 182, 0.5);
  --color-active: rgba(109, 168, 105, 0.5);
  --block-color-hover: rgba(187, 255, 182, 0.5);
  --block-color-active: rgba(109, 168, 105, 0.5);
}
</style>
