<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <h1 style="text-align: center;">Crea tu Grupo</h1>
      <form @submit.prevent="crearGrupo">
        <label for="nombre">Nombre del grupo:</label>
        <input type="text" id="nombre" v-model="grupo.nombre" required>

        <label for="uf">UF:</label>
        <select id="uf" class="form-select" v-model="grupo.uf" required>
          <option v-for="(item, i) in uf" :key="i" :value="item.id">{{ item.siglas }}</option>
          <!-- Agrega las opciones de UF que necesites -->
        </select>

        <label for="cupo">Cupo límite:</label>
        <input type="number" id="cupo" v-model="grupo.cupo" required>

        <label for="estado">Estado del grupo:</label>
        <input type="checkbox" id="estado" v-model="grupo.estado">

        <label for="profesor">Profesor:</label>
        <select id="profesor" class="form-select" v-model="grupo.profesor" required>
          <option v-for="(item, i) in profesor" :key="i" :value="item.id"> {{ item.nombre }}</option>
        </select>

        <label for="periodo">Periodo:</label>
        <select id="periodo" class="form-select" v-model="grupo.periodo" required>
          <option v-for="(item, i) in periodo" :key="i" :value="item.id"> {{ item.fechaInicio + " | " +  item.fechaFin }}</option>
        </select>

        <button type="submit">Crear grupo</button>
      </form>
    </body>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

import NavInit from '../components/NavInitProf.vue';

const uf = ref([]);

const profesor = ref([]);

const periodo = ref([]);


onMounted(() => {
  axios
    .get('http://127.0.0.1:8000/api/uf/')
    .then(response => {
      uf.value = response.data;
    })
    .catch(error => {
      console.log(error);
    });
});

onMounted(() => {
    axios.get('http://localhost:8000/api/profesor/')
        .then(result => {
            console.log(result.data)
            profesor.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
})

onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/periodo/')
        .then(result => {
            console.log(result.data)
            periodo.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
})

const grupo = ref({
  nombre: '',
  uf: '',
  cupo: null,
  estado: false,
  profesor: '',
  periodo: ''
});

const crearGrupo = () => {
  // Aquí puedes realizar las acciones necesarias para crear el grupo,
  // como enviar los datos al servidor o ejecutar una función en tu aplicación.

  // Ejemplo de cómo acceder a los datos del grupo:
  console.log(grupo.value.nombre);
  console.log(grupo.value.uf);
  console.log(grupo.value.cupo);
  console.log(grupo.value.estado);
  console.log(grupo.value.profesor);
  console.log(grupo.value.periodo);
};
</script>


<style>
body {
  font-family: Arial, sans-serif;
  background-image: url("http://i.imgur.com/w16HASj.png");
  color: #00a9d4;
}

.table-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.table {
  width: 80%;
  border-collapse: collapse;
  background-color: #ffffff;
}

.card {
  width: 80%;
  border: 1px solid #dddddd;
  border-radius: 4px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
}
</style>