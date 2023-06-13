<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
</script>

<script>
import NavInit from '../components/NavInit.vue'
import AcordeonInit from '../components/AcordeonTareasMain.vue'
import List from '../components/List.vue'

export default {
  components: {
    NavInit,
    AcordeonInit,
    List
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body style="display: flex; padding-top: 8%;">
      <div id="tasks" style="width: 50%; padding-left: 5%; padding-right: 5%;">
          <h1 style="color: aqua; padding-top: 2%;"> Task to do</h1>
          <List />
      </div>
        <div id="acts" style="width: 50%; padding-left: 10%; padding-right: 5%;">
          <h1 style="color: aqua; padding-top: 2%;"> Modulos y actividades</h1>
            <AcordeonInit />
        </div>
    </body>
    <RouterView />
  </div>
</template>

<style>
    body{
        width: 100%;
        height: 100%;
        background-color: rgb(26, 22, 64);
        text-shadow: none;
    }
    #menu-nav{
      text-decoration: underline;
    }
    #desempenio-nav{
      text-decoration: none;
    }
</style>
