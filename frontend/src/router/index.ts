import { createRouter, createWebHistory } from 'vue-router'
import BooksView from '@/views/BooksView.vue'
import AddBook from '@/views/AddBook.vue'
import BookDetail from '@/views/BookDetail.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/books',
      name: 'book-list',
      component: BooksView
    },
    {
      path: '/books/add',
      name: 'book-add',
      component: AddBook
    },
    {
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetail
    }
  ]
})

export default router
