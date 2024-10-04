<template>
  <q-page padding>
    <div class="job-management-container">
      <h4 class="header-title">仕事管理 - すべての形式</h4>
      <div class="job-management-info">
        <p>仕事自体の削除は「削除する」を選択してください。</p>
        <p>※仕事自体を削除すると、元に戻すことはできません。</p>
      </div>
      <!-- 削除ボタン -->
      <q-btn
        label="選択した仕事を削除"
        color="negative"
        class="q-mb-md"
        @click="deleteSelectedJobs"
        :disable="selectedJobs.length === 0"
      />
      <q-table
        :rows="jobs"
        :columns="columns"
        row-key="id"
        flat
        bordered
        class="job-table"
        selection="multiple"
        v-model:selected="selectedJobs"
      >
        <template v-slot:body-cell-action="props">
          <q-btn
            flat
            color="primary"
            label="操作を選択"
            @click="handleAction(props.row)"
          />
        </template>
      </q-table>
    </div>
  </q-page>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      jobs: [], // 仕事のリストを保持する配列
      selectedJobs: [], // チェックされた仕事のリスト
      columns: [
        {
          name: "id",
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        {
          name: "job_description",
          label: "業務内容",
          align: "left",
          field: "job_description",
          sortable: true,
        },
        {
          name: "num_of_people",
          label: "募集人数",
          align: "left",
          field: "num_of_people",
          sortable: true,
        },
        {
          name: "work_location",
          label: "勤務地",
          align: "left",
          field: "work_location",
          sortable: true,
        },
        {
          name: "budget",
          label: "給与",
          align: "left",
          field: "budget",
        },
        {
          name: "payment_type",
          label: "支払い形式",
          align: "left",
          field: "payment_type",
        },
        {
          name: "benefits",
          label: "待遇",
          align: "left",
          field: "benefits",
        },
      ],
    };
  },
  created() {
    // データベースから仕事のリストを取得
    axios
      .get("http://127.0.0.1:5000/api/jobs")
      .then((response) => {
        this.jobs = response.data;
      })
      .catch((error) => {
        console.error("Error:", error);
        this.$q.notify({
          type: "negative",
          message: "仕事リストの取得に失敗しました",
        });
      });
  },
  methods: {
    handleAction(row) {
      console.log("Selected action for row:", row);
      // 必要に応じて編集・コピー・削除の処理を追加
    },
    deleteSelectedJobs() {
      // 選択された行のIDを取得
      const idsToDelete = this.selectedJobs.map((job) => job.id);
      // 削除リクエストを送信
      axios
        .post("http://127.0.0.1:5000/api/jobs/delete", { ids: idsToDelete })
        .then(() => {
          // 成功時にテーブルから削除
          this.jobs = this.jobs.filter((job) => !idsToDelete.includes(job.id));
          this.$q.notify({
            type: "positive",
            message: "選択した仕事を削除しました",
          });
        })
        .catch((error) => {
          console.error("Error:", error);
          this.$q.notify({
            type: "negative",
            message: "選択した仕事の削除に失敗しました",
          });
        });
    },
  },
};
</script>
<style scoped>
.job-management-container {
  max-width: 1200px;
  margin: 0 auto;
}
.header-title {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 20px;
}
.job-management-info {
  margin-bottom: 20px;
}
.job-tabs {
  margin-bottom: 20px;
}
.job-filter {
  margin-bottom: 10px;
  font-weight: bold;
}
.job-table {
  margin-top: 20px;
}
</style>