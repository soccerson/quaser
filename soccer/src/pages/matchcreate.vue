<template>
<q-page padding>
  <h4 class="test">対戦相手探し</h4>
  <div id="app">
    <q-input
      v-model="userInput"
      placeholder="Ask something..."
      @keyup.enter="handleSend"
      class="q-mb-md"
    />
    <q-btn label="Send" @click="handleSend" color="primary" />
    <div class="q-mt-md">
      <div v-for="(msg, index) in messages" :key="index">
        <q-card class="q-mb-sm">
          <q-card-section>
            {{ msg }}
          </q-card-section>
        </q-card>
      </div>
    </div>

    <!----- 表の表示 ----->
    <div id="list">
      <h5 class="column-title">おすすめ対戦相手</h5>
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
    <!----- 表の表示 ----->
    <div>
      <table>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.column1 }}</td>
          <td>{{ item.column2 }}</td>
        </tr>
      </table>
    </div>
  </div>
</q-page>
</template>

<script>
import { ref } from 'vue';
import { sendMessage } from 'src/services/openai';
import 
export default {
  name: "SimpleMarkerMap",
  
  //chatgptの動作
  setup() {
    const userInput = ref('');
    const messages = ref([]);

    const handleSend = async () => {
      if (userInput.value.trim() === '') return;

      const userMessage = userInput.value;
      console.log(userMessage);
      messages.value.push(`You: ${userMessage}`);
      // API 呼び出し
      try {
        const response = await sendMessage(userMessage);
        messages.value.push(`GPT: ${response}`);
      } catch (error) {
        messages.value.push('Error: Failed to get response from ChatGPT');
      }

      userInput.value = '';  // 入力をリセット
    };

    return {
      userInput,
      messages,
      handleSend
    };
  },

  //tableにおすすめ対戦相手を表示
  data(){
    return{
      locations:[
        {schoolName: "A学校", schoolAdress:"A市", lat: 35.6895, lng: 139.6917},
        {schoolName: "B学校", schoolAdress:"B市", lat: 34.0522, lng: -118.2437}
      ]
    };
  },

  //google mapの表示
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
        this.locations.forEach(location => {
          new google.maps.marker.AdvancedMarkerElement({
          position: { lat: location.lat, lng: location.lng },
          map,
          title: location.schoolName,

        })
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
    margin-bottom: 50px;
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

  .column-title {
    color: #1976D2;
    font-weight: bold;
    margin-bottom: 20px;
  }
  .test {
  max-width: 1200px;
  margin: 0 auto;
  }
</style>
