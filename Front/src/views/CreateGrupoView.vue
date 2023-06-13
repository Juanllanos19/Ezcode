<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <h1>Lista de Alumnos</h1>
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
  margin: 0;
  padding: 80px;
}

h1 {
  margin-bottom: 20px;
}

.table {
  width: 80%;
  margin: 0 auto;  border-collapse: collapse;
  background-color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.table-container {
  width: 80%;
  margin-bottom: 20px;
}

/* Resto de tus estilos CSS existentes */


.table th,
.table td {
  padding: 10px;
  border-bottom: 1px solid #dddddd;
}

.table thead {
  background-color: #f2f2f2;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}

.checkbox-label {
  display: flex;
  align-items: center;
}

.checkbox-label input {
  margin-right: 5px;
}

.card {
  width: 80%;
  margin: 0 auto;
  margin-top: 20px;
  border: 1px solid #dddddd;
  border-radius: 4px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-header {
  padding: 10px 20px;
  background-color: #f2f2f2;
}

.card-body {
  padding: 20px;
}

.btn-primary {
  background-color: #00a9d4;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #00a9d4;
}
</style>
