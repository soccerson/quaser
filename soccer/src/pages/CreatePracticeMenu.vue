<template>
  <q-page padding>
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
  </q-page>
</template>

<script>
import { ref } from 'vue';
import { sendMessage } from 'src/services/openai';

export default {
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
  }
};
</script>

<style scoped>
.q-page {
  max-width: 600px;
  margin: auto;
}

.q-card {
  background-color: #f9f9f9;
}
</style>
