<template>
  <div>
    <header>
      <NavInit />
    </header>

    <body style="padding-top: 6%;">
      <div class="header mt-4">
        <h2 class="mb-0">Lista de tareas creadas</h2>
      </div>
      <div class="container-fluid px-1 px-md-4 py-5 mx-auto">
        <div class="row d-flex justify-content-center px-3">
          <div class="text-center">
            <button class="button-1" role="button" @click="navigateToFormsView">Crear Pregunta</button>
            <button class="button-1" role="button" @click="navigateToListView">Crear Actividad</button>
          </div>
        </div>
        <div class="row d-flex justify-content-center px-3">
          <div class="card">
            <h2 class="ml-auto mr-4 mt-3 mb-0">{{ titulo.x }}</h2>
            <p class="ml-auto mr-4 mb-0 med-font">{{ grupo.x }}</p>
            <p class="ml-4 mb-4">{{ fecha.x }}</p>
            <p class="ml-4 mb-4">{{ tema.x }}</p>
            <button type="button" class="btn btn-outline-light edit-button">Editar</button>
          </div>
        </div>
      </div>
    </body>
  </div>
</template>

<script>
import NavInit from '../components/NavInitProf.vue'


export default {
  data() {
    return {
      titulo: { x: 'Título de ejemplo' },
      grupo: { x: 'Grupo de ejemplo' },
      fecha: { x: 'Fecha de ejemplo' },
      tema: { x: 'Tema de ejemplo' }
    };
  },
  components: {
    NavInit
  },
  methods: {
    navigateToFormsView() {
      this.$router.push('/form'); // Assuming you have defined the route for FormsView.vue
    },
    navigateToListView() {
      this.$router.push('/list'); // Assuming you have defined the route for ListView.vue
    }
  }
};
</script>

<style scoped>
body {
  overflow-x: hidden;
  height: 100%;
  background-image: url("http://i.imgur.com/w16HASj.png");
}

.header {
  text-align: center;
  color: #00a9d4;
  margin-top: -10px;
}

.card {
  color: #00a9d4;
  background-image: url("http://i.imgur.com/w16HASj.png");
  background-size: cover;
  width: 80%;
  height: 400px;
  border-radius: 20px;
  margin-top: 10px;
  margin-bottom: 50px;
  padding-top: 20px;
  position: relative;
}

.edit-button {
  position: absolute;
  bottom: 10px;
}

.time-font {
  font-size: 50px;
}

.sm-font {
  font-size: 18px;
}

.med-font {
  font-size: 28px;
}

.large-font {
  font-size: 60px;
}

.button-1 {
  background-color: #00a9d4;
  border-radius: 8px;
  border-style: none;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  line-height: 20px;
  list-style: none;
  margin: 0 10px;
  /* Añade un margen entre los botones */
  outline: none;
  padding: 10px 16px;
  position: relative;
  text-align: center;
  text-decoration: none;
  transition: color 100ms;
  vertical-align: baseline;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-1:hover,
.button-1:focus {
  background-color: #1c3166;
}
</style>
