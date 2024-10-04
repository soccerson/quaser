<template>
  <q-page padding>
    <div class="job-selection-container">
      <h4>対戦相手を探しましょう！</h4>
      <h5 class="step-title">対戦したい相手の特徴を入力してください</h5>
      <hr class="bold-line" />
      <div id="app">
        <q-input
          v-model="userInput"
          placeholder="例：勝率から対戦相手を取得"
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

    <v-container>
      <v-data-table
        :headers="headers"
        :items="schools"
        class="elevation-1"
      >
        <template v-slot:[`item.actions`]="{ item }">
          <v-btn color="primary" @click="editItem(item)">Edit</v-btn>
          <v-btn color="red" @click="deleteItem(item)">Delete</v-btn>
        </template>
      </v-data-table>
    </v-container>

<!----- 表の表示 ----->
        <div id="list">
          <h5 class="column-title">おすすめ対戦相手</h5>
          <table>
            <thead>
              <tr>
                <th>学校名</th>
                <th>緯度</th>
                <th>経度</th>
                <th>大会順位</th>
                <th>勝率</th>
                <th>失点率</th>
                <th>得点率</th>

              </tr>
            </thead>
            <tbody>
              <tr v-for="(location, index) in locations" :key="index">
                <td>{{ location.schoolName }}</td>
                <td>{{ location.lat }}</td>
                <td>{{ location.lng }}</td>
                <td>{{ location.match }}</td>
                <td>{{ location.winrate }}</td>
                <td>{{ location.lostpoint }}</td>
                <td>{{ location.getpoint }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div id="map"></div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { ref } from "vue";
import { sendMessage } from "src/services/openai";
import axios from "axios";
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

  created() {
    // データベースから学校のリストを取得
    axios
      .get("http://127.0.0.1:5000/api/school")
      .then((response) => {
        this.schools = response.data;
      })
      .catch((error) => {
        console.error("Error:", error);
        this.$q.notify({
          type: "negative",
          message: "仕事リストの取得に失敗しました",
        });
      });
  },
  data() {
    return {
      //schools: [],
      //headers: [
        //{ text: "学校名", value: "schoolName" },
        //{ text: "緯度", value: "lat" },
        //{ text: "経度", value: "lng" },
        //{ text: "大会順位", value: "match_number" },
        //{ text: "勝率", value: "winRate"},
        //{ text: "失点率", value: "LostPointRate" },
        //{ text: "得点率", value: "GetPointRate" },
      //],
      locations:[
        {schoolName:'千葉県立柏高校', lat:35.8932629, lng:139.9864032, match:2, winrate:0.80, lostpoint:0.3, getpoint:1.7},
        {schoolName:'桐光学園高校', lat:35.6026613, lng:139.469791, match:4, winrate:0.75, lostpoint:0.35, getpoint:1.6},
        {schoolName:'青森山田高校',lat:40.8039102, lng:140.7465038, match:5, winrate:0.75, lostpoint:0.35, getpoint:1.6}
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
        center: { lat: 35.4908426, lng: 139.6381515 },
        zoom: 4,
        mapId: "DEMO_MAP_ID",
      });

      // Add markers
      new google.maps.marker.AdvancedMarkerElement({
        position: { lat: 35.8932629, lng: 139.9864032 },
        map,
        title: "My location",
      });

      new google.maps.marker.AdvancedMarkerElement({
        position: { lat: 35.6026613, lng: 139.469791 },
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

.bold-line {
  height: 3px;
  background-color: #0072bc;
  border: none;
  margin: 20px 0;
}

.step-title {
  color: #1976d2;
  font-weight: bold;
  margin-bottom: 20px;
}

.job-selection-container {
  max-width: 1200px;
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
</style>
