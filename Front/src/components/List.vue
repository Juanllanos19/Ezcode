<script setup>
import {ref , onMounted, defineProps} from 'vue'
import axios from 'axios'
import router from '../router';
const {idUsuario} = defineProps(['idUsuario'])

function goToTask(id){
  router.push({ name: 'task', params: { id: id } })
}

const estudianteGrupo = ref([{
  estudiante: "",
  grupo: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/estudianteGrupo')
  .then((result) => {
    console.log(result.data);
    estudianteGrupo.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

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

const actGrupo = ref([{
  id: "",
  grupo: "",
  actividad: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/actividaGrupo')
  .then((result) => {
    console.log(result.data);
    actGrupo.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

</script>

<template>
  <div v-for="(item1,j) in estudianteGrupo" :key="j">
  <div v-if="item1.estudiante.id === parseInt(idUsuario)">
    <ol class="list-group list-group-numbered text-bg-primary">
      <li class="list-group-item d-flex justify-content-between align-items-start text-bg-primary" data-bs-theme="dark" v-for="(item2,k) in actGrupo" :key="k"
          @click="goToTask(item2.id)">
        <div class="ms-2 me-auto" v-if="item2.grupo.id === item1.grupo.id">
          <div class="fw-bold">{{ item2.actividad.nombre }}</div>
          <strong>Fecha de Inicio:</strong> {{ item2.actividad.fechaInicio }} <br>
          <strong>Duracion:</strong> {{ item2.actividad.duracion }} <br>
        </div>
        <span class="badge text-bg-danger rounded-pill">{{ item2.actividad.fechaFin }}</span>
      </li>
    </ol>
  </div>
  </div>
</template>

<script>
export default {
    name: 'List',
}
</script>