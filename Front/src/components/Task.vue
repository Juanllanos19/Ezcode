<script setup>
import { createSlots, defineProps, onMounted, ref } from 'vue'
import axios from 'axios'
import router from '../router';

const props = defineProps(['id', 'idUsuario'])


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

const contenido = ref({})

onMounted(() => {
  axios.get('http://localhost:8000/api/actividaPregunta/' + props.id + '/')
  .then(result => {
    console.log(result.data)
    preguntas.value = result.data
    axios.get(preguntas.value.pregunta.contenido)
    .then(response => {
      contenido.value = response.data
      console.log(contenido.value.description)
    })
    .catch(error => {
      console.log(error)
    })
  })
  .catch(error => {
    console.log(error)
  })
})

function agregaCalif() {
  var calificacion = {
    "actividad": preguntas.value.id,
    "estudiante": props.idUsuario,
    "ponderacion": preguntas.value.valor,
    "puntosTotal": preguntas.value.valor
  };

  console.log(calificacion);
    axios.post('http://localhost:8000/api/calificacion/', calificacion)
    .then(response => {
      console.log('Solicitud exitosa:', response.data)
    })
    .catch(error => {
      console.error('Error al realizar la solicitud:', error)
    })
}

function agregaCalif2() {
  var calificacion = {
    "actividad": preguntas.value.actividad.id,
    "estudiante": props.idUsuario,
    "ponderacion": 0,
    "puntosTotal": preguntas.value.valor
  };
  console.log(calificacion);
    axios.post('http://localhost:8000/api/calificacion/', calificacion)
    .then(response => {
      console.log('Solicitud exitosa:', response.data)
    })
    .catch(error => {
      console.error('Error al realizar la solicitud:', error)
    })
}

const respuestaSeleccionada = ref(null)
const respuestaCorrecta = ref(null);

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function enviarRespuesta(id) {
  if (respuestaSeleccionada.value.text === contenido.value.options[contenido.value.answer].text) {
    respuestaCorrecta.value = true;
    agregaCalif()
    await delay(2000); // Esperar 3 segundos
    router.push({ path: `/task/${id}/${props.idUsuario}` });
  } else {
    respuestaCorrecta.value = false;
    agregaCalif2()
    await delay(2000); // Esperar 3 segundos
    router.push({ path: `/task/${id}/${props.idUsuario}` });
  }
}


</script>

<template>
    <div>
      <body style="display: flex; padding-top: 8%;">
            <div id="tasks" style="width: 50%; padding-left: 6%; padding-right: 2%;">
                <div style=" background-color: #304878; align-items: center; border-radius: 5px; text-align: left; width: 40%;">
                    <h1 style="color: white; padding-top: 1%;padding-bottom: 1%; padding-left: 8%;"> Descripcion</h1>
                </div>
                <div style="color: white; background-color: #7890A8; border-radius: 5px; text-align:left; width: 100%; height: 100%; margin-top:2%;">
                    <h2 style="color: white; padding-top: 3%;padding-left: 3%;">{{ contenido.title }}</h2> <br>
                    <h3 style="color: white; padding-top: 3%;padding-left: 3%;">{{ contenido.description }}</h3>
                </div>
            </div>
                <div id="acts" style="width: 50%; padding-left: 2%; padding-right: 10%;">
                <ul style="list-style: none;padding-left: 0;padding-top: 8%;">
                    <li style="list-style: none; background-color: #7890A8; border-radius: 5px; text-align: left; width: 100%; padding-top: 2%;padding-bottom: 2%; margin-top: 2%; color: white; font-size: large; font-family: 'Roboto', sans-serif;" 
                    v-for="(opcion, index) in contenido.options" :key="index" >
                    <label >
                        <input type="radio" :name="'opcion-' + contenido.id" :value="opcion" v-model="respuestaSeleccionada" />
                        {{ opcion.text }}
                    </label>
                    </li>
                </ul>
                <button class="btn btn-success" v-on:click="enviarRespuesta(preguntas.actividad.id,idUsuario)">Contestar</button>
                </div>
                <div v-if="respuestaCorrecta==null"></div>
                <div v-else-if="!respuestaCorrecta">
                  <div class="alert alert-success" role="alert">
                    <h4 class="alert-heading">Respuesta Incorrecta!</h4>
                  </div>
                </div>
                <div v-else-if="respuestaCorrecta">
                  <div class="alert alert-success" role="alert">
                    <h4 class="alert-heading">Respuesta Correcta!</h4>
                  </div>
                </div>
        </body>
      <RouterView />
    </div>
  </template>

<script>
export default {
    name: 'TaskMultiple'
}
</script>
  
  <style>
  body {
    width: 100%;
    height: 100%;
    background-color: rgb(26, 22, 64);
    text-shadow: none;
  }
  #menu-nav {
    text-decoration: underline;
  }
  #desempenio-nav {
    text-decoration: none;
  }
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');
  </style>
