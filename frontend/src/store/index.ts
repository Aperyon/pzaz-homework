import { fetchBooks, deleteBook, addBook, fetchBook } from '@/api/books'
import { login } from '@/api/auth'
import { createStore } from 'vuex'

export const store = createStore({
  state: () => ({ books: [], book: null, user: null }),
  mutations: {
    setBooks(state, books) {
      state.books = books
    },
    setBook(state, book) {
      state.book = book
    },
    resetBooks(state) {
      state.books = []
    },
    selectBook(state, book) {
      state.book = book
    },
    resetBook(state) {
      state.book = null
    }
  },
  actions: {
    async loadBooks({ commit }) {
      const response = await fetchBooks()
      commit('setBooks', response.data)
    },
    async deleteBook({ dispatch }, book) {
      const response = await deleteBook(book.uuid)
      dispatch('loadBooks')
    },
    async addBook(store, values) {
      await addBook(values)
    },
    async loadBook({ commit }, bookId) {
      const response = await fetchBook(bookId)
      commit('setBook', response.data)
    },
    async login({ }, values) {
      const response = await login(values)
      localStorage.setItem('token', response.data.token)
    }
  }
})
