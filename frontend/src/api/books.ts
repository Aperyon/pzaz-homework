import type { Book } from '@/types/book'
import { type AxiosResponse } from 'axios'
import { axiosInstance } from '.'

export function fetchBooks(): Promise<AxiosResponse<Book[]>> {
  const url = '/api/books/'
  return axiosInstance.get(url)
}

export function fetchBook(id: string): Promise<AxiosResponse<Book[]>> {
  const url = `/api/books/${id}/`
  return axiosInstance.get(url)
}

export function deleteBook(id: string) {
  const url = `/api/books/${id}/`
  return axiosInstance.delete(url)
}

export function addBook(values: Partial<Book>) {
  const url = '/api/books/'
  return axiosInstance.post(url, values, { headers: { 'Content-Type': 'multipart/form-data' } })
}
