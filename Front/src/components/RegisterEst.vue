<template>
    <br><br><br><div class="auth-container">
      <div class="auth-content">
            <h2 class="auth-title">¡Registrate!</h2>
            <form @submit.prevent="signupE">
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
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Ingrese su correo electrónico" pattern="[Aa]\d{8}@tec\.mx" required>
                <p v-if="email && !isEmailValid" class="error-message">El formato es: AXXXXXXXX@tec.mx</p>
              </div>
              <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Ingrese su contraseña" required>
                <p v-if="password && !isPasswordValid" class="error-message">La contraseña debe tener al menos 8 caracteres y contener letras mayúsculas, minúsculas, números y símbolos.</p>
              </div>
              <div class="form-group">
                <label for="confirmPassword">Confirmar contraseña</label>
                <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" placeholder="Confirme su contraseña" required>
                <p v-if="confirmPassword && confirmPassword !== password" class="error-message">Las contraseñas no coinciden.</p>
              </div>
              <button type="submit" class="btn btn-primary">Crear cuenta</button>
            </form>
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

  export default {

    name: 'RegisterEst',

    data() {
      return {
        name: '',
        lastname: '',
        email: '',
        password: '',
        confirmPassword: '',
      };
    },

    computed: {
      isPasswordValid() {
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return passwordRegex.test(this.password);
      },

      isEmailValid() {
        const emailRegex = /^[Aa]\d{8}@tec\.mx$/;
        return emailRegex.test(this.email);
      },
    },

    methods: {

      async signupE() {

        if (this.password !== this.confirmPassword) {
          console.log('Las contraseñas no coinciden');
          return;
        }

        if (!this.isPasswordValid) {
          console.log('La contraseña no cumple con los requisitos');
          return;
        }

      },
    },
  };

</script>

<script setup>
  import {ref} from 'vue'
  import axios from 'axios'

  const name = ref();
  const lastname = ref();
  const email = ref();
  const password = ref();

  function signupP(){
    var name = {"name": name.value};
    var lastname = {"lastname": lastname.value};
    var email = {"email": email.value};
    var password = {"password": password.value};
    var headers = {'Content-Type': 'application/json'};
    axios.post('http://localhost:5173/RegisterEst', name, lastname, email, password, headers)
    .then(result => {
      console.log(result.data)
    })
    .catch(error => {
      console.log(error)
    })
  }
</script>