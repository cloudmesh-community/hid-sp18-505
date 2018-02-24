<template>
  <div class="row">
    <div class="col-md-6">
      <h2>Swagger Project Client</h2>
      <div id="map"></div>
    </div>
    <div class="col-md-6">Here</div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      map: null,
      tileLayer: null,
      layers: []
    }
  },
  mounted () {
    this.initMap()
    // this.initLayers();
  },
  methods: {
    initMap () {
      var srer = [31.854814534841164, -110.85308074951173]

      // eslint-disable-next-line
      var mymap = L.map('map').setView(new L.LatLng(srer[0], srer[1]), 11)

      // eslint-disable-next-line
      L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWNhdGVqciIsImEiOiJDTFpxOWpJIn0.1gwlWR5IcLfCAbBs0Ue27g', { maxZoom: 30, attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' + '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery &copy <a href="http://mapbox.com">Mapbox</a>', id: 'mapbox.streets'
      }).addTo(mymap)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  /* width: 100%*/;
  height: 500px;
}
</style>
