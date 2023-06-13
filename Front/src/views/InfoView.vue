<template>
    <div>
        <header>
            <NavInit />
        </header>
        <body style="padding-top: 6%;">
            <div class="header mt-4">
                <h2 class="mb-0">Grupos Creados</h2>
            </div>
            <div class="container-fluid px-1 px-md-4 py-5 mx-auto">
                <div class="row d-flex justify-content-center px-3">
                    <div class="text-center">
                        <button class="button-1" role="button" @click="navigateToCreateView">Crear Grupo</button>
                    </div>
                </div>
                <div class="row d-flex justify-content-center px-3">
                    <div v-for="grupo in grupos" :key="grupo.id" class="card">
                        <p class="ml-auto mr-4 mb-0 med-font">ID: {{ grupo.id }} - Nombre: {{ grupo.nombre }}</p>
                        <div class="card-footer">
                            <router-link :to="`/grupos/${grupo.id}`" class="btn btn-outline-light">Editar</router-link>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Aquí agregamos el componente InfoGroup -->
            <InfoGroup v-if="grupoSeleccionado" :grupo="grupoSeleccionado" :alumnos="alumnosDelGrupo" />
        </body>
    </div>
</template>

<script>
import NavInit from '../components/NavInitProf.vue'
import InfoGroup from './InfoGroup.vue';
import { mapGetters } from 'vuex';

export default {
    components: {
        InfoGroup,
        NavInit
    },
    methods: {
        navigateToCreateView() {
            this.$router.push('/Cgrupo'); // Asumiendo que has definido la ruta para el componente Cgrupo.vue
        },
        navigateToEditView(grupo) {
            this.$store.dispatch('seleccionarGrupo', grupo);
            this.$router.push(`/grupos/${grupo.id}`);
        }

    },
    computed: {
        ...mapGetters(['obtenerGrupos', 'obtenerGrupoSeleccionado']),
        grupos() {
            return this.obtenerGrupos;
        },
        alumnosDelGrupo() {
            const grupoSeleccionado = this.obtenerGrupoSeleccionado;
            if (grupoSeleccionado) {
                return grupoSeleccionado.alumnos;
            }
            return [];
        }
    }
};
</script>

  
  
<style>
body {
    overflow-x: hidden;
    height: 100%;
    background-image: url("http://i.imgur.com/w16HASj.png");
}

.header {
    text-align: center;
    color: #00a9d4;
    margin-top: -10px;
}

.card {
    color: #00a9d4;
    background-image: url("http://i.imgur.com/w16HASj.png");
    background-size: cover;
    width: 80%;
    height: 400px;
    border-radius: 20px;
    margin-bottom: 50px;
    padding-top: 20px;
    margin-top: auto;

}

.card-footer {
    margin-top: auto;
}

.time-font {
    font-size: 50px;
}

.sm-font {
    font-size: 18px;
}

.med-font {
    font-size: 28px;
}

.large-font {
    font-size: 60px;
}

.button-1 {
    background-color: #00a9d4;
    border-radius: 8px;
    border-style: none;
    box-sizing: border-box;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    height: 40px;
    line-height: 20px;
    list-style: none;
    margin: 0 10px;
    /* Añade un margen entre los botones */
    outline: none;
    padding: 10px 16px;
    position: relative;
    text-align: center;
    text-decoration: none;
    transition: color 100ms;
    vertical-align: baseline;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
}

.button-1:hover,
.button-1:focus {
    background-color: #1c3166;
}
</style>
  