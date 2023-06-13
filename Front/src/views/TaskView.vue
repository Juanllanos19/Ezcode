<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
const props = defineProps(['id'])

const preguntas = ref([
  {
    id: "",
    actividad: "",
    pregunta: {
      id: "",
      titulo: "",
      contenido: "",
      tipoP: "",
      estado: "",
      tema: "",
      profesor: "",
      dificultad: ""
    },
    valor: ""
  }
])


onMounted(() => {
  axios.get('http://localhost:8000/api/actividaPregunta/')
  .then(result => {
    console.log(result.data)
    preguntas.value = result.data
  })
  .catch(error => {
    console.log(error)
  })
})
</script>

<script>
import NavInit from '../components/NavInit.vue'


export default {
  components: {
    NavInit
  }
}

function goToPreguntaMultiple(id){
  router.push({ path: `/question/${id}` });
}
function goToPreguntaCode(id){
  router.push({ name: 'compiler', params: { id: id } })
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body>
      <div class="container" style=" padding-top: 8%; padding-left: 5%;">
        <h1>{{preguntas[0].actividad.nombre}}</h1>
        <div class="card w-25 mb-3" v-for="(item,i) in preguntas" :key="i">
        <div v-if="item.pregunta.tipoP">
          <div class="card-body">
            <h5 class="card-title">Pregunta {{ i +1 }}</h5>
            <p class="card-text"> Tipo: Opción Múltiple</p>
            <p class="card-text"> Valor: {{ item.valor }}</p>
            <a href="#" class="btn btn-primary" v-on:click="goToPreguntaMultiple(item.id)">Responder</a>
          </div>
        </div>
        <div v-else>
          <div class="card-body">
            <h5 class="card-title">Pregunta {{ i +1 }}</h5>
            <p class="card-text"> Tipo: Coding challenge</p>
            <p class="card-text"> Valor: {{ item.valor}}</p>
            <a href="#" class="btn btn-primary" v-on:click="goToPreguntaCode(item.id)">Responder</a>
          </div>
        </div>
      </div>
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
