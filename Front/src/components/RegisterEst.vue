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
                <label for="lastnameP">Apellido Paterno</label>
                <input type="text" class="form-control" id="lastnameP" v-model="lastnameP" placeholder="Ingrese su apellido paterno" required>
              </div>
              <div class="form-group">
                <label for="lastnameM">Apellido Materno</label>
                <input type="text" class="form-control" id="lastnameM" v-model="lastnameM" placeholder="Ingrese su apellido materno">
              </div>
              <div class="form-group">
                <label for="carrera">Carrera</label>
                <select id="carrera" class="form-control" v-model="selectedCarrera" placeholder="Seleccione su carrera" required>
                  <option v-for="carrera in carreras" :key="carrera.id" :value="carrera.siglas">{{ carrera.siglas }}</option>
                </select>
              </div>
              <div class="form-group">
                <label for="matricula">Matricula</label>
                <input type="text" class="form-control" id="matricula" v-model="matricula" placeholder="Ingrese su matricula" required>
              </div>
              <div class="form-group">
                <label for="email">Correo electrónico</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Ingrese su correo electrónico" pattern="A\d{8}@tec\.mx" required>
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

  import axios from 'axios';

  export default {

    name: 'RegisterEst',

    data() {
      return {
        name: '',
        lastnameP: '',
        lastnameM: '',
        matricula: '',
        selectedCarrera: '',
        email: '',
        password: '',
        confirmPassword: '',
        isPasswordValid: false,
        carreras: []
      }
    },

    mounted() {
      this.obtenerCarreras();
    },

    computed: {
      isPasswordValid() {
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return passwordRegex.test(this.password);
      },
    },

    methods: {

      obtenerCarreras() {
        axios.get('http://127.0.0.1:8000/api/carrera/')
          .then(response => {
            this.carreras = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },

      signupE(e) {

        const formData = {
          name: this.name,
          lastnameP: this.lastnameP,
          lastnameM: this.lastnameM,
          matricula: this.matricula,
          selectedCarrera: this.selectedCarrera,
          email: this.email,
          password: this.password
        }

        axios
          .post('http://127.0.0.1:8000/api/estudiante/', formData)
          .then(response =>{
            this.$router.push('/login')
            console.log('Usuario agregado:', response)
          })
          .catch(error => {
            console.log('Error al agregar el usuario:', error)
          })

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