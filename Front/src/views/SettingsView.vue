<script setup>
import { ref } from 'vue'
const darkMode = ref(false);
</script>

<template>
  <div class="container py-5">
    <div class="col-lg-8">
      <div class="card mb-4">
        <div class="card-body">
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0"> ID</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">A00000000</p>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Correo</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">A00000000@example.com</p>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Tipo de usaurio</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">Alumno</p>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Contraseña</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">
                <a href="#" class="text-decoration-none">Cambiar contraseña</a>
              </p>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Modo</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
              </div>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.container.py-5 {
  margin-top: 120px;
  /* altura */
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  /* Adjust the height as needed */
}
</style>