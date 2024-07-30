import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useRegister = () => {
  const last_name = ref('')
  const nickname = ref('')
  const email = ref('')
  const first_name = ref('')
  const password = ref('')
  const router = useRouter()

  const submitRegiser = async () => {
    //Preparamos la data para la peticion
    const endpoint = 'http://127.0.0.1:8000/users/register/'
    const data = {
      last_name: last_name.value,
      first_name: first_name.value,
      email: email.value,
      nickname: nickname.value,
      password: password.value
    }

    //Hacemos la peticion
    try {
      const response = await axios.post(endpoint, data)

      await new Promise((resolve) => setTimeout(resolve, 1000))
      alert('Exitoso')
      router.replace({ name: 'home' })
    } catch (err) {
      console.error(err)
    }
  }
  return {
    last_name,
    nickname,
    email,
    first_name,
    password,
    submitRegiser
  }
}
