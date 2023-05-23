import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/HomeView.vue')
        },
        {
            path: "/inicio",
            name: 'main',
            component: () => import('../views/MainView.vue')
        },
        {
            path: "/quizes",
            name: 'quizes',
            component: () => import('../views/QuizesView.vue')
        },
        {
            path: "/quiz/:id",
            name: 'quiz',
            component: () => import('../views/QuizesView.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../components/Register.vue')
        }
    ]
})

export default router