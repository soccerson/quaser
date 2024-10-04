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
            <div class="text-h6">
              業務内容<span class="required"
                ><span class="red-star">※</span>必須</span
              >
            </div>
            <ul>
              例：
              <li>チーム練習の計画・指導</li>
              <li>試合の指導および管理</li>
              <li>チームメンバーへの個別指導</li>
              <li>チーム運営に関するサポート</li>
            </ul>
          </q-card-section>
        </q-card>
        <!-- 業務内容入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              v-model="form.jobDescription"
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
      <!-- 募集人数セクション -->
      <div>
        <q-card flat bordered class="q-pa-md q-mt-md">
          <q-card-section>
            <div class="text-h6">
              募集人数<span class="required"
                ><span class="red-star">※</span>必須</span
              >
            </div>
            <div class="q-mt-sm">
              <q-input
                v-model="form.numpeople"
                label="人数"
                type="number"
                outlined
                dense
                class="people-input"
                placeholder="人数を入力してください"
              />
            </div>
          </q-card-section>
        </q-card>
      </div>

      <div class="q-mt-lg"></div>

      <!-- 期間入力のフォーム -->
      <q-card flat bordered class="q-pa-md q-mb-md">
        <q-card-section>
          <div class="text-h6">
            期間<span class="required"
              ><span class="red-star">※</span>必須</span
            >
          </div>
          <q-input
            type="textarea"
            v-model="form.deadline"
            label="期間"
            filled
            placeholder="- 期間をここに入力してください..."
            class="deadline-input"
          />
        </q-card-section>
      </q-card>

      <!-- STEP 2 -->
      <div>
        <h5 class="step-title">STEP 2 勤務地を入力しましょう</h5>
        <hr class="bold-line" />
        <!-- 勤務地入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <div class="text-h6">
              勤務地<span class="required"
                ><span class="red-star">※</span>必須</span
              >
            </div>
            <q-input
              type="textarea"
              v-model="form.workLocation"
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
        <!-- 予算入力のフォーム -->
        <q-card flat bordered class="q-pa-md q-mt-md">
          <q-card-section>
            <div class="text-h6">
              給与<span class="required"
                ><span class="red-star">※</span>必須</span
              >
            </div>
            <q-input
              type="textarea"
              v-model="form.budget"
              label="給与を入力してください"
              outlined
              dense
              placeholder="（例）時給1500円、日給1万円"
            />
          </q-card-section>
        </q-card>
      </div>

      <!-- 支払い方式入力のフォーム -->
      <q-card flat bordered class="q-pa-md q-mt-md">
        <q-card-section>
          <div class="text-h6">
            支払い方式<span class="required"
              ><span class="red-star">※</span>必須</span
            >
          </div>
          <q-option-group
            v-model="form.paymentType"
            :options="paymentOptions"
            type="radio"
            inline
            class="q-mt-md"
          />
        </q-card-section>
      </q-card>

      <!-- STEP 4 -->
      <div>
        <h5 class="step-title">STEP 4 待遇を決めましょう</h5>
        <hr class="bold-line" />
        <!-- 待遇入力のフォーム -->
        <q-card flat bordered class="q-pb-md q-mb-md">
          <q-card-section>
            <q-input
              type="textarea"
              v-model="form.benefits"
              label="待遇"
              filled
              placeholder="- 待遇をここに入力してください..."
              class="benefits-input"
            />
          </q-card-section>
        </q-card>
      </div>

      <div class="button-container">
        <!-- 戻るボタン -->
        <q-btn
          label="戻る"
          color="grey-5"
          class="full-width-btn"
          @click="goBack()"
        />
        <!-- 確認ボタン -->
        <q-btn
          label="確認"
          color="primary"
          class="full-width-btn"
          @click="handleConfirm"
        />
      </div>
    </div>
  </q-page>
</template>
<script>
export default {
  name: "ConfirmButton",
  data() {
    return {
      form: {
        jobDescription: "", // 業務内容の入力内容
        numpeople: "", // 人数
        workLocation: "", // 勤務地の入力内容
        budget: "", // 予算の入力内容
        paymentType: "", // 支払い方法の選択肢
        deadline: "", // 期間の入力内容
        benefits: "", // 待遇の入力内容
      },
      paymentOptions: [
        { label: "銀行振込", value: "bank" },
        { label: "現金払い", value: "cash" },
      ],
    };
  },
  created() {
    this.loadFromLocalStorage();
  },
  watch: {
    form: {
      handler() {
        this.saveToLocalStorage();
      },
      deep: true, // オブジェクト全体を監視
    },
  },
  methods: {
    saveToLocalStorage() {
      console.log("Saving to local storage...");
      localStorage.setItem("jobFormData", JSON.stringify(this.form));
    },
    loadFromLocalStorage() {
      const savedData = JSON.parse(localStorage.getItem("jobFormData"));
      if (savedData) {
        this.form = savedData;
      }
    },
    handleConfirm() {
      this.$router.push({
        path: "/confirm",
        query: {
          ...this.form,
        },
      });
    },
    goBack() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>
<style scoped>
.bold-line {
  height: 3px;
  background-color: #0072bc;
  border: none;
  margin: 20px 0;
}
.job-selection-container {
  max-width: 1200px;
  margin: 0 auto;
}
.step-title {
  color: #1976D2;
  font-weight: bold;
  margin-bottom: 20px;
}
.q-my-md {
  margin-top: 16px;
  margin-bottom: 16px;
}
.red-star {
  color: red;
  font-size: 0.85rem;
}
.required {
  color: red;
  font-size: 0.85rem;
  margin-left: 5px;
}
.button-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  max-width: 400px;
  margin: 0 auto;
}
.full-width-btn {
  flex: 1;
  height: 48px;
}
</style>
