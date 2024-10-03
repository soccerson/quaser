<template>
    <div id="app">
        <div id="map"></div>
    </div>
</template>
<script>
export default {
  name: "SimpleMarkerMap",
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 40.12150192260742, lng: -100.45039367675781 },
        zoom: 4,
        mapId: "DEMO_MAP_ID",
      });

      // Add markers
      new google.maps.marker.AdvancedMarkerElement({
        position: { lat: 40.12150192260742, lng: -100.45039367675781 },
        map,
        title: "My location",
      });

      new google.maps.marker.AdvancedMarkerElement({
        position: { lat: 58.2728981, lng: -161.7464394 },
        map,
        title: "My location",
      });
    },
  }
};
</script>
<style>
    #map {
    height: 50vh; /* Fill the screen */
    width: 50%;
    }
    /* Always set the map height explicitly to define the size of the div
    * element that contains the map. */
    gmp-map {
        height: 100%;
    }
</style>