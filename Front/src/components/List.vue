<script setup>
import {ref , onMounted} from 'vue'
import axios from 'axios'
import router from '../router';

const data = ref([{
  id: "",
  nombre: "",
  fechaInicio: "",
  fechaFin: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/actividad')
  .then((result) => {
    console.log(result.data);
    data.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

function goToTask(id){
  router.push({ name: 'task', params: { id: id } })
}

</script>

<template>
    <ol class="list-group list-group-numbered">
  <li class="list-group-item d-flex justify-content-between align-items-start" data-bs-theme="dark" v-for="(item,i) in data" :key="i" 
      @click="goToTask(item.id)">
    <div class="ms-2 me-auto">
      <div class="fw-bold">{{ item.nombre }}</div>
      <strong>Fecha de Inicio:</strong> {{ item.fechaInicio }} <br>
      <strong>Duracion:</strong> {{ item.duracion }} <br>
    </div>
    <span class="badge bg-primary rounded-pill">{{ item.fechaFin }}</span>
  </li>
</ol>
</template>

<script>
export default {
    name: 'List'
}
</script>