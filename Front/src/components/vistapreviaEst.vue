<template>
    <div class="auth-container">
      <div class="auth-content">
        <h1 class="title">Bienvenido {{ nombre }} a login</h1>
      </div>  
    </div>
  </template>
  
  <style>
  .auth-container {
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
      }
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

  };
  </script>
  