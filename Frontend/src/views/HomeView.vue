<script setup>

</script>

<template>
  <body>
    <!-- MENU START  -->
    <nav class="navbar navbar-expand-lg navbar-dark">
      <!-- NAV CONTAINER START -->
      <div class="container-fluid">
        <a href="" class="navbar-brand text-info fw-semibold fs-4">Pregunta</a>

        <!-- NAV BUTTON  -->
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#menuLateral">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- OFFCANVAS MAIN CONTAINER START -->
        <section class="offcanvas offcanvas-start" id="menuLateral" tabindex="-1">
          <div class="offcanvas-header" data-bs-theme="dark">
            <h5 class="offcanvas-title text-info">Lista de preguntas</h5>
            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="offcanvas"></button>
          </div>
          <!-- OFF CANVAS MENU LINKS  START-->
          <div class="offcanvas-body d-flex flex-column justify-content-between px-0">
            <ul class="navbar-nav fs-5 justify-content-evenly">
              <li class="nav-item p-3 py-md-1">
                <a href="" class="nav-link">Pregunta 1</a>
              </li>
              <li class="nav-item p-3 py-md-1">
                <a href="" class="nav-link">Pregunta 2</a>
              </li>
              <li class="nav-item p-3 py-md-1">
                <a href="" class="nav-link">Pregunta 3</a>
              </li>
              <li class="nav-item p-3 py-md-1">
                <a href="" class="nav-link">Pregunta 4</a>
              </li>
              <!-- <div>
                <div v-for="(textbox, index) in textboxes" :key="index">
                  <input v-model="textbox.value" />
                  <button @click="removeTextbox(index)">Borrar</button>
                </div>
                <button @click="addTextbox">añadir</button>
              </div> -->
            </ul>
            <!-- enlaces redes sociales -->

            <div class="d-lg-none align-self-center py-3">
              <a href=""><i class="bi bi-twitter px-2 text-info fs-2"></i></a>
              <a href=""><i class="bi bi-facebook px-2 text-info fs-2"></i></a>
              <a href=""><i class="bi bi-github px-2 text-info fs-2"></i></a>
              <a href=""><i class="bi bi-whatsapp px-2 text-info fs-2"></i></a>
            </div>
          </div>
        </section>
        <!-- OFFCANVAS MAIN CONTAINER END  -->
      </div>
    </nav>
  </body>
<h3>personaliza la pregunta</h3>
  <!--align-items: center; justify-content: center; display: flex;-->
  <div class="mx-auto col-5" style="margin-top: 10rem; min-height: 100vh; display: flex; flex-direction: column; gap: 30px;">
      <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
        <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
        <label class="btn btn-outline-primary" for="btnradio1"> Code </label>

        <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
        <label class="btn btn-outline-primary" for="btnradio2"> Multiple </label>
      </div>


    <!-- Single button Dropdowns-->
    <div class="btn-group">
      <div class="dropdown ">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          Tema
        </button>
        <ul class="dropdown-menu">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
            <label class="form-check-label" for="flexRadioDefault1">
              Array
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
            <label class="form-check-label" for="flexRadioDefault2">
              Funtion
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
            <label class="form-check-label" for="flexRadioDefault2">
              Variables
            </label>
          </div>
        </ul>
      </div>
      <!-- Single button Dropdowns-->
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          Dificultad
        </button>
        <ul class="dropdown-menu">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
            <label class="form-check-label" for="flexRadioDefault1">
              Facil
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
            <label class="form-check-label" for="flexRadioDefault2">
              Intermedio
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
            <label class="form-check-label" for="flexRadioDefault2">
              Dificil
            </label>
          </div>
        </ul>
      </div>
    </div>
    <h1 class="text-center mb-3 text-secondary">fecha límite</h1>
    <form>
      <input class="form-control" type="datetime-local" placeholder="Dia limite">
    </form>
    <!-- Text box -->
    <div class="inputbox">
      <input type="text" required="required">
      <span>Titulo</span>
      <input type="text" required="required">
      <span>Autor</span>
      <input type="number" placeholder="1.0" step="0.01" min="0" max="10" />
      <span>Puntaje</span>
    </div>
    <div class="expanding-text-input">
      <textarea id="input" rows="1" placeholder="Describa el problema..."></textarea>
    </div>
    <div>
      <h2>Ingresa los test cases</h2>
      <div v-for="(textbox, index) in textboxes" :key="index">
        <input v-model="textbox.value" />
        <button @click="removeTextbox(index)">Borrar</button>
      </div>
      <button @click="addTextbox">añadir</button>
    </div>
    <button>Guardar</button>
  </div>
</template>



<!-- Scrip of the text box add -->
<script>
export default {
  data() {
    return {
      textboxes: [{ value: '' }]
    }
  },
  methods: {
    addTextbox() {
      this.textboxes.push({ value: '' })
    },
    removeTextbox(index) {
      this.textboxes.splice(index, 1)
    }
  }
}
</script>


<!-- Style of the canvas  -->
<style>
nav,
.offcanvas {
  background-color: #1e293b;
}

.navbar-toggler {
  border: none;
}

.navbar-toggler:focus {
  outline: none;
  box-shadow: none;
}

@media (max-width: 768px) {
  .navbar-nav>li:hover {
    background-color: #0dcaf0;
  }
}

.inputbox input {
  width: 100%;

  padding: 10px;
  border: 1px solid rgba(80, 77, 77, 0.25);
  border-radius: 5px;
  font-size: 1em;
}

.inputbox span {
  position: absolute;
  left: 100;
  /* padding: 10px; */
}
</style>
