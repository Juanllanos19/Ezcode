<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <h1 style="text-align: center;">Lista de Alumnos</h1>
      <div class="table-container">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Nombre</th>
              <th scope="col">Grupo</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="alumno in alumnos" :key="alumno.id">
              <td>{{ alumno.nombre }}</td>
              <td>
                <input type="checkbox" v-model="alumno.enGrupo" @change="verificarGrupo" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="table-container">
        <div v-if="alumnosEnGrupo.length > 0" class="card">
          <div class="card-header">
            <h2>Alumnos en el Grupo:</h2>
            <button class="btn btn-primary" @click="crearGrupo">Crear Grupo</button>
          </div>
          <div class="card-body">
            <ul>
              <li v-for="alumno in alumnosEnGrupo" :key="alumno.id">{{ alumno.nombre }}</li>
            </ul>
          </div>
        </div>
      </div>
    </body>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';
import NavInit from '../components/NavInitProf.vue'

export default {
  data() {
    return {
      alumnos: [
        { id: 1, nombre: 'Alumno 1', enGrupo: false },
        { id: 2, nombre: 'Alumno 2', enGrupo: false },
        { id: 3, nombre: 'Alumno 3', enGrupo: false },
        // ... Agrega más alumnos según tus necesidades
      ]
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/estudiante/')
    .then(response => this.alumnos = response.data)
  },
  components: {
    NavInit
  },
  computed: {
    alumnosEnGrupo() {
      return this.alumnos.filter(alumno => alumno.enGrupo);
    }
  },
  methods: {
    verificarGrupo() {
      // Aquí puedes agregar lógica adicional para manejar la verificación del grupo
      // Por ejemplo, puedes mostrar una alerta o realizar una llamada a una API
    },
    crearGrupo() {
      // Aquí puedes agregar la lógica para crear el grupo
      // Por ejemplo, puedes guardar los alumnos seleccionados en una base de datos o realizar alguna acción específica
      console.log('Grupo creado');
    },
    ...mapActions(['crearGrupo']),
    crearNuevoGrupo() {
      // Lógica para crear el grupo
      const nuevoGrupo = { x: 'Nuevo Grupo' };
      this.crearGrupo(nuevoGrupo);
    }
  }
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