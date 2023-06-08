<script setup>
import { defineProps, onMounted, ref } from 'vue'
import axios from 'axios'

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

function agregaCalif() {
    console.log(preguntas.value.id);
  var calificacion = {
    "actividad": {
      "id": preguntas.value.id,
      "actividad": preguntas.value.actividad,
      "pregunta": preguntas.value.pregunta,
      "valor": preguntas.value.valor  
    },
    "estudiante": {
      "id": "",
      "nombre": "Juan Carlos",
      "apellidoPat": "Llanos",
      "apellidoMat": "Ordoñez",
      "matricula": "A01734916"
    },
    "ponderacion": preguntas.value.valor,
    "puntosTotal": preguntas.value.valor
  };
  console.log(calificacion);
  var headers = { 'Content-Type': 'application/json' };
  axios.post('http://localhost:8000/api/calificacion/', calificacion, headers)
    .then(result => {
      console.log(result.data);
    })
    .catch(error => {
      console.log(error);
    });
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
                    <div style=" background-color: #304878; align-items: center; border-radius: 5px; text-align: left; width: 100%;">
                        <h1 style="color: white; padding-top: 0.7%;padding-bottom: 0.7%; padding-left: 8%;"> NO SE QUE PONER ACA</h1>
                    </div>
                <ul style="list-style: none;padding-left: 0;">
                    <li style="list-style: none; background-color: #7890A8; border-radius: 5px; text-align: left; width: 100%; padding-top: 2%;padding-bottom: 2%; margin-top: 2%; color: white; font-size: large; font-family: 'Roboto', sans-serif;" 
                    v-for="(opcion, index) in contenido.options" :key="index" >
                    <label >
                        <input type="radio" :name="'opcion-' + contenido.id" :value="opcion" v-model="respuestaSeleccionada" />
                        {{ opcion.text }}
                    </label>
                    </li>
                </ul>
              <button class="btn btn-success" @click="enviarRespuesta">Contestar</button>
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
