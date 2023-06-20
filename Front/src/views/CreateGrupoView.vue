<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <h1 style="text-align: center;">Crea tu Grupo</h1>
      <form>
        <div class="form-group">
          <label for="nombre">Nombre del grupo:</label>
          <input type="text" id="nombre" v-model="grupo.nombre" required class="form-control">
        </div>

        <div class="form-group">
          <label for="uf">UF:</label>
          <select id="uf" class="form-select-sm form-control" v-model="grupo.uf" required>
            <option v-for="(item, i) in uf" :key="i" :value="item.id">{{ item.siglas }}</option>
          </select>
        </div>

        <div class="form-group">
          <label for="cupo">Cupo límite:</label>
          <input type="number" id="cupo" v-model="grupo.cupo" required class="form-control">
        </div>

        <div class="form-group">
          <label for="estado">Estado del grupo:</label>
          <input type="checkbox" id="estado" v-model="grupo.estado">
        </div>

        <div class="form-group">
          <label for="profesor">Profesor:</label>
          <select id="profesor" class="form-select-sm form-control" v-model="grupo.profesor" required>
            <option v-for="(item, i) in profesor" :key="i" :value="item.id"> {{ item.nombre }}</option>
          </select>
        </div>

        <div class="form-group">
          <label for="periodo">Periodo:</label>
          <select id="periodo" class="form-select-sm form-control" v-model="grupo.periodo" required>
            <option v-for="(item, i) in periodo" :key="i" :value="item.id"> {{ item.fechaInicio + " | " + item.fechaFin }}
            </option>
          </select>
        </div>

        <button type="submit" @click="crearGrupo" @submit="crearGrupo" class="confirm-button">Crear grupo</button>
      </form>

      <!-- Popup -->
      <div class="popup" v-if="showPopup">
        <div class="popup-content">
          <h2>{{ popupTitle }}</h2>
          <p>{{ popupMessage }}</p>
          <button @click="closePopup">Cerrar</button>
        </div>
      </div>
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
const showPopup = ref(false);
const popupTitle = ref('');
const popupMessage = ref('');

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

const crearGrupo = (event) => {
  // Crea un objeto con los datos del grupo
  const nuevoGrupo = {
    nombre: grupo.value.nombre,
    uf: grupo.value.uf,
    cupo: grupo.value.cupo,
    estado: grupo.value.estado,
    profesor: grupo.value.profesor,
    periodo: grupo.value.periodo
  };
  event.preventDefault();

  // Realiza la solicitud POST utilizando Axios
  axios
    .post('http://127.0.0.1:8000/api/grupo/', nuevoGrupo)
    .then(response => {
      // Mostrar el popup después de crear el grupo
      showPopup.value = true;
      popupTitle.value = 'Grupo creado';
      popupMessage.value = 'El grupo se ha creado con éxito.';
      console.log(response.data); // Maneja la respuesta exitosa del servidor aquí
    })
    .catch(error => {
      // Mostrar el popup en caso de error
      showPopup.value = true;
      popupTitle.value = 'Error';
      popupMessage.value = 'No se pudo crear el grupo. Por favor, inténtalo nuevamente.';
      console.log(error); // Maneja el error de la solicitud aquí
    });
};

const closePopup = () => {
  if (showPopup.value) {
    showPopup.value = false;
  }
};

</script>


<style scoped>
body {
  background-image: url("http://i.imgur.com/w16HASj.png");
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-control {
  margin-top: 10px;
  height: 48px;
  width: 150%;
  border: 2px solid #eee;
  border-radius: 10px;
}

.form-control:focus {
  box-shadow: none;
  border: 2px solid #039BE5;
}

.confirm-button {
  height: 50px;
  border-radius: 10px;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.popup-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.popup h2 {
  margin-top: 0;
}

.popup p {
  margin-bottom: 20px;
}

.popup button {
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #039be5;
  color: #fff;
  border: none;
  cursor: pointer;
}

.popup button:hover {
  background-color: #0277bd;
}
</style>
