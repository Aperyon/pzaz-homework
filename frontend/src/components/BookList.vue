<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps(['books'])
const store = useStore()

function onClickDelete(book) {
  store.dispatch('deleteBook', book)
}

function onClickView(book) {
  router.push(`/books/${book.uuid}`)
}
</script>

<template>
  <p v-if="books.length === 0">There are no books to display</p>
  <table v-else>
    <thead>
      <tr>
        <th></th>
        <th>Title</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="book in books" :key="book.uuid">
        <td><img :src="book.cover_image" style="max-width: 40px" /></td>
        <td>{{ book.title }}</td>
        <td>
          <button @click="() => onClickView(book)">View</button>
          <button @click="() => onClickDelete(book)">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>
