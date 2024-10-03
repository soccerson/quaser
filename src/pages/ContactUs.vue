<template>
  <q-page padding>
    <div class="contact-us-container">
      <h2>お問い合わせ</h2>
      <p class="intro-text">
        必要事項をご入力の上、下記のフォームよりお問い合わせください。
      </p>

      <q-form @submit="onSubmit">
        <!-- お名前 -->
        <q-input
          filled
          v-model="name"
          label="お名前"
          outlined
          :rules="[(val) => !!val || 'お名前を入力してください']"
          class="input-field"
        />

        <!-- メールアドレス -->
        <q-input
          filled
          v-model="email"
          label="メールアドレス"
          type="email"
          outlined
          :rules="[
            (val) => !!val || 'メールアドレスを入力してください',
            (val) =>
              /.+@.+\..+/.test(val) || '有効なメールアドレスを入力してください',
          ]"
          class="input-field"
        />

        <!-- 電話番号 -->
        <q-input
          filled
          v-model="phone"
          label="電話番号"
          type="tel"
          outlined
          class="input-field"
        />

        <!-- 問い合わせ内容 -->
        <q-input
          filled
          v-model="message"
          label="お問い合わせ内容"
          type="textarea"
          outlined
          :rules="[(val) => !!val || 'お問い合わせ内容を入力してください']"
          class="input-field"
        />

        <!-- 送信ボタン -->
        <q-btn
          label="送信する"
          type="submit"
          color="primary"
          class="submit-btn q-mt-md"
        />
      </q-form>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "ContactUs",
  data() {
    return {
      companyName: "",
      name: "",
      email: "",
      phone: "",
      message: "",
    };
  },
  methods: {
    onSubmit() {
      if (this.name && this.email && this.message) {
        // 実際にはここでAPIなどに問い合わせ内容を送信する処理を記述します。
        alert("お問い合わせありがとうございます！");
        // フォームをリセット
        this.companyName = "";
        this.name = "";
        this.email = "";
        this.phone = "";
        this.message = "";
      }
    },
  },
};
</script>

<style scoped>
.contact-us-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.intro-text {
  font-size: 16px;
  color: #555;
  margin-bottom: 20px;
}

.input-field {
  margin-bottom: 15px;
}

.submit-btn {
  width: 100%;
  font-weight: bold;
}
</style>
