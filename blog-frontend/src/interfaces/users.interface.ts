export interface Users {
  id: number
  user_post: UserPost[]
  last_login: Date | null
  is_superuser: boolean
  nickname: string
  first_name: string
  last_name: string
  email: string
  profile_picture: null | string
  groups: any[]
  user_permissions: number[]
}

export interface UserPost {
  id: number
  title: string
  short_desc: string | null
  content: string
  image: null | string
  user: number
}

export interface UserInformation {
  id: number
  user_post: any[]
  nickname: string
  first_name: string
  last_name: string
  email: string
  profile_picture: string
}
