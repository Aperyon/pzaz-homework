<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const { id: bookId } = route.params

onMounted(() => store.dispatch('loadBook', bookId))

const book = computed(() => store.state.book)
</script>

<template>
  <h1>Book Detail</h1>
  <router-link to="/books">Go back to books</router-link>
  <p v-if="book === null">Loading</p>

  <div v-else>
    <p><strong>Title</strong>: {{ book.title }}</p>
  </div>
</template>
