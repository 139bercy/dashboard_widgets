<template>
  <div id="map" class="map"></div>
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
  components: {
  },
  data () {
    return {
      indicateur_data: undefined,
      map: undefined,
      markers: []
    }
  },
  props: {
    indicateur: String
  },
  computed: {
  },
  methods: {
    async getData () {
      // store.dispatch('getData', this.indicateur).then(data => {
      //   this.indicateur_data = data
      //   this.loading = false
      //   this.updateMap()
      // })
      // TODO
      await fetch("impact.data.json")
        .then(res => res.json())
        .then(data => {
          this.loading = false
          this.indicateur_data = data.find(d => d.code == this.indicateur)
          if (this.indicateur_data) {
            this.indicateur_data.points = JSON.parse(this.indicateur_data.points)
            this.updateData()
          }
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
    updateData () {
      this.map.removeLayer(this.markers);
      const markers = { "entreprises": [] };
      //  Création des points d'intérêt (entreprise)
      this.indicateur_data.points.forEach(point => {
        // Rien ne sera affiché d'une entreprise si elle ne possède pas de coordonnées GPS !
        if (point.latitude && point.longitude) {
          if (point.latitude !== "null" && point.longitude !== "null") {
            let marker = L.marker([point.latitude, point.longitude]);
            // let tooltip = `<b>${entreprise.identite["DENOMINATION_UNITE_LEGALE"]}</b>`
            let tooltip = `<b>${point.nom}</b><br/>SIREN: ${point.siren}<br/><br/><small>Date de mise à jour: ${point.last_date}</small>`
            marker.bindTooltip(tooltip);
            markers.entreprises.push(marker);
          }
        }
      });

      this.markers = L.layerGroup(markers.entreprises);
      this.map.addLayer(this.markers)
    },

    updateMap () {
      this.updateData()
    },
  },
  mounted () {
    this.defineMap("map")
    this.getData()
  },
  watch: {
    indicateur: function () {
      this.getData()
    },
  }
}

</script>

<style scoped lang="scss">

</style>
