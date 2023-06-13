import { createStore } from 'vuex'

export default createStore({
    state: {    
        token: '',
        isAuthenticated: false,
        grupos: [],
        contadorGrupos: 1,
        grupoSeleccionado: null,
        actividad: null,
    },
    mutations: {
        initializeStore(state) {
            if ( localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state){
            state.token = ''
            state.isAuthenticated = false
        },
        agregarGrupo(state, grupo) {
            grupo.id = state.contadorGrupos; // Asignar el ID utilizando el contador de grupos
            state.grupos.push(grupo);
            state.contadorGrupos++; // Incrementar el contador de grupos en 1        
        },
        seleccionarGrupo(state, grupo) {
            state.grupoSeleccionado = grupo;
        },
        setActividad(state, actividad) {
            state.actividad = actividad;
        },
    },
    actions: {
        crearGrupo({ commit }, grupo) {
            commit('agregarGrupo', grupo);
          },
          seleccionarGrupo({ commit }, grupo) {
            commit('seleccionarGrupo', grupo);
          },
    },
    modules: {
    },
    getters: {
        obtenerGrupos(state) {
          return state.grupos;
        },
        obtenerGrupoSeleccionado(state) {
          return state.grupoSeleccionado;
        },
        getActividad(state) {
            return state.actividad;
        },
      }
})