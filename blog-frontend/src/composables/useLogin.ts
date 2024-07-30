import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useLogin = () => {
  const email = ref('')
  const password = ref('')
  const router = useRouter()

  const sumbitData = async () => {
    const endpoint = 'http://127.0.0.1:8000/users/token/'
    const data = {
      email: email.value,
      password: password.value
    }

    try {
      const response = await axios.post(endpoint, data)

      const { access, refresh } = response.data

      localStorage.setItem('accessToken', access)
      localStorage.setItem('refreshToken', refresh)
      localStorage.setItem('email', email.value)

      console.log('ejecutada')
      alert('Exitoso')
      router.replace({ name: 'home' })
    } catch (err) {
      console.error(err)
    }
  }

  return {
    email,
    password,
    sumbitData
  }
}
