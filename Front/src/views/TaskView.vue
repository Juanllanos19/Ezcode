<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
const props = defineProps(['id'])

const data = ref([{
  id: "",
  actividad: "",
  estudiante: "",
  ponderacion: "",
  puntosTotal: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/calificacion')
  .then((result) => {
    console.log(result.data);
    data.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

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
    <body style="padding-top: 8%; width: 80%; margin-left: 10%;">
      <div class="container">
        <h1 style="text-align: center;">{{preguntas[0].actividad.nombre}}</h1>
        <div style="width: 60%; margin-left: 20%;" class="card mb-3" v-for="(item,i) in preguntas" :key="i">
        <div v-for="(item1,j) in data" :key="j">
          <div v-if="item.pregunta.tipoP">
          <div class="card-body text-bg-dark">
            <h5 style="text-align: center;" class="card-title">Pregunta {{ i +1 }}</h5>
            <p style="text-align: center;" class="card-text"> Tipo: Opción Múltiple</p>
            <p style="text-align: center;" class="card-text"> Valor: {{ item.valor }}</p>
            <a style="margin-left:42%;" href="#" class="btn btn-primary" v-on:click="goToPreguntaMultiple(item.id)">Responder</a>
          </div>
        </div>
        <div v-else>
          <div class="card-body text-bg-dark">
            <h5 style="text-align: center;" class="card-title">Pregunta {{ i +1 }}</h5>
            <p style="text-align: center;" class="card-text"> Tipo: Coding challenge</p>
            <p style="text-align: center;" class="card-text"> Valor: {{ item.valor }}</p>
            <a style="margin-left:42%;" href="#" class="btn btn-primary" v-on:click="goToPreguntaCode(item.id)">Responder</a>
          </div>
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
        height: 100%;
        background-color: rgb(26, 22, 64);
        text-shadow: none;
    }
    
</style>
