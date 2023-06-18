<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <h1 style="text-align: center;">Crea tu Grupo</h1>
      <form>
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

        <button type="submit" @click="crearGrupo">Crear grupo</button>
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
  // Crea un objeto con los datos del grupo
  const nuevoGrupo = {
    nombre: grupo.value.nombre,
    uf: grupo.value.uf,
    cupo: grupo.value.cupo,
    estado: grupo.value.estado,
    profesor: grupo.value.profesor,
    periodo: grupo.value.periodo
  };

  // Realiza la solicitud POST utilizando Axios
  axios
    .post('http://127.0.0.1:8000/api/grupo/', nuevoGrupo)
    .then(response => {
      console.log(response.data); // Maneja la respuesta exitosa del servidor aquí
    })
    .catch(error => {
      console.log(error); // Maneja el error de la solicitud aquí
    });
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