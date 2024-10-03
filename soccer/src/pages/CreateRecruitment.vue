<template>
  <q-page padding>
    <div class="job-selection-container">
      <h4>新しい仕事を依頼</h4>

      <!-- STEP 1 -->
      <div>
        <h5 class="step-title">STEP 1 依頼したい仕事の内容を入力しましょう</h5>
        <hr class="bold-line" />

        <!-- 業務内容の例 -->
        <q-card flat bordered class="q-pa-md">
          <q-card-section>
            <div class="text-h6">業務内容の例：</div>
            <ul>
              <li>チーム練習の計画・指導</li>
              <li>試合の指導および管理</li>
              <li>チームメンバーへの個別指導・カウンセリング</li>
              <li>保護者および学校関係者とのコミュニケーション</li>
              <li>チーム運営に関するサポート</li>
            </ul>
          </q-card-section>
        </q-card>

        <!-- 業務内容入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              v-model="jobDescription"
              type="textarea"
              label="業務内容"
              filled
              placeholder="- 業務内容をここに入力してください..."
              rows="6"
              class="job-input"
            />
          </q-card-section>
        </q-card>
      </div>

      <!-- STEP 2 -->
      <div>
        <h5 class="step-title">STEP 2 勤務地を入力しましょう</h5>
        <hr class="bold-line" />

        <!-- 勤務地の例 -->
        <q-card flat bordered class="q-pa-md">
          <q-card-section>
            <div class="text-h6">勤務地の例：</div>
            <ul>
              <li>東京都渋谷区</li>
              <li>大阪府梅田周辺</li>
              <li>在宅勤務可</li>
            </ul>
          </q-card-section>
        </q-card>

        <!-- 勤務地入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              type="textarea"
              v-model="workLocation"
              label="勤務地"
              filled
              placeholder="- 勤務地をここに入力してください..."
              class="location-input"
            />
          </q-card-section>
        </q-card>
      </div>

      <!-- STEP 3 -->
      <div>
        <h5 class="step-title">STEP 3 予算と支払い方法を決めましょう</h5>
        <hr class="bold-line" />
        <!-- 支払い方式セクション -->
        <q-card flat bordered class="q-pa-md">
          <q-card-section>
            <div class="text-h6">
              支払い方式<span class="required">必須</span>
            </div>
            <q-option-group
              v-model="paymentType"
              :options="paymentOptions"
              type="radio"
              inline
              class="q-mt-md"
            />
            <div>
              支払い方式の違いについては
              <a href="#">こちら</a>をご確認ください。
            </div>
          </q-card-section>
        </q-card>

        <!-- 募集人数セクション -->
        <q-card flat bordered class="q-pa-md q-mt-md">
          <q-card-section>
            <div class="text-h6">
              募集人数<span class="required">必須</span>
            </div>
            <q-option-group
              v-model="recruitmentNumber"
              :options="recruitmentOptions"
              type="radio"
              inline
              class="q-mt-md"
            />
            <div v-if="recruitmentNumber === 'multiple'" class="q-mt-sm">
              <q-input
                v-model="numOfPeople"
                label="人数"
                type="number"
                outlined
                dense
                class="people-input"
                placeholder="2以上の人数を入力してください"
              />
            </div>
          </q-card-section>
        </q-card>

        <!-- 予算セクション -->
        <q-card flat bordered class="q-pa-md q-mt-md">
          <q-card-section>
            <div class="text-h6">予算<span class="required">必須</span></div>
            <q-option-group
              v-model="budgetSelection"
              :options="budgetOptions"
              type="radio"
              inline
              class="q-mt-md"
            />
            <div v-if="budgetSelection === 'specify'" class="q-mt-sm">
              <q-select
                v-model="budgetRange"
                :options="budgetRanges"
                label="予算の範囲を選択"
                outlined
                dense
              />
            </div>
          </q-card-section>
        </q-card>
      </div>
      <!-- STEP 4 -->
      <div>
        <h5 class="step-title">STEP 4 期限を決めましょう</h5>
        <hr class="bold-line" />

        <!-- 期限の例 -->
        <q-card flat bordered class="q-pa-md">
          <q-card-section>
            <div class="text-h6">期限の例：</div>
            <ul>
              <li>1週間以内に完了</li>
              <li>1ヶ月以内に完了</li>
              <li>特定の日付までに完了</li>
            </ul>
          </q-card-section>
        </q-card>

        <!-- 期限入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              v-model="deadline"
              label="期限"
              filled
              placeholder="- 期限をここに入力してください..."
              class="deadline-input"
            />
          </q-card-section>
        </q-card>
      </div>

      <!-- STEP 5 -->
      <div>
        <h5 class="step-title">STEP 5 待遇を決めましょう</h5>
        <hr class="bold-line" />

        <!-- 待遇の例 -->
        <q-card flat bordered class="q-pa-md">
          <q-card-section>
            <div class="text-h6">待遇の例：</div>
            <ul>
              <li>交通費支給</li>
              <li>ボーナスあり</li>
              <li>食事補助あり</li>
            </ul>
          </q-card-section>
        </q-card>

        <!-- 待遇入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              v-model="benefits"
              label="待遇"
              filled
              placeholder="- 待遇をここに入力してください..."
              class="benefits-input"
            />
          </q-card-section>
        </q-card>
      </div>
    </div>

    <div>
      <!-- 確認ボタン -->
      <q-btn
        label="確認"
        color="primary"
        @click="handleConfirm"
        class="q-my-md"
      />
    </div>
  </q-page>
</template>

<script>
export default {
  name: "ConfirmButton",
  data() {
    return {
      jobDescription: "", // 業務内容の入力内容を保持
      workLocation: "", // 勤務地の入力内容
      budget: "", // 予算の入力内容
      paymentMethod: "", // 支払い方法の入力内容
      deadline: "", // 期限の入力内容
      benefits: "", // 待遇の入力内容
    };
  },
  methods: {
    // 確認ボタンがクリックされたときの処理
    handleConfirm() {
      alert("確認しました！");
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

.q-my-md {
  margin-top: 16px;
  margin-bottom: 16px;
}
</style>
