<template>
  <div class="q-pa-md" style="max-width: 400px; margin: auto;">
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="q-gutter-md"
    >
      <!-- 性（姓）と名の入力フィールド -->
      <q-row class="q-gutter-md" justify="center">
        <q-col class="col-6">
          <q-input
            ref="lastNameRef"
            filled
            v-model="lastName"
            label="Last Name *"
            lazy-rules
            :rules="lastNameRules"
            style="max-width: 250px;"
          />
        </q-col>
        <q-col class="col-6">
          <q-input
            ref="firstNameRef"
            filled
            v-model="firstName"
            label="First Name *"
            lazy-rules
            :rules="firstNameRules"
            style="max-width: 250px;"
          />
        </q-col>
      </q-row>

      <!-- メールアドレス入力フィールド -->
      <q-row class="q-gutter-md" justify="center">
        <q-col class="col-12">
          <q-input
            ref="emailRef"
            filled
            type="email"
            v-model="email"
            label="Email Address *"
            hint="Please enter a valid email address"
            lazy-rules
            :rules="emailRules"
            style="max-width: 300px;"
          />
        </q-col>
      </q-row>

      <!-- パスワード入力フィールド -->
      <q-row class="q-gutter-md" justify="center">
        <q-col class="col-12">
          <q-input
            ref="passwordRef"
            filled
            type="password"
            v-model="password"
            label="Password *"
            lazy-rules
            :rules="passwordRules"
            style="max-width: 300px;"
          />
        </q-col>
      </q-row>

      <!-- 利用規約のトグル -->
      <q-row class="q-gutter-md" justify="center">
        <q-col class="col-12">
          <div>
            <q-toggle
              v-model="accept"
              label="" 
            />
            <span @click="goToTermsOfService" class="q-ml-sm">利用規約に同意する</span> 
          </div>
        </q-col>
      </q-row>

      <!-- 送信とリセットボタン -->
      <q-row class="q-gutter-md" justify="center">
        <q-col class="col-12 text-center">
          <q-btn label="Submit" type="submit" color="primary" />
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
        </q-col>
      </q-row>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lastName: '',
      firstName: '',
      email: '',
      password: '',
      accept: false,
      lastNameRules: [val => !!val || 'Last name is required'],
      firstNameRules: [val => !!val || 'First name is required'],
      emailRules: [
        val => !!val || 'Email is required', 
        val => /^\S+@\S+\.\S+$/.test(val) || 'Please enter a valid email address'
      ],
      passwordRules: [
        val => !!val || 'Password is required',
        val => val.length >= 6 || 'Password must be at least 6 characters long',
      ],
    };
  },
  methods: {
    onSubmit() {
      console.log("Last Name:", this.lastName, "First Name:", this.firstName, "Email:", this.email, "Password:", this.password, "Accept:", this.accept);
    },
    onReset() {
      this.lastName = '';
      this.firstName = '';
      this.email = '';
      this.password = '';
      this.accept = false;
    },
    goToTermsOfService() {
      window.open('https://example.com/terms', '_blank'); // ここに実際の利用規約のURL
    }
  }
}
</script>