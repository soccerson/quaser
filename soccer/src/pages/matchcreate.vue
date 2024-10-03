<template>
    <div id="app">
    <!----- 表の表示 ----->
        <div id="list">
          <h5>おすすめ対戦相手</h5>
          <table>
            <thead>
              <tr>
                <th>学校名</th>
                <th>住所</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(location, index) in locations" :key="index">
                <td>{{location.schoolName}}</td>
                <td>{{location.schoolAdress}}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div id="map"></div>
    </div>
</template>
<script>
export default {
  name: "SimpleMarkerMap",
  data(){
    return{
      locations:[
        {schoolName: "A学校", schoolAdress:"A市"},
        {schoolName: "B学校", schoolAdress:"B市"}
      ]
    };
  },
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
    table{
      width: 80%;
      margin: 0 auto;
      border-collapse: collapse;
    }

    th, td{
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }

    #list{
      margin-bottom: 80px;
    }
    #map {
    height: 50vh; /* Fill the screen */
    width: 80%;
    margin: 0 auto;
    }

    /* Always set the map height explicitly to define the size of the div
    * element that contains the map. */
    gmp-map {
        height: 100%;
    }
</style>