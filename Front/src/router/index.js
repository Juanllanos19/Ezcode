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
            path: '/registerprof',
            name: 'registerprof',
            component: () => import('../views/RegisterProfView.vue')
        },
        {
            path: '/registerest',
            name: 'registerest',
            component: () => import('../views/RegisterEstView.vue')
        },
        {
            path: '/compiler',
            name: 'compiler',
            component: () => import('../views/CompilerView.vue')
        },
        {
            path: '/compiler',
            name: 'compiler',
            component: () => import('../views/CompilerView.vue')
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        },
        {
            path: '/vistapreviaProf/:idUsuario',
            name: 'vistapreviaProf',
            props: true,
            component: () => import('../views/VistaPreviaProfView.vue')
        },
        {
            path: '/vistapreviaEst/:idUsuario',
            name: 'vistapreviaEst',
            props: true,
            component: () => import('../views/VistaPreviaEstView.vue')
        }
    ]
})

export default router