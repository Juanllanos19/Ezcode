<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
</script>

<script>
import NavInit from '../components/NavInit.vue'
import AcordeonInit from '../components/AcordeonTareasMain.vue'

export default {
  components: {
    NavInit,
    AcordeonInit
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body>
      <div id="modulosandtasks" style="width: 60%;">
        <div class="modulos">
          
        </div>
        <div id="tasks" style="width: 100%; padding-left: 5%; padding-right: 5%;">
          <AcordeonInit />
        </div>
      </div>
      <div id="acts">

      </div>
    </body>
    <!-- <RouterView /> -->
  </div>
</template>

<style>
    body{
        width: 100%;
        height: 100%;
        background-color: rgb(26, 22, 64);
        text-shadow: none;
    }
</style>
