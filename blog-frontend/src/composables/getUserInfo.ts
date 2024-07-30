import axios from 'axios'

export const getUserInfo = async (endpoint: string) => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`
    const response = await axios.get(endpoint)
    localStorage.setItem('id', response.data.id)
    return response.data
  } catch (err) {
    console.error(err)
  }
}
