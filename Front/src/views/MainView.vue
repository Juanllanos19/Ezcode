<script setup>
import {onMounted, ref, defineProps} from 'vue'
import axios from 'axios'
import router from '../router';
const {idUsuario} = defineProps(['idUsuario'])
const nombre = ref(null)
axios.get(`http://127.0.0.1:8000/api/estudiante/${idUsuario}`)
        .then(response => {
          nombre.value = response.data.nombre;
        })
        .catch(error => {
          console.error(error);
        });

const grupo = ref();
    function agregaGrupo(){
        var gpo = {
          "estudiante": idUsuario,
          "grupo": grupo.value};
        axios.post('http://127.0.0.1:8000/api/estudianteGrupo/', gpo)
    .then(result => {
        console.log(result.data)
    })
    .catch(error => {
    console.log(error)
    })
    }
</script>

<script>
import NavInit from '../components/NavInit.vue'
import AcordeonInit from '../components/AcordeonTareasMain.vue'
import List from '../components/List.vue'

export default {
  components: {
    NavInit,
    AcordeonInit,
    List,
  },
  methods: {
        created() {
          const idUsuario = this.$route.params.idUsuario;
          axios.get('http://127.0.0.1:8000/api/estudiante/${idUsuario}')
              .then(response => {
              console.log(response);
              })
              .catch(error => {
              console.error(error);
              });
        }
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit :idUsuario="idUsuario"/>
    </header>
    <body style="display: flex; padding-top: 8%;">
      <div id="tasks" style="width: 50%; padding-left: 5%; padding-right: 5%;">
        <h1 style="color: aqua; padding-top: 2%;"> Enrolarse a nuevo grupo</h1>
        <form @submit.prevent="agregaGrupo()">
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Codigo de grupo" v-model="grupo" aria-label="Username" aria-describedby="basic-addon1">
          </div>
          <button type="submit" class="btn btn-primary">Enrolarse</button>
        </form>
          <h1 style="color: aqua; padding-top: 2%;"> Task to do</h1>
          <List :idUsuario="idUsuario"/>
      </div>
        <div id="acts" style="width: 50%; padding-left: 10%; padding-right: 5%;">
          <h1 style="color: aqua; padding-top: 2%;"> Modulos y actividades</h1>
            <AcordeonInit />
        </div>
    </body>
    <RouterView />
  </div>
</template>

<style>
    body{
        width: 100%;
        height: 100%;
        background-color: rgb(26, 22, 64);
        text-shadow: none;
    }
    #menu-nav{
      text-decoration: underline;
    }
    #desempenio-nav{
      text-decoration: none;
    }
</style>
