import axios from 'axios'

export const generalGet = async (endpoint: string) => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`

    const response = await axios.get(endpoint)
    const data = response.data
    return data
  } catch (err) {
    console.error(err)
  }
}
