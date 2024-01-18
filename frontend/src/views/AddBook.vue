<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

function onSubmit(values) {
  const payload = new FormData()
  payload.append('title', values.title)
  payload.append('description', values.description)
  if (values.cover_image[0]) {
    payload.append('cover_image', values?.cover_image[0]?.file || null)
  }
  store.dispatch('addBook', payload)
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
