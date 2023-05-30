<template>
    <br><br><br><div class="auth-container">
      <div class="auth-content">
            <h2 class="auth-title">¡Registrate!</h2>
            <form @submit.prevent="signupE">
              <div class="form-group">
                <label for="nombre">Nombre</label>
                <input type="text" class="form-control" id="nombre" v-model="nombre" placeholder="Ingrese su nombre" required>
              </div>
              <div class="form-group">
                <label for="apellidoPat">Apellido Paterno</label>
                <input type="text" class="form-control" id="apellidoPat" v-model="apellidoPat" placeholder="Ingrese su apellido paterno" required>
              </div>
              <div class="form-group">
                <label for="apellidoMat">Apellido Materno</label>
                <input type="text" class="form-control" id="apellidoMat" v-model="apellidoMat" placeholder="Ingrese su apellido materno">
              </div>
              <div class="form-group">
                <label for="carrera">Carrera</label>
                <select id="carrera" class="form-control" v-model="carrera" placeholder="Seleccione su carrera" required>
                  <option v-for="carrera in carreras" :key="carrera.id" :value="carrera.id">{{ carrera.siglas }}</option>
                </select>
              </div>
              <div class="form-group">
                <label for="matricula">Matricula</label>
                <input type="text" class="form-control" id="matricula" v-model="matricula" placeholder="Ingrese su matricula" required>
              </div>
              <div class="form-group">
                <label for="correo">Correo electrónico</label>
                <input type="email" class="form-control" id="correo" v-model="correo" placeholder="Ingrese su correo electrónico" pattern="A\d{8}@tec\.mx" required>
              </div>
              <div class="form-group">
                <label for="contrasena">Contraseña</label>
                <input type="password" class="form-control" id="contrasena" v-model="contrasena" placeholder="Ingrese su contraseña" required>
                <p v-if="contrasena && !isPasswordValid" class="error-message">La contraseña debe tener al menos 8 caracteres y contener letras mayúsculas, minúsculas, números y símbolos.</p>
              </div>
              <div class="form-group">
                <label for="confirmPassword">Confirmar contraseña</label>
                <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" placeholder="Confirme su contraseña" required>
                <p v-if="confirmPassword && confirmPassword !== contrasena" class="error-message">Las contraseñas no coinciden.</p>
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
        nombre: '',
        apellidoPat: '',
        apellidoMat: '',
        matricula: '',
        carrera: '',
        correo: '',
        contrasena: '',
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
        return passwordRegex.test(this.contrasena);
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
          nombre: this.nombre,
          apellidoPat: this.apellidoPat,
          apellidoMat: this.apellidoMat,
          matricula: this.matricula,
          carrera: this.carrera,
          correo: this.correo,
          contrasena: this.contrasena
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