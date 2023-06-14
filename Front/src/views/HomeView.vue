<script setup>
import { loadFull } from "tsparticles";

const particlesInit = async engine => {
    await loadFull(engine);
};

const particlesLoaded = async container => {
    console.log("Particles container loaded", container);
};
</script>

<script>
import Nav from '../components/Nav.vue'
import Producto from '../components/Producto.vue'
import Nosotros from '../components/Nosotros.vue'
import Background from '../components/Background.vue'

</script>

<template>
    <Nav />
    <Background />
  <div class="ezcode-logo">
    <img id="ezcode-logo-imagen" src="../assets/Group187.png" alt="">
  </div>
  <div style="width: 100%; padding-left: 20%; padding-right: 20%; padding-top: 10%;" >
    <Producto />
  </div>
  <div style="width: 100%; padding-left: 20%; padding-right: 20%; padding-top: 10%;" >
    <Nosotros />
  </div>
</template>

<style>
.ezcode-logo {
  display: flex;
  justify-content: center;
  padding-top: 10%;
  align-items: center;
}

#ezcode-logo-imagen {
  width: auto;
}

/* Responsive styles */
@media (max-width: 768px) {
  #ezcode-logo-imagen {
    width: 70%; /* Adjust the width as needed for smaller screens */
    padding-top: 18%;
  }
}

@media (max-width: 576px) {
  #ezcode-logo-imagen {
    width: 90%; /* Adjust the width as needed for even smaller screens */
    padding-top: 18%;
  }
}
</style>


