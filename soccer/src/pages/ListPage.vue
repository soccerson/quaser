<template>
  <q-page padding>
    <div class="q-my-md">
      <h4>仕事管理</h4>
      <q-btn
        label="新しい仕事依頼を作成"
        color="primary"
        @click="goToFormPage"
      />
    </div>

    <!-- 仕事リストテーブル -->
    <q-table
      :rows="jobs"
      :columns="columns"
      row-key="id"
      flat
      bordered
      class="q-my-md"
    >
      <template v-slot:body-cell-status="props">
        <q-td :props="props">
          <q-badge color="red" label="公開待ち" />
        </q-td>
      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-select
            v-model="props.row.selectedAction"
            :options="actions"
            label="操作を選択"
            outlined
            dense
          />
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      jobs: [],
      columns: [
        {
          name: "title",
          required: true,
          label: "依頼タイトル",
          align: "left",
          field: "title",
        },
        { name: "format", label: "形式", align: "left", field: "format" },
        { name: "status", label: "ステータス", align: "left", field: "status" },
        { name: "needs", label: "対応が必要", align: "left", field: "needs" },
        { name: "actions", label: "編集・コピー・削除など", align: "left" },
      ],
      actions: ["編集", "コピー", "削除"],
    };
  },
  created() {
    // ページが作成されたときにローカルストレージからデータを読み込む
    this.jobs = JSON.parse(localStorage.getItem("jobs") || "[]");
  },
  methods: {
    goToFormPage() {
      this.$router.push("/create-recruitment");
    },
  },
};
</script>

<style scoped>
.q-my-md {
  margin: 16px 0;
}
</style>
