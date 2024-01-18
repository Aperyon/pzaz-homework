<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

function onSubmit(values) {
  store.dispatch('addBook', values)
  router.push('/books')
}
</script>

<template>
  <router-link to="/books">Go back to books</router-link>
  <FormKit type="form" @submit="onSubmit">
    <FormKit type="text" name="title" label="Title" />
    <FormKit type="textarea" name="description" label="Description" />
    <FormKit type="file" name="cover_image" label="Cover Image" />
  </FormKit>
</template>
