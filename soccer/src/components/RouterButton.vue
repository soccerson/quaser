<template>
  <router-link :to="to" class="button-wrapper">
    <q-btn flat :label="label" :icon="icon" class="router-link-btn" />
  </router-link>
</template>

<script>
export default {
  name: "RouterButton",
  props: {
    to: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      default: null, // アイコンが必要な場合に使う
    },
  },
};
</script>

<style scoped>
.router-link-btn {
  width: auto; /* ボタンの幅を文字に自動で調整 */
  font-weight: bold; /* フォントの強調 */
  border-radius: 8px; /* ボタンの角を少し丸くする */
}
.button-wrapper {
  text-decoration: none;
  color: inherit;
  height: 100%; /* 親要素の高さを全体に */
}
</style>
