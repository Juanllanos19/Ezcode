<template>
    <div class="auth-container">
      <div class="auth-content">
        <transition name="slide">
          <div v-if="activeForm === 'login'" class="auth-form">
            <h2 class="auth-title">Inicio de sesión</h2>
            <form @submit.prevent="login">
              <div class="form-group">
                <label for="matricula">Matricula o Nómina</label>
                <input type="text" class="form-control" id="matricula" v-model="matricula" placeholder="Ingrese su matricula o nómina" required>
              </div>
              <div class="form-group">
                <label for="contrasena">Contraseña</label>
                <input type="password" class="form-control" id="contrasena" v-model="contrasena" placeholder="Ingrese su contraseña" required>
              </div>
              <button type="submit" class="btn btn-primary">Iniciar sesión</button>
              <p class="auth-switch" @click="switchForm">¿No tienes una cuenta? ¡Registrate!</p>
            </form>
          </div>
        </transition>
  
        <transition name="slide">
          <div v-if="activeForm === 'signup'" class="auth-form">
            <h2 class="auth-title">¡Registrate!</h2>
            <form @submit.prevent="signup">
              <div class="form-group">
                <label for="btnRegProf">Si eres estudiante:</label>
                <button class="btn btn-primary" @click="redirectToRegisterEst">Estudiantes</button>
              </div><br>
              <div class="form-group">
                <label for="btnRegProf">Si eres profesorx:</label>
                <button class="btn btn-primary" @click="redirectToRegisterProf">Profesores</button>
              </div>
              <p class="auth-switch" @click="switchForm">¿Ya tienes una cuenta? Inicia sesión</p>
            </form>
          </div>
        </transition>
      </div>
    </div>
  </template>
  
<style>
  @import url('https://fonts.googleapis.com/css?family=Fira+Sans:400,500,600,700,800');
  
  .auth-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .auth-content {
    width: 350px;
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
  }
  
  .auth-title {
    text-align: center;
    color: #000;
    font-family: 'Fira Sans', sans-serif;
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .auth-form {
    margin-top: 20px;
  }
  
  .form-group {
    margin-bottom: 10px;
  }
  
  .btn-primary {
    width: 100%;
  }
  
  .auth-switch {
    text-align: center;
    color: #000;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .slide-enter-active,
  .slide-leave-active {
    transition: all 0.01s;
  }
  
  .slide-enter,
  .slide-leave-to {
    transform: translateX(100%);
    opacity: 0;
  }

  .error-message {
    color: red;
    font-size: 14px;
    margin-top: 5px;
  }
</style>
  
<script>

  import axios from 'axios';
  
  export default {

    name: 'Login',

    data() {
      return {
        activeForm: 'login',
        matricula: '',
        contrasena: '',
        departamento: '',
        carrera: '',
      };
    },

    methods: {

      redirectToRegisterProf() {
        window.location.href = 'http://localhost:5173/RegisterProf';
      },
      redirectToRegisterEst() {
        window.location.href = 'http://localhost:5173/RegisterEst';
      },

      switchForm() {
        this.activeForm = this.activeForm === 'login' ? 'signup' : 'login';
      },

      login(e) {

        const matriculaPrefix = this.matricula.charAt(0).toLowerCase();

        if (matriculaPrefix === 'a') {
          
          const formData = {
            matricula: this.matricula,
            contrasena: this.contrasena,
            carrera: 1,
          };

          axios
            .post('http://127.0.0.1:8000/api/estudiante/', formData )
            .then(response => {
              const token = response.data.auth_token;

              console.log('Inicio de sesión exitoso como estudiante.');
              this.$store.commit('setToken', token);
              axios.defaults.headers.common['Authorization'] = 'Token ' + token;
              localStorage.setItem('token', token);
              window.location.href = 'http://localhost:5173/vistapreviaEst';
            })
            .catch(error => {
              console.log('Error al iniciar sesión como alumno:', error);
            });
        } else if (matriculaPrefix === 'l') {

          const formData = {
            matricula: this.matricula,
            contrasena: this.contrasena,
            departamento: 1,
          };

          axios
            .post('http://127.0.0.1:8000/api/profesor/', formData)
            .then(response => {
              const token = response.data.auth_token;

              console.log('Inicio de sesión exitoso como profesor.');
              this.$store.commit('setToken', token);
              axios.defaults.headers.common['Authorization'] = 'Token ' + token;
              localStorage.setItem('token', token);
              window.location.href = 'http://localhost:5173/vistapreviaProf';
            })
            .catch(error => {
              console.log('Error al iniciar sesión como profesor:', error);
            });
        }
      },
    },
  };
 </script>
  