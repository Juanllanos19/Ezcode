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
            path: '/compiler/:id',
            name: 'compiler',
            props: true,
            component: () => import('../views/testView.vue')
        },
        {
            path: '/stats',
            name: 'stats',
            component: () => import('../views/StatsView.vue')
        },
        {
            path: "/desempenio/:idUsuario",
            name: 'desempenio',
            props: true,
            component: () => import('../views/DesempenioView.vue')
        },
        {
            path: "/inicio/:idUsuario",
            name: 'main',
            props: true,
            component: () => import('../views/MainView.vue')
        },
        {
            path: "/desempenio/:idUsuario",
            name: 'desempenio',
            props: true,
            component: () => import('../views/DesempenioView.vue')
        },
        {
            path: "/task/:id/:idUsuario",
            name: 'task',
            props: true,
            component: () => import('../views/TaskView.vue')
        },
        {
            path: "/question/:id/:idUsuario",
            name: 'question',
            props: true,
            component: () => import('../views/TaskMultView.vue')
        },
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
            path: '/biblio/:idUsuario',
            name: 'biblio',
            props: true,
            component: () => import('../views/BiblioView.vue')
        },
        {
            path: '/list/:idUsuario',
            name: 'list',
            props: true,
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
        },
        {
            path: '/Cgrupo',
            name: 'Cgrupo',
            props: true,
            component: () => import('../views/CreateGrupoView.vue')
        },
        {
            path: '/info/:idUsuario',
            name: 'info',
            props: true,
            component: () => import('../views/InfoView.vue')
        },
        {
            path: '/pregu',
            name: 'pregu',
            props: true,
            component: () => import('../components/Pregunta.vue')
        },
    ]
})

export default router