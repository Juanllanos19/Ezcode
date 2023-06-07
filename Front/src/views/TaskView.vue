<script setup>
import { onMounted, ref, ssrContextKey } from 'vue'
import axios from 'axios'
import router from '../router'

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
          <h2>{{ contenido.answer }}</h2>
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
  import { ref } from 'vue';
  import NavInit from '../components/NavInit.vue';
  
  export default {
    data() {
      return {
        respuestaSeleccionada: null
      };
    },
    methods: {
      enviarRespuesta() {
        if (this.respuestaSeleccionada === this.contenido.answer) {
          alert('¡Respuesta correcta!');
        } else {
          alert('Respuesta incorrecta. La respuesta correcta es: ' + this.contenido.answer);
        }
      },
    },
    components: {
      NavInit
    }
  };
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
