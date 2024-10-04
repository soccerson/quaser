<template>
  <q-page padding>
    <q-card flat bordered class="q-pa-md q-my-md">
      <q-card-section>
        <h4>確認画面</h4>
        <!-- 2×7のテーブル -->
        <table class="confirm-table">
          <tbody>
            <tr>
              <th>業務内容</th>
              <td>{{ jobDescription }}</td>
            </tr>
            <tr>
              <th>人数</th>
              <td>{{ numpeople }}</td>
            </tr>
            <tr>
              <th>勤務地</th>
              <td>{{ workLocation }}</td>
            </tr>
            <tr>
              <th>予算</th>
              <td>{{ budget }}</td>
            </tr>
            <tr>
              <th>支払い方法</th>
              <td>{{ paymentTypeLabel }}</td>
            </tr>
            <tr>
              <th>期限</th>
              <td>{{ deadline }}</td>
            </tr>
            <tr>
              <th>待遇</th>
              <td>{{ benefits }}</td>
            </tr>
          </tbody>
        </table>
        <!-- ボタン -->
        <div class="button-container">
          <q-btn
            label="修正する"
            color="grey-5"
            class="full-width-btn"
            @click="goBack"
          />
          <q-btn
            label="送信"
            color="primary"
            class="full-width-btn"
            @click="handleSubmit"
          />
        </div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      jobDescription: "",
      numpeople: "",
      workLocation: "",
      budget: "",
      paymentType: "",
      deadline: "",
      benefits: "",
    };
  },
  computed: {
    paymentTypeLabel() {
      return this.paymentType === "bank" ? "銀行振込" : "現金払い";
    },
  },
  created() {
    // クエリパラメータからデータを取得
    this.jobDescription = this.$route.query.jobDescription;
    this.numpeople = this.$route.query.numpeople;
    this.workLocation = this.$route.query.workLocation;
    this.budget = this.$route.query.budget;
    this.paymentType = this.$route.query.paymentType;
    this.deadline = this.$route.query.deadline;
    this.benefits = this.$route.query.benefits;
  },
  methods: {
    goBack() {
      // 入力画面に戻る処理
      this.$router.push({ path: "/create-recruitment" });
    },
    handleSubmit() {
      axios
        .post(
          "http://127.0.0.1:5000/api/jobs",
          {
            jobDescription: this.jobDescription,
            numpeople: this.numpeople,
            workLocation: this.workLocation,
            budget: this.budget,
            paymentType: this.paymentType,
            deadline: this.deadline,
            benefits: this.benefits,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          console.log(response.data.message);
          this.$q.notify({
            type: "positive",
            message: "仕事が正常に追加されました",
          });
        })
        .catch((error) => {
          console.error("Error:", error);
          this.$q.notify({
            type: "negative",
            message: "データベースへの保存に失敗しました",
          });
        });
    },
  },
};
</script>

<style scoped>
.q-my-md {
  margin: 16px 0;
}

.confirm-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 16px;
}

.confirm-table th,
.confirm-table td {
  padding: 12px;
  border: 1px solid #ccc;
  text-align: left;
}

.confirm-table th {
  background-color: #f0f8ff; /* 項目の背景色（薄い青） */
  font-weight: bold;
}

.confirm-table td {
  background-color: #f9f9f9; /* 内容の背景色（薄い灰色） */
}

.button-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px; /* ボタン間のスペース */
  margin-top: 16px;
}

.full-width-btn {
  flex: 1;
  height: 48px; /* ボタンの高さ */
}
</style>
