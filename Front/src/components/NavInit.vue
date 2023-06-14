import { RouterLink} from 'vue-router'

<template>
    <nav class="navbar navbar-expand-lg fixed-top" style="background-color: rgb(113, 132, 158);">
        <div class="container-fluid">
        <RouterLink to="/" class="navbar-brand"  style="width:15%; padding-left: 5%;"><img id="logo-navbar" src="../assets/Group190.png" style="width: auto; height: 80px;"></RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" style="padding-right: 10%; font-family: 'Russo One', sans-serif; font-size: large">
                <router-link :to="`/inicio/${this.$route.params.idUsuario}`" class="nav-link text-white" id="menu-nav">MENU</router-link>
            </li>
            <li class="nav-item" style="padding-right: 10%; font-family: 'Russo One', sans-serif; font-size: large;" >
                <router-link :to="`/desempenio/${this.$route.params.idUsuario}`" class="nav-link text-white" id="desempenio-nav" >DESEMPEÑO</router-link>
            </li>
            <li class="nav-item">
                
            </li>
            </ul>
            <span class="navbar-text" style="padding-right: 3%;">
                <RouterLink to="/" class="navbar-brand logo-text"><img id="logo-notificaciones" src="../assets/iconbell.png" style="width: 80%;"></RouterLink>
            </span>
            <span class="navbar-text" style="padding-right: 10%;">
                <div class="dropdown">
                <button class="navbar-brand" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background: transparent; width: 100%; border: transparent;">
                    <img id="logo-perfil" src="../assets/iconprofile.png" style="width: 80%;">
                </button>
                <ul class="dropdown-menu text-bg-dark" aria-labelledby="dropdownMenuButtonDark">
                    <li><a class="dropdown-item" href="#">Hola, {{ nombre }}</a></li>
                    <li><a class="dropdown-item" href="#">Configuración</a></li>
                    <li><a class="dropdown-item" @click="cerrarSesion" href="#">Cerrar sesion</a></li>
                </ul>
                </div>
            </span>
        </div>
        </div>
    </nav>
    <RouterView />
</template>

<script>
import axios from 'axios';
export default {
    name: 'NavInit',
    
    data() {
      return {
        nombre: '',
      }
    },

    methods: {
        cerrarSesion() {
            window.location.href='http://localhost:5173/';
        },
    },
    
    created() {
      const idUsuario = this.$route.params.idUsuario;

      axios.get(`http://127.0.0.1:8000/api/estudiante/${idUsuario}`)
        .then(response => {
          this.nombre = response.data.nombre;
        })
        .catch(error => {
          console.error(error);
        });
    }

}
</script>
  