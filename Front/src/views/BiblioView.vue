<template>
  <div>
    <header>
      <NavInit :idUsuario="idUsuario"/>
    </header>

    <body style="padding-top: 6%; width: 60%; margin-left: 20%;">
    <br><div class="header mt-4">
      <h2 class="mb-0">Lista de tareas creadas de {{ nombre }}</h2>
    </div>

    <div class="container-fluid px-1 px-md-4 py-5 mx-auto">
      <div class="row d-flex justify-content-center px-3">
        <button class="button-1" role="button" @click="navigateToFormsView">Crear Pregunta</button>
        <button class="button-1" role="button" @click="navigateToListView" style="margin-top: 1%;">Crear Actividad</button>
      </div>
        <div class="row d-flex justify-content-center px-3">
          <div class="card" style="width: 100%;" v-for="grupo in this.grupos" @click="goGrupo(grupo.id)">
                <div class="card-body">
                    <h2 class="card-title" style="font-size: 48px;">{{ grupo.nombre }}</h2>
                    <p class="card-text" style="font-size: 32px;">{{ grupo.uf.siglas }}</p> 
                </div>
          </div>
      </div>
    </div>
    </body>
  </div>
</template>

<script>
import NavInit from '../components/NavInitProf.vue'
import router from '../router';
import { ref } from 'vue';
import axios from 'axios';

export default {
  props: ['idUsuario'],
  data() {
      return {
        nombre: '',
        grupos: [{}]
      }
    },

    created() {
          axios.get(`http://127.0.0.1:8000/api/profesor/${this.idUsuario}`)
            .then(response => {
              this.nombre = response.data.nombre;
            })
            .catch(error => {
              console.error(error);
            });

          axios.get(`http://127.0.0.1:8000/api/grupo/`)
            .then(response => {
              this.grupos = this.filterGroups(response.data);
              console.log("Grupos: ", this.grupos);
            })
            .catch(error => {
              console.error(error);
            });
        },


  methods: {
      navigateToFormsView() {
        this.$router.push(`/form/${this.idUsuario}`); // Assuming you have defined the route for FormsView.vue
      },
      navigateToListView() {
        this.$router.push(`/list/${this.idUsuario}`); // Assuming you have defined the route for ListView.vue
      },
      filterGroups(lista)
      {
        var respuesta = [];
        for (var i = 0; i < lista.length; i++){
          if (lista[i].profesor.id == this.idUsuario)
          {
            respuesta.push(lista[i])
          }
        }
        return respuesta;
      },
      goGrupo(id)
      {
        this.$router.push(`/stats/${this.idUsuario}/${id}`)
      }
    },
    components: {
        NavInit
    },
};
</script>


<style>
body {
  overflow-x: hidden;
  height: 100%;
  background-image: url("http://i.imgur.com/w16HASj.png");
}

.header {
  text-align: center;
  color: aquamarine;
  margin-top: -10px;
}

.card {
  background-image: url("https://i.imgur.com/uwZRmwg.png");
  color: aquamarine;
  background-size: cover;
  width: 100%;
  height: auto;
  border-radius: 20px;
  margin-top: 2.5%;
  margin-bottom: 2.5%;
  padding-top: 0px;
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
  background-color: #EA4C89;
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
  background-color: #F082AC;
}
</style>
