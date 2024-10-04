<template>
  <q-page padding>
    <h4 class="test">対戦相手を探しましょう！</h4>
    <div id="app">
      <q-input
        v-model="userInput"
        placeholder="例：シュート率を上げたい、移動に80分以内"
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
              <td>{{ location.schoolName }}</td>
              <td>{{ location.schoolAdress }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div id="map"></div>
    </div>
  </q-page>
</template>

<script>
import { ref } from "vue";
import { sendMessage } from "src/services/openai";
export default {
  name: "SimpleMarkerMap",

  //chatgptの動作
  setup() {
    const userInput = ref("");
    const messages = ref([]);

    const handleSend = async () => {
      if (userInput.value.trim() === "") return;

      const userMessage = userInput.value;
      console.log(userMessage);
      messages.value.push(`You: ${userMessage}`);
      // API 呼び出し
      try {
        const response = await sendMessage(userMessage);
        messages.value.push(`GPT: ${response}`);
      } catch (error) {
        messages.value.push("Error: Failed to get response from ChatGPT");
      }

      userInput.value = ""; // 入力をリセット
    };

    return {
      userInput,
      messages,
      handleSend,
    };
  },

  //tableにおすすめ対戦相手を表示
  data() {
    return {
      locations: [
        { schoolName: "A学校", schoolAdress: "A市" },
        { schoolName: "B学校", schoolAdress: "B市" },
      ],
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
  },
};
</script>
<style>
table {
  width: 80%;
  margin: 0 auto;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}

#list {
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
  color: #1976d2;
  font-weight: bold;
  margin-bottom: 20px;
}
.test {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
