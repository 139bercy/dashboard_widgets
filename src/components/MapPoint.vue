<template>
  <div id="map" class="map map-point"></div>
</template>

<script>
import store from '@/store'
import { mixin } from '@/utils.js'

import "leaflet/dist/leaflet.css";
import L from "leaflet";

// Code pour valider l'affichage des icônes de marker car cela ne fonctionne pas autrement
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

export default {
  name: 'MapPoint',
  mixins: [mixin],
  // components: {
  // },
  data () {
    return {
      indicateurs_data: [],
      map: undefined,
      markers: [],
      loading: true
    }
  },
  props: {
    indicateurs: Array,
    activatedIndicateurs: Array
  },
  computed: {
  },
  methods: {
    async getData (indicateur) {
      return await store.dispatch('getData', indicateur).then(data => {
        this.indicateurs_data[indicateur] = data
      })
    },
    defineMap(divId) {
      // TODO https://www.datavis.fr/index.php?page=leaflet-cluster ?
      this.map = L.map(divId).setView(
        /*coordonnées centrés sur la france*/[46.549, 2.210],
        /*précision de la carte pour voir la totalité de la france métropolitaine à l'écran*/5
      );
      // Mise en place de la cate OpenStreetMap
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
      }).addTo(this.map);

      // Affichage de l'échelle
      L.control.scale().addTo(this.map);
    },
    updateData (indicateur, color) {
      // console.log(indicateur, color)
      if (!this.indicateurs_data[indicateur]) {
        return;
      }
      const markers = { "entreprises": [] };
      //  Création des points d'intérêt (entreprise)
      this.indicateurs_data[indicateur].points.forEach(point => {
        // Rien ne sera affiché d'une entreprise si elle ne possède pas de coordonnées GPS !
        if (
          point.latitude && point.latitude !== 'nan' && point.latitude !== "null"
          && point.longitude && point.longitude !== 'nan' && point.longitude !== "null"
        ) {
          L.Icon.Default.prototype.options.className = `color-${color}`
          let marker = L.marker([point.latitude, point.longitude]);

          // let tooltip = `<b>${entreprise.identite["DENOMINATION_UNITE_LEGALE"]}</b>`
          let tooltip = `<b>${point.nom}</b><br/>SIREN: ${point.siren}<br/><br/><small>Date de mise à jour: ${point.last_date}</small>`
          marker.bindTooltip(tooltip);
          markers.entreprises.push(marker);
        }
      });

      const layerGroup = L.layerGroup(markers.entreprises);
      // this.map.addLayer(layerGroup)
      // console.log("indicateur '" + indicateur + "' added")
      return layerGroup
    },
    toggleIndicateurs () {
      this.indicateurs.forEach((indicateur,index) => {
        // console.log(this.activatedIndicateurs.join('\t|\t'))
        if (this.activatedIndicateurs.includes(indicateur) && this.markers[indicateur] && !this.map.hasLayer(this.markers[indicateur])) {
          // console.log(index, indicateur, this.markers, this.markers[indicateur])
          L.Icon.Default.prototype.options.className = `color-${index+1}`
          this.map.addLayer(this.markers[indicateur])
        }
        if (!this.activatedIndicateurs.includes(indicateur) && this.markers[indicateur] && this.map.hasLayer(this.markers[indicateur])) {
          this.map.removeLayer(this.markers[indicateur]);
        }
      })
    },
  },
  async mounted () {
    this.defineMap("map")
    const promises = await Promise.all(this.indicateurs.map(async (indicateur, index) => {
      return await this.getData(indicateur)
    }))
    const markers = []
    promises.map((_, index) => {
      return this.updateData(this.indicateurs[index], index+1)
    }).filter(layerGroup => layerGroup).forEach((layer, index) => {
      markers[this.indicateurs[index]] = layer
    })
    this.markers = markers
    this.toggleIndicateurs()
    // console.log(markers, this.markers)
    this.loading = false
  },
  watch: {
    activatedIndicateurs: function () {
      this.toggleIndicateurs()
    },
  }
}

</script>

<style lang="scss">


.map-point {

  /* Couleur par défaut dans MapPoint ne pas modifier color-0 */
  /* --map-point-color-0: #3383cc; */
  --map-point-color-0-H: 209deg;
  --map-point-color-0-S: 60%;
  --map-point-color-0-L: 50%;
  --map-point-color-0: hsl(var(--map-point-color-0-H), var(--map-point-color-0-S), var(--map-point-color-0-L));
  .leaflet-marker-icon {
    // calcule des couleurs à partir de cette technique
    // https://stackoverflow.com/questions/29037023/how-to-calculate-required-hue-rotate-to-generate-specific-colour
    &.color-0 {
      filter: hue-rotate(0deg);
    }
    &.color-1 {
      filter: hue-rotate(calc(var(--map-point-color-1-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-1-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-1-L) - var(--map-point-color-0-L))));
    }
    &.color-2 {
      filter: hue-rotate(calc(var(--map-point-color-2-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-2-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-2-L) - var(--map-point-color-0-L))));
    }
    &.color-3 {
      filter: hue-rotate(calc(var(--map-point-color-3-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-3-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-3-L) - var(--map-point-color-0-L))));
    }
    &.color-4 {
      filter: hue-rotate(calc(var(--map-point-color-4-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-4-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-4-L) - var(--map-point-color-0-L))));
    }
    &.color-5 {
      filter: hue-rotate(calc(var(--map-point-color-5-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-5-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-5-L) - var(--map-point-color-0-L))));
    }
    &.color-6 {
      filter: hue-rotate(calc(var(--map-point-color-6-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-6-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-6-L) - var(--map-point-color-0-L))));
    }
    &.color-7 {
      filter: hue-rotate(calc(var(--map-point-color-7-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-7-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-7-L) - var(--map-point-color-0-L))));
    }
    &.color-8 {
      filter: hue-rotate(calc(var(--map-point-color-8-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-8-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-8-L) - var(--map-point-color-0-L))));
    }
    &.color-9 {
      filter: hue-rotate(calc(var(--map-point-color-9-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-9-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-9-L) - var(--map-point-color-0-L))));
    }
    &.color-10 {
      filter: hue-rotate(calc(var(--map-point-color-10-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-10-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-10-L) - var(--map-point-color-0-L))));
    }
    &.color-11 {
      filter: hue-rotate(calc(var(--map-point-color-11-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-11-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-11-L) - var(--map-point-color-0-L))));
    }
    &.color-12 {
      filter: hue-rotate(calc(var(--map-point-color-12-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-12-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-12-L) - var(--map-point-color-0-L))));
    }
    &.color-13 {
      filter: hue-rotate(calc(var(--map-point-color-13-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-13-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-13-L) - var(--map-point-color-0-L))));
    }
    &.color-14 {
      filter: hue-rotate(calc(var(--map-point-color-14-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-14-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-14-L) - var(--map-point-color-0-L))));
    }
    &.color-15 {
      filter: hue-rotate(calc(var(--map-point-color-15-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-15-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-15-L) - var(--map-point-color-0-L))));
    }
    &.color-16 {
      filter: hue-rotate(calc(var(--map-point-color-16-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-16-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-16-L) - var(--map-point-color-0-L))));
    }
    &.color-17 {
      filter: hue-rotate(calc(var(--map-point-color-17-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-17-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-17-L) - var(--map-point-color-0-L))));
    }
    &.color-18 {
      filter: hue-rotate(calc(var(--map-point-color-18-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-18-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-18-L) - var(--map-point-color-0-L))));
    }
    &.color-19 {
      filter: hue-rotate(calc(var(--map-point-color-19-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-19-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-19-L) - var(--map-point-color-0-L))));
    }
    &.color-20 {
      filter: hue-rotate(calc(var(--map-point-color-20-H) - var(--map-point-color-0-H)))
              // saturate(calc(100% + (var(--map-point-color-20-S) - var(--map-point-color-0-S))))
              brightness(calc(100% + (var(--map-point-color-20-L) - var(--map-point-color-0-L))));
    }
  }
}
 // .leaflet-marker-icon { filter:hue-rotate(250deg) }
</style>
