<script setup>
import { onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useStore()

function onSubmit(values) {
  store.dispatch('login', values)
  router.push('/books')
}

onMounted(() => {
  if (localStorage.getItem('token')) {
    router.push('/books')
  }
})
</script>

<template>
  <FormKit type="form" @submit="onSubmit">
    <FormKit type="text" name="username" label="Email" />
    <FormKit type="password" name="password" label="Password" />
  </FormKit>
</template>
