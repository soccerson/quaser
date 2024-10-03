<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="custom-header">
      <div>
        <!-- ログインしている時 -->
        <div v-if="!isLoggedIn">
          <div>
            <q-toolbar>
              <q-toolbar-title class="app-name">
                <!-- <img src="@/assets/logo.png" alt="Logo" class="logo" /> -->
                サカいく2
              </q-toolbar-title>
              <RouterButton to="/login" label="すべての仕事" />
              <RouterButton to="/contact" label="お問い合わせ" />
              <q-btn flat label="ログアウト" @click="logout()" />
              <q-space />
              <div class="profile-info">
                <!-- <span class="profile-name">{{ userName }}さん</span> -->
                <span class="profile-name">Kさん</span>
              </div>
              <q-btn flat icon="mail" />
              <q-btn flat icon="notifications">
                <q-badge color="red" floating> 1 </q-badge>
              </q-btn>
              <q-btn flat icon="help_outline" />
            </q-toolbar>
          </div>
          <div class="second-toolbar">
            <q-toolbar>
              <div class="left-labels">
                <q-btn flat label="マイページ" />
                <q-btn flat label="対戦探し" />
                <RouterButton to="/create-recruitment" label="募集作成" />
                <q-btn flat label="求人依頼" />
                <q-btn flat label="メッセージ" />
              </div>
              <div class="right-label">
                <q-btn flat icon="swap_horiz" label="ワーカーに切り替える" />
              </div>
            </q-toolbar>
          </div>
        </div>

        <!-- ログインしていないとき -->
        <div v-else>
          <div>
            <q-toolbar>
              <q-toolbar-title class="app-name">
                <!-- <img src="@/assets/logo.png" alt="Logo" class="logo" /> -->
                サカいく
              </q-toolbar-title>
              <RouterButton to="/login" label="サカいくとは" />
              <RouterButton to="/contact" label="お問い合わせ" />
              <RouterButton to="/login" label="ログイン" />
              <RouterButton to="/signin" label="ログイン" color="orange" />
            </q-toolbar>
          </div>
        </div>
      </div>
    </q-header>
    <q-page-container>
      <router-view />
      <!-- ここに各ページのコンテンツが挿入される -->
    </q-page-container>
  </q-layout>
</template>

<script>
import RouterButton from "src/components/RouterButton.vue";
export default {
  data() {
    return {
      isLoggedIn: false, // ログイン状態を管理
    };
  },
  components: {
    RouterButton,
  },
  methods: {
    goToLogin() {
      // ログインページに遷移する処理
      this.$router.push("/login");
    },
    goToSignup() {
      // サインアップページに遷移する処理
      this.$router.push("/signup");
    },
    logout() {
      // ログアウト処理（ここでは単にログイン状態をfalseに）
      this.isLoggedIn = false;
    },
    login() {
      // ログイン処理（ログイン成功後にisLoggedInをtrueに）
      this.isLoggedIn = true;
    },
    goToCreste() {
      // 求人作成
      this.$router.push("/create");
    },
  },
  created() {
    // ここで仮にログイン状態を確認する（実際にはサーバーからの認証情報などを使用）
    const savedLoginStatus = localStorage.getItem("isLoggedIn");
    this.isLoggedIn = savedLoginStatus === "true";
  },
  watch: {
    isLoggedIn(newValue) {
      // ログイン状態を保存（例：localStorage）
      localStorage.setItem("isLoggedIn", newValue);
    },
  },
};
</script>

<style scoped>
.app-name {
  margin-left: 40px;
}
.custom-header {
  background-color: #ffffff; /* ヘッダーの背景色 */
  color: #000; /* テキスト色 */
}

.second-toolbar {
  background-color: #198dda; /* 2段目のツールバーの背景色 */
  color: #ffffff; /* テキスト色 */
  width: 100vw; /* ツールバーを画面幅いっぱいに設定 */
  max-width: 100%; /* 最大幅を画面いっぱいに設定 */
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.left-labels {
  display: flex;
  gap: 20px; /*ラベル間のスペースを調整 */
}

.right-label {
  margin-left: auto;
}

.q-btn {
  font-weight: bold; /* ボタンのフォントを強調 */
}

.q-toolbar-title {
  font-size: 20px; /* タイトルのフォントサイズ調整 */
}

.q-space {
  flex-grow: 1; /* 右側のアイコンボタンを右端に配置 */
}
</style>
