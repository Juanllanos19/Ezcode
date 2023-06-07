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
            path: "/desempenio",
            name: 'desempenio',
            component: () => import('../views/DesempenioView.vue')
        },
        {
            path: "/inicio",
            name: 'main',
            component: () => import('../views/MainView.vue')
        },
        {
            path: "/quiz/:id",
            name: 'quiz',
            props: true,
            component: () => import('../views/QuizView.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        }
    ]
})

export default router