<template>
  <q-page padding>
    <h4>練習メニューを自動作成</h4>
    <h5 class="step-title">行いたい練習メニューを選択してください</h5>
    <hr class="bold-line" />
    <div class="q-pa-md q-gutter-sm" style="text-align:center">
      <q-btn color="primary" label="シュート練習多め" @click="handleSend('シュート練習多め')" />
      <q-btn color="secondary" label="パス練習多め" @click="handleSend('パス練習多め')" />
      <q-btn color="amber" glossy label="ディフェンス練習多め" @click="handleSend('ディフェンス練習多め')" />
      <q-btn color="deep-orange" label="バランスよく" @click="handleSend('バランスよく')" />
      <!-- <q-btn color="deep-orange" glossy label="室内練習" @click="handleSend('室内練習')" /> -->
    </div>
    <div class="q-mt-md">
      <div v-for="(msg, index) in messages" :key="index">
        <q-card class="q-mb-sm">
          <q-card-section style="white-space:pre-wrap; word-wrap:break-word;">
            {{ msg }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { ref } from 'vue';
import { sendMessage } from 'src/services/openai';
import { useQuasar } from 'quasar'

export default {
  setup() {
    const messages = ref([]);
    const $q = useQuasar()

    const handleSend = async (userInput) => {
      $q.loading.show({
        message: 'ただいまAIが練習メニューを作成中です。'
      })
      messages.value
      if (userInput === '') return;

      const userMessage = userInput;
      console.log(userMessage);
      messages.value.push(`You: ${userMessage}`);
      // API 呼び出し
      try {
        const response = await sendMessage(userMessage);
        messages.value.push(`GPT: ${response}`);
      } catch (error) {
        messages.value.push('Error: Failed to get response from ChatGPT');
      }
      $q.loading.hide()
    };

    return {
      messages,
      handleSend
    };
  }
};
</script>

<style scoped>
.q-page {
  margin: auto;
}

.q-card {
  background-color: #f9f9f9;
}

.bold-line {
  height: 3px;
  background-color: #0072bc;
  border: none;
  margin: 20px 0;
}

.step-title {
  color: #1976D2;
  font-weight: bold;
  margin-bottom: 20px;
}
</style>
