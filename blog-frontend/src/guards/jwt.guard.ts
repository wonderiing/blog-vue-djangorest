import type { RouteLocationNormalized, NavigationGuardNext } from 'vue-router'

const isAuthenticated = (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) => {
  const accesToken = localStorage.getItem('accessToken')

  if (!accesToken) {
    return next({
      name: 'auth'
    })
  }

  return next()
}

export default isAuthenticated
