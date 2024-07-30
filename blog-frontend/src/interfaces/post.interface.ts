export interface UserPostReal {
  id: number
  title: string
  short_desc: string
  content: string
  image: null | string
  user: string
}

export interface MyPosts {
  user_post: UserPost[]
}

export interface UserPost {
  id: number
  user: string
  short_desc: string
  title: string
}
