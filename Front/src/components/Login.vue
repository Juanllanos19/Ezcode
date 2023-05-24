<template>
    <div class="auth-container" style="background-color: #032b50;">
      <div class="auth-content">
        <transition name="slide">
          <div v-if="activeForm === 'login'" class="auth-form">
            <h2 class="auth-title">Inicio de sesión</h2>
            <form @submit.prevent="login">
              <div class="form-group">
                <label for="email">Correo electrónico</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Ingrese su correo electrónico" required>
              </div>
              <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Ingrese su contraseña" required>
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
                <label for="name">Nombre</label>
                <input type="text" class="form-control" id="name" v-model="name" placeholder="Ingrese su nombre" required>
              </div>
              <div class="form-group">
                <label for="lastname">Apellidos</label>
                <input type="text" class="form-control" id="lastname" v-model="lastname" placeholder="Ingrese sus apellidos" required>
              </div>
              <div class="form-group">
                <label for="email">Correo electrónico</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Ingrese su correo electrónico" required>
              </div>
              <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Ingrese su contraseña" required>
              </div>
              <div class="form-group">
                <label for="confirmPassword">Confirmar contraseña</label>
                <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" placeholder="Confirme su contraseña" required>
              </div>
              <button type="submit" class="btn btn-primary">Crear cuenta</button>
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
  </style>
  
  <script>
  export default {
    data() {
      return {
        activeForm: 'login',
        name: '',
        lastname: '',
        email: '',
        password: '',
        confirmPassword: '',
      };
    },
    methods: {
      signup() {
        // Lógica de registro (signup) con Django aquí
      },
      login() {
        // Lógica de login con Django aquí
      },
      switchForm() {
        if (this.activeForm === 'signup') {
          this.activeForm = 'login';
        } else {
          this.activeForm = 'signup';
        }
      },
    },
  };
  </script>
  