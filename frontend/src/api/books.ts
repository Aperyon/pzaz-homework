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
  const payload = new FormData()
  payload.append('title', values.title)
  payload.append('description', values.description)
  payload.append('cover_image', values.cover_image[0].file)
  return axiosInstance.post(url, payload, { headers: { 'Content-Type': 'multipart/form-data' } })
}
