<script setup>
import { defineProps, onMounted, ref } from 'vue'
import axios from 'axios'
import NavInit from '../components/NavInit.vue'

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

function agregaCalif(){
        var calificacion = 
        {
          "actividad": preguntas.actividad,
          "estudiante": {
            "id":"",
            "nombre": "Juan Carlos",
            "apellidoPat": "Llanos",
            "apellidoMat": "Ordoñez",
            "matricula": "A01734916",
        },
          "ponderacion": preguntas.valor,
          "puntosTotal": preguntas.valor 
        };
        var headers = {'Content-Type': 'application/json'};
        axios.post('http://localhost:8000/api/calificacion/', calificacion,
        headers)
    .then(result => {
        console.log(result.data)
    })
    .catch(error => {
    console.log(error)
    })
    }

    function agregaCalif2(){
        var calificacion = 
        {
          "actividad": preguntas.actividad,
          "estudiante": null,
          "ponderacion": 0,
          "puntosTotal": preguntas.valor 
        };
        var headers = {'Content-Type': 'application/json'};
        axios.post('http://localhost:8000/api/calificacion/', calificacion,
        headers)
    .then(result => {
        console.log(result.data)
    })
    .catch(error => {
    console.log(error)
    })
    }

const respuestaSeleccionada = ref(null)
const enviarRespuesta = () => {
  if (respuestaSeleccionada.value.text === contenido.value.options[contenido.value.answer].text) {
    agregaCalif()
    alert('¡Respuesta correcta!')
  } else {
    agregaCalif2()
    alert('Respuesta incorrecta. La respuesta correcta es:')
  }
}
</script>

<template>
    <div>
      <header>
        <NavInit />
      </header>
      <body style="display: flex; padding-top: 8%;">
        <div>
          <h2>{{ contenido.title }}</h2>
          <h2>{{ contenido.description }}</h2>
          <ul>
            <li v-for="(opcion, index) in contenido.options" :key="index">
              <label>
                <input type="radio" :name="'opcion-' + contenido.id" :value="opcion" v-model="respuestaSeleccionada" />
                {{ opcion.text }}
              </label>
            </li>
          </ul>
          <button @click="enviarRespuesta">Enviar</button>
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
  </style>
