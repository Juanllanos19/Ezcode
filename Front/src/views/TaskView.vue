<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
import NavInit from '../components/NavInit.vue'

const props = defineProps(['id', 'idUsuario'])

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

function goToPreguntaMultiple(id, idUsuario) {
  router.push({ path: `/question/${id}/${idUsuario}` });
}

function goToPreguntaCode(id){
  router.push({ path: `/compiler/${props.idUsuario}/${id}` })
}


onMounted(() => {
  axios.get('http://localhost:8000/api/actividaPregunta/')
  .then(result => {
    console.log(result.data)
    preguntas.value = filterPreguntas(result.data)
  })
  .catch(error => {
    console.log(error)
  })
})

function filterPreguntas(lista){
  var respuesta = [];
  for (var i = 0; i < lista.length; i++){
    console.log("id?: ", lista[i].id)
    console.log("props: ", props.id)
    if(lista[i].actividad.id==props.id){
      respuesta.push(lista[i])
    }
  }
  console.log(respuesta)
  return respuesta
}

function checkCalif(item){
  for (let j = 0; j < Object.keys(data.value).length; j++){
    if(data.value[j]['estudiante']['id'] == parseInt(props.idUsuario) && item==data.value[j]['actividad']['pregunta'] && data.value[j]['actividad']['actividad']==props.id){
      return true
    }
  }
  return false
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
        <div v-if="item.pregunta.tipoP">
          <div class="card-body text-bg-dark">
            <h5 style="text-align: center;" class="card-title">Pregunta {{ i +1 }}</h5>
            <p style="text-align: center;" class="card-text"> Tipo: Opción Múltiple</p>
            <p style="text-align: center;" class="card-text"> Valor: {{ item.valor }}</p>
            <div v-if="!checkCalif(item.pregunta.id)">
              <a style="margin-left:42%;" href="#" class="btn btn-primary" @click="goToPreguntaMultiple(item.id,idUsuario)">Responder</a>
            </div>
            <div v-else>
              <div class="alert alert-warning" role="alert" style="text-align: center;">
                Contestada
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <div class="card-body text-bg-dark">
            <h5 style="text-align: center;" class="card-title">Pregunta {{ i +1 }}</h5>
            <p style="text-align: center;" class="card-text"> Tipo: Coding challenge</p>
            <p style="text-align: center;" lass="card-text"> Valor: {{ item.valor}}</p>
            <div v-if="!checkCalif(item.pregunta.id)">
              <a style="margin-left:42%;" href="#" class="btn btn-primary" @click="goToPreguntaCode(item.id)">Responder</a>
            </div>
            <div v-else>
              <div class="alert alert-warning" role="alert" style="text-align: center;">
                Contestada
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
    
    <router-link :to="`/inicio/${this.$route.params.idUsuario}`" class="nav-link text-white" id="menu-nav"><button style="margin-left:80%;" type="button" class="btn btn-success">ENTREGAR</button></router-link>
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
