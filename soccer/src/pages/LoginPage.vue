<template>
  <div class="q-pa-md" style="max-width: 300px">
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="q-gutter-md"
    >
      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Your name *"
        hint="Name and surname"
        lazy-rules
        :rules="nameRules"
      />

      <q-input
        ref="ageRef"
        filled
        type="number"
        v-model="age"
        label="Your age *"
        lazy-rules
        :rules="ageRules"
      />

      <q-toggle v-model="accept" label="I accept the license and terms" />

      <div>
        <q-btn label="Submit" type="submit" color="primary" />
        <q-btn
          label="Reset"
          type="reset"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </form>
  </div>
</template>

<!-- <template>
  <q-page class="flex flex-center">
    <q-card>
      <q-card-section>
        <div class="text-h6">ログイン</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit="onSubmit">
          <q-input v-model="email" label="Email" type="email" />
          <q-input v-model="password" label="Password" type="password" />
          <q-btn type="submit" label="ログイン" color="primary" />
        </q-form>
      </q-card-section>

      <q-card-actions align="center">
        <q-btn flat label="新規登録はこちら" @click="goToRegister" />
      </q-card-actions>
    </q-card>
  </q-page>
</template> -->

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    onSubmit() {
      // ログイン処理をここに実装（例: APIへのリクエスト）
      console.log("ログイン:", this.email, this.password);
    },
    goToRegister() {
      this.$router.push("/register");
    },
  },
};
</script>
