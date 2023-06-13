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
            path: "/quiz/:id",
            name: 'quiz',
            component: () => import('../views/QuizView.vue')
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
            component: () => import('../views/testView.vue')
        },
        {
            path: '/stats',
            name: 'stats',
            component: () => import('../views/StatsView.vue')
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
            path: "/task/:id",
            name: 'task',
            props: true,
            component: () => import('../views/TaskView.vue')
        },
        // {
        //     path: "/question/:id",
        //     name: 'question',
        //     props: true,
        //     component: () => import('../views/TaskMultView.vue')
        // },
        {
            path: '/setting',
            name: 'setting',
            component: () => import('../views/SettingsView.vue')
        },
        {
            path: '/form',
            name: 'form',
            component: () => import('../views/FormsView.vue')
        },
        {
            path: '/biblio',
            name: 'biblio',
            component: () => import('../views/BiblioView.vue')
        },
        {
            path: '/list',
            name: 'list',
            component: () => import('../views/ListView.vue')
        },
        {
            path: '/NavInit/:idUsuario',
            name: 'NavInit',
            props: true,
            component: () => import('../components/NavInit.vue')
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