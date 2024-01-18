<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import BookList from '@/components/BookList.vue'

const router = useRouter()
const store = useStore()
const books = computed(() => store.state.books)

onMounted(() => {
  if (!localStorage.getItem('token')) {
    router.push('/login')
  }
  store.dispatch('loadBooks')
})

function onLogoutClick() {
  localStorage.removeItem('token')
  location.reload()
}
</script>

<template>
  <h1>Books</h1>
  <router-link to="/books/add">Add new book</router-link>
  <BookList :books="books" />
  <button @click="onLogoutClick">Logout</button>
</template>
