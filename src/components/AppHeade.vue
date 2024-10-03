<template>
  <q-header elevated>
    <q-toolbar>
      <q-toolbar-title>
        <img src="@/assets/logo.png" alt="Logo" class="logo" />
        TeamHub
      </q-toolbar-title>

      <q-btn flat label="機能" />
      <q-btn flat label="プラン" />
      <q-btn flat label="使い方" />
      <q-btn flat label="お問い合わせ" />

      <q-space />

      <q-btn flat label="ログイン" @click="goToLogin" />
      <q-btn color="green" label="サインアップ" @click="goToSignup" />
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  methods: {
    goToLogin() {
      this.$router.push("/login"); // ログインページに遷移
    },
    goToSignup() {
      this.$router.push("/signup"); // サインアップページに遷移
    },
  },
};
</script>

<style scoped>
.logo {
  width: 40px; /* ロゴのサイズを調整 */
  margin-right: 8px;
}
</style>
