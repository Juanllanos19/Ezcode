<script setup>
import {ref , onMounted} from 'vue'
import axios from 'axios'

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

</script>

<template>
  <div class="card text-bg-dark mb-3" >
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Ultimo intento</th>
            <th scope="col">Titulo</th>
            <th scope="col">Tema</th>
            <th scope="col">Dificultad</th>
            <th scope="col">Resultado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in data" v-bind:key="i">
            <!-- Pensar si va fecha de inicio o fecha de fin -->
            <th scope="row">{{ item.actividad.actividad.fechaInicio }}</th>
            <td>{{ item.actividad.pregunta.titulo }}</td>
            <td>{{ item.actividad.pregunta.tema.tipo }}</td>
            <td>{{ item.actividad.pregunta.dificultad.rango }}</td>
            <td>{{ item.ponderacion + ' / ' + item.puntosTotal}}</td>
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