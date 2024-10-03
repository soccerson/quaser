<template>
  <q-page padding>
    <div class="job-selection-container">
      <h4>新しい仕事を依頼</h4>
      <div>
        <h5 class="step-title">
          STEP 1 依頼したい仕事の業務内容を選びましょう
        </h5>
        <hr class="bold-line" />

        <!-- タブメニュー -->
        <q-tabs v-model="selectedTab" class="tab-container" inline-label>
          <q-tab name="popular" label="人気のカテゴリから選ぶ" />
          <q-tab name="all" label="すべてのカテゴリから選ぶ" />
        </q-tabs>

        <!-- 検索バー -->
        <q-input
          filled
          placeholder="キーワードでカテゴリを検索できます！"
          v-model="searchQuery"
          class="search-bar"
          prepend-icon="search"
        />

        <div class="categories-container">
          <!-- カテゴリリスト -->
          <div class="categories-list">
            <q-list bordered>
              <q-item
                v-for="category in filteredCategories"
                :key="category.name"
                clickable
                @click="selectCategory(category)"
              >
                <q-item-section>{{ category.name }}</q-item-section>
              </q-item>
            </q-list>
          </div>

          <!-- カテゴリ詳細 -->
          <div class="category-details">
            <div v-if="selectedCategory">
              <h4>{{ selectedCategory.name }}</h4>
              <ul>
                <li v-for="detail in selectedCategory.details" :key="detail">
                  {{ detail }}
                </li>
              </ul>
            </div>
            <div v-else>
              <p>カテゴリを選択してください。</p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <h5 class="step-title">STEP 1 依頼したい仕事を選びましょう</h5>
        <hr class="bold-line" />
      </div>
      <div>
        <h5 class="step-title">STEP 1 依頼したい仕事を選びましょう</h5>
        <hr class="bold-line" />
      </div>
      <div>
        <h5 class="step-title">STEP 1 依頼したい仕事を選びましょう</h5>
        <hr class="bold-line" />
      </div>
      <div>
        <h5 class="step-title">STEP 1 依頼したい仕事を選びましょう</h5>
        <hr class="bold-line" />
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      selectedTab: "popular", // デフォルトのタブ
      searchQuery: "",
      selectedCategory: null, // 選択されたカテゴリ
      categories: [
        {
          name: "システム開発",
          details: ["サイト構築", "業務システム", "ウェブ開発"],
        },
        {
          name: "AI（人工知能）・機械学習",
          details: ["機械学習", "ChatGPT開発", "チャットボット開発"],
        },
        {
          name: "アプリ・スマートフォン開発",
          details: ["iPhoneアプリ", "Androidアプリ"],
        },
        {
          name: "ホームページ制作・Webデザイン",
          details: ["ホームページ作成", "ランディングページデザイン"],
        },
        {
          name: "ECサイト・ネットショップ構築",
          details: ["ECサイト制作", "商品登録"],
        },
        { name: "デザイン", details: ["ロゴデザイン", "バナーデザイン"] },
        {
          name: "動画・映像・アニメーション",
          details: ["YouTube動画作成", "動画編集"],
        },
      ],
    };
  },
  computed: {
    // 検索結果に応じてカテゴリをフィルタリング
    filteredCategories() {
      if (this.searchQuery) {
        return this.categories.filter((category) =>
          category.name.includes(this.searchQuery)
        );
      }
      return this.categories;
    },
  },
  methods: {
    // カテゴリ選択時の処理
    selectCategory(category) {
      this.selectedCategory = category;
    },
  },
};
</script>

<style scoped>
.bold-line {
  height: 3px; /* ラインの高さ（太さ）を設定 */
  background-color: #0072bc; /* 青色の背景 */
  border: none; /* デフォルトのボーダーを消す */
  margin: 20px 0; /* 上下の余白を調整 */
}
.job-selection-container {
  max-width: 1200px;
  margin: 0 auto;
}

.step-title {
  color: #1976d2;
  font-weight: bold;
  margin-bottom: 20px;
}

.tab-container {
  margin-bottom: 20px;
}

.search-bar {
  margin: 20px 0;
  max-width: 600px;
}

.categories-container {
  display: flex;
  gap: 20px;
}

.categories-list {
  flex: 1;
  max-width: 300px;
}

.category-details {
  flex: 2;
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
}
</style>
