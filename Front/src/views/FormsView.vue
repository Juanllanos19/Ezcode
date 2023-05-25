<script setup>
import { ref } from 'vue';
import Datepicker from 'vue3-datepicker';

const selectedDate = ref('');
const reacTitle = ref('');
const selectedTheme = ref('');
const selectedDifficulty = ref('');
const author = ref('');
const ponderation = ref('');
const description = ref('');
const boxTextOut = ref([]); // Array to hold box texts
const preguntas = ref([]);
const boxTextInt = ref([]);

// Method to add a new box text
const addBoxText = () => {
  boxTextOut.value.push('');
};

// Method to delete the last box text
const deleteBoxText = () => {
  boxTextOut.value.pop();
};

const addBoxTextInt = () => {
  boxTextInt.value.push('');
};

// Method to delete the last box text
const deleteBoxTextInt = () => {
  boxTextInt.value.pop();
};

const agregarPregunta = () => {
  preguntas.value.push('');
};

// Método para eliminar la última pregunta
const eliminarPregunta = () => {
  preguntas.value.pop();
};
</script>



<template>
  <div class="wrapper">
    <!-- Sidebar  -->
    <nav id="sidebar">

      <label for="referrer"> ¿Cual es la dificultad?
        <select id="inputState" class="form-select" v-model="selectedDifficulty">
          <option selected>Choose...</option>
          <option value="1">Dificil</option>
          <option value="2">Medio</option>
          <option value="3">Facil</option>
        </select>
      </label>


      <div class="content-wrapper">
        <label for="datepicker">Fecha y hora</label>
        <datepicker v-model="selectedDate" format="yyyy-MM-dd HH:mm" :clear-button="true" :editable="false">
        </datepicker>
      </div>
      <ul class="list-unstyled components">
        <p>Reactivos</p>
        <li>
          <!-- Add multiple box texts -->
          <div v-for="(pregunta, index) in preguntas" :key="index">
            <div class="col-12">
              <a>
                <button type="button" class="btn btn-link form-label" @click="editQuestion(index)">Pregunta {{ index + 1
                }}</button>
              </a>
            </div>
          </div>
        </li>
      </ul>
      <!-- botones de añadir pregunta -->
      <div class="col-12">
        <button type="button" class="btn btn-primary" @click="agregarPregunta">Añadir</button>
        <button type="button" class="btn btn-danger" @click="eliminarPregunta">Eliminar</button>
      </div>

      <div class="col-12">
        <button type="submit" class="btn btn-primary">Guardar</button>
      </div>


    </nav>

    <!-- Page Content  -->
    <div id="content">
      <form class="row g-3 p-3">
        <div class="form-group">
          <label for="exampleInputEmail1" class="form-label">Ingresa el nombre del Reactivos</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
            placeholder="Ingresa el titulo de reactivos" v-model="reacTitle">
        </div>



        <div class="col-md-4">
          <label for="referrer"> ¿Cual es el tema?
            <select id="inputState" class="form-select" v-model="selectedTheme">
              <option selected>Choose...</option>
              <option value="1">arrays</option>
              <option value="2">if</option>
              <option value="3">whiles</option>
            </select>
          </label>
        </div>
        <p></p>

        <div class="col-md-4">
          <label for="validationDefault02" class="form-label"></label>
          <input type="text" class="form-control" id="validationDefault02" placeholder="Autor" required v-model="author">
        </div>
        <div class="col-md-4">
          <label for="validationDefaultUsername" class="form-label"></label>
          <div class="input-group">
            <span class="input-group-text" id="inputGroupPrepend2">#</span>
            <input type="number" id="replyNumber" min="0" data-bind="value:replyNumber" placeholder="Ponderacion" required
              v-model="ponderation">
          </div>
        </div>


        <div class="col-12">
          <label for="inputAddress" class="form-label"></label>
          <input type="text" class="form-control" id="inputAddress" placeholder=" Descripcion del problema"
            v-model="description">
        </div>

        <div v-for="(boxTextOut, index) in boxTextOut" :key="index">
          <div class="col-12">
            <a for="inputAddress" class="form-label">Output {{ index + 1 }}</a>
            <input type="text" class="form-control" v-model="boxText">
          </div>
        </div>

        <div class="col-12">
          <button type="button" class="btn btn-primary" @click="addBoxText">Añadir</button>
          <button type="button" class="btn btn-danger" @click="deleteBoxText">Eliminar</button>
        </div>

        <div v-for="(boxTextInt, index) in boxTextInt" :key="index">
          <div class="col-12">
            <a for="inputAddress" class="form-label">Input {{ index + 1 }}</a>
            <input type="text" class="form-control" v-model="boxText">
          </div>
        </div>

        <div class="col-12">
          <button type="button" class="btn btn-primary" @click="addBoxTextInt">Añadir</button>
          <button type="button" class="btn btn-danger" @click="deleteBoxTextInt">Eliminar</button>
        </div>


      </form>
    </div>
  </div>
</template>




<style>
body {
  align-items: center;
  min-height: 120vh;
  text-align: center;
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: center;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

form {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  min-height: 50vh;
}

p {
  font-family: 'Poppins', sans-serif;
  font-size: 1.1em;
  font-weight: 300;
  line-height: 1.7em;
  color: #999;
}

a,
a:hover,
a:focus {
  color: inherit;
  text-decoration: none;
  transition: all 0.3s;
}

/* ---------------------------------------------------
    SIDEBAR STYLE
----------------------------------------------------- */

.wrapper {
  display: flex;
  max-width: 100%;
  align-items: stretch;
}

#sidebar {
  min-width: 250px;
  max-width: 250px;
  background: #7386D5;
  color: #fff;
  transition: all 0.3s;
  
}

#sidebar .sidebar-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 120px;
  background: #6d7fcc;
}

#sidebar ul p {
  color: #fff;
  padding: 10px;
}

#sidebar ul li a {
  padding: 10px;
  font-size: 1.1em;
  display: block;
}

#sidebar ul li a:hover {
  color: #7386D5;
  background: #fff;
}

/* Custom colors */
:root {
  --primary-color: #7386D5;
  --secondary-color: #6d7fcc;
  --background-color: #95aad8;
  --text-color: #fff;
  --form-background: #000;
  --form-text-color: #fff;
}

body {
  background-color: var(--background-color);
}

#sidebar {
  background: var(--primary-color);
}

#sidebar .sidebar-header {
  background: var(--secondary-color);
}

section.container {
  background-color: var(--form-background);
  color: var(--form-text-color);
}
</style>
