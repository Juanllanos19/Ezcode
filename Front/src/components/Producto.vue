import { RouterLink} from 'vue-router'
<template>
    <div class="card text-center" style="color: white; background: none;">
      <div class="card-body">
        <h1 class="card-title">Tu nueva ruta hacia la programación</h1>
        <div class="card-group" style="padding-top: 2%;">
          <div class="card text-bg-primary custom-card mb-3">
            <img src="../assets/code1.jpeg" class="card-img-top" alt="..." style="height: 200px;">
            <div class="card-body">
              <p class="card-text">¡Bienvenido a EzC0de! En nuestro sitio, te ofrecemos una plataforma interactiva y desafiante para mejorar tus habilidades de programación y enfrentar problemas algorítmicos.</p>
            </div>
          </div>
          <div class="card text-bg-primary custom-card mb-3">
            <img src="../assets/code2.jpg" class="card-img-top" alt="..." style="height: 200px;">
            <div class="card-body">
              <p class="card-text">Con una amplia colección de desafíos, desde problemas sencillos hasta desafiantes, te brindamos la oportunidad de poner a prueba tus conocimientos y mejorar tus habilidades de resolución de problemas. Nuestra plataforma está diseñada para ayudarte a prepararte para entrevistas técnicas, competencias de programación y fortalecer tus habilidades de codificación.</p>
            </div>
          </div>
          <div class="card text-bg-primary custom-card mb-3" style="width: border-radius: 10px;;">
            <img src="../assets/code3.jpeg" class="card-img-top" alt="..." style="height: 200px;">
            <div class="card-body">
              <p class="card-text">Únete a nuestra comunidad de programadores entusiastas, comparte soluciones, participa en discusiones y mejora tus habilidades de resolución de problemas.</p>
            </div>
          </div>
        </div>
        <RouterLink id="producto" to="/login" class="btn btn-primary" style="margin-top: 2%; margin-bottom: 2%; font-size: large; font-family: 'Russo One', sans-serif;">Inicia tu aventura</RouterLink>
      </div>
    </div>
    <RouterView />
  </template>
  
  <style>
  .custom-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-bottom: 20px; /* Agregamos margen inferior para separar las tarjetas */
  }
  
  .card-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px; /* Agregamos espaciado entre las tarjetas */
  }
  </style>
  
  
  
  

<script>
export default {
    name: 'Producto'
}
</script>