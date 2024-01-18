import { axiosInstance } from '.'

export function login(values) {
  const url = '/auth/api-token-auth/'
  return axiosInstance.post(url, values)
}
