<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="custom-header">
      <div>
        <!-- ログインしている時 -->
        <div v-if="!isLoggedIn">
          <div>
            <q-toolbar>
              <!-- サカいくタイトル -->
              <q-toolbar-title class="app-name"> サカいく </q-toolbar-title>
              <!-- ナビゲーションボタン -->
              <RouterButton to="/login" label="すべての仕事" class="nav-btn" />
              <RouterButton
                to="/contact"
                label="お問い合わせ"
                class="nav-btn"
              />
              <q-btn
                flat
                label="ログアウト"
                @click="logout()"
                class="nav-btn"
              />
              <q-space />
              <div class="profile-info">
                <span class="profile-name">Kさん</span>
              </div>
              <q-btn flat icon="mail" />
              <q-btn flat icon="notifications">
                <q-badge color="red" floating> 1 </q-badge>
              </q-btn>
              <q-btn flat icon="help_outline" />
            </q-toolbar>
          </div>

          <!-- 2段目のツールバー（メニュー部分） -->
          <div class="second-toolbar">
            <q-toolbar>
              <div class="left-labels">
                <q-btn
                  flat
                  to="/create_match"
                  label="対戦相手探し"
                  class="menu-btn"
                />
                <q-btn
                  flat
                  to="/create-practice-menu"
                  label="練習メニュー作成"
                  class="menu-btn"
                />
                <q-btn
                  flat
                  to="/create-recruitment"
                  label="募集作成"
                  class="menu-btn"
                />
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
              <q-toolbar-title class="app-name"> サカいく </q-toolbar-title>
              <RouterButton to="/login" label="サカいくとは" class="nav-btn" />
              <RouterButton
                to="/contact"
                label="お問い合わせ"
                class="nav-btn"
              />
              <RouterButton to="/login" label="ログイン" class="nav-btn" />
              <RouterButton to="/signin" label="新規登録" class="nav-btn" />
            </q-toolbar>
          </div>
        </div>
      </div>
    </q-header>

    <!-- メインコンテンツ -->
    <q-page-container>
      <router-view />
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
      this.$router.push("/login");
    },
    goToSignup() {
      this.$router.push("/signup");
    },
    logout() {
      this.isLoggedIn = false;
    },
    login() {
      this.isLoggedIn = true;
    },
    goToCreste() {
      this.$router.push("/create");
    },
  },
  created() {
    const savedLoginStatus = localStorage.getItem("isLoggedIn");
    this.isLoggedIn = savedLoginStatus === "true";
  },
  watch: {
    isLoggedIn(newValue) {
      localStorage.setItem("isLoggedIn", newValue);
    },
  },
};
</script>

<style scoped>
/* サカいくのタイトルを目立たせる */
.q-toolbar-title {
  font-size: 48px;
  font-weight: bold;
  color: white;
  background: #1565c0;
  padding: 12px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  border: 8px solid #0d47a1;
}

/* ナビゲーションボタン（すべての仕事、お問い合わせ、ログアウト） */
.nav-btn {
  background-color: transparent;
  color: white;
  margin-right: 20px;
  padding: 10px 20px;
  text-align: center;
  transition: background-color 0.3s, color 0.3s;
}

.nav-btn:hover {
  background-color: #42a5f5; /* ホバー時の色 */
  color: white;
  transform: translateY(-2px); /* 軽い浮き上がり効果 */
  box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
}

.q-space {
  flex-grow: 1;
}

/* ページ全体の青系統で統一した背景 */
body {
  background-color: #e3f2fd;
  color: #0d47a1;
}

/* ホバー時に文字が中央揃えになる */
.nav-btn {
  display: flex;
  justify-content: center;
  align-items: center;
}

.menu-btn {
  background-color: #42a5f5;
  color: white;
  border-radius: 12px;
  padding: 10px 20px;
  font-weight: bold;
  margin: 0 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease-in-out;
}

.menu-btn:hover {
  background-color: #64b5f6;
  transform: translateY(-2px);
  box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
}

.second-toolbar {
  background-color: #1e88e5;
  color: white;
  padding: 10px 0;
}

.profile-name {
  font-weight: bold;
  font-size: 18px;
  color: #ffffff;
}
</style>
