<script setup>
import {ref , onMounted} from 'vue'
import axios from 'axios'
const {idUsuario} = defineProps(['idUsuario'])

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

<template>
  <div class="card text-bg-dark mb-3" >
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Ultimo intento</th>
            <th scope="col">Titulo</th>
            <th scope="col">Dificultad</th>
            <th scope="col">Resultado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in data" v-bind:key="i">
            <div style="width:100%;" v-if="item.estudiante.id==parseInt(idUsuario)">
              <div style="width:100%;" v-for="(item1,j) in preguntas" v-bind:key="j">
                <div style="width:100%;" v-if="item.actividad.id==parseInt(item1.actividad.id)">
                  <th  scope="row">{{ item.actividad.actividad.fechaInicio }}</th>
                    <td>{{ item1.actividad.fechaInicio }}</td>
                    <td>{{ item1.pregunta.titulo }}</td>
                    <td>{{ item1.pregunta.dificultad }}</td>
                    <td>{{ item.ponderacion + ' / ' + item.puntosTotal}}</td>
                  </div>
              </div>
            </div>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
  .card{
    width: 60%;
  }
</style>

<script>
export default {
    name: 'WindowDesempenio'
}
</script>