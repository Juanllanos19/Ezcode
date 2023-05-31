<template>
    <div class="container">
      <h1 class="title">Bienvenido {{ nombre }}</h1>
    </div>
  </template>
  
  <style>
  .container {
    width: 250px;
    height: 350px;
    background-color: #f30000;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .title {
    font-size: 32px;
    text-align: center;
  }
  </style>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'VistaPreviaEst',
    data() {
      return {
        nombre: '',
      };
    },
    mounted() {
      this.getNombreUsuario();
    },
    methods: {
      getNombreUsuario() {
        axios.get('http://127.0.0.1:8000/api/estudiante/')
          .then(response => {
            this.nombre = response.data.nombre;
          })
          .catch(error => {
            console.log('Error al obtener el nombre del usuario:', error);
          });
      },
    },
  };
  </script>
  