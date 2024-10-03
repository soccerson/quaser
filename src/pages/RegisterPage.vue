<template>
  <q-page class="flex flex-center">
    <q-card class="q-pa-md" style="width: 400px">
      <q-card-section>
        <div class="text-h6">新規登録</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit="onSubmit">
          <q-input
            v-model="name"
            label="名前"
            outlined
            dense
            required
            class="q-mb-md"
          />
          <q-input
            v-model="email"
            label="Email"
            type="email"
            outlined
            dense
            required
            class="q-mb-md"
          />
          <q-input
            v-model="password"
            label="Password"
            type="password"
            outlined
            dense
            required
            class="q-mb-md"
          />
          <q-btn
            type="submit"
            label="登録"
            color="primary"
            unelevated
            class="full-width"
          />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    onSubmit() {
      // APIと連携した登録処理をここに実装
      console.log("登録情報:", this.name, this.email, this.password);
    },
  },
};
</script>

<style>
.full-width {
  width: 100%;
}
</style>
