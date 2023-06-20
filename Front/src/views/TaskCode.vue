<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
const props = defineProps(['id']);
console.log("Prueba: " + props.id);
</script>

<script>
import NavInit from '../components/NavInit.vue'
import TaskCode from '../views/testView.vue'


export default {
  components: {
    NavInit,
    TaskCode
  }
}
</script>

<template>
  <div>
    <header>
    </header>
    <body>
          <TaskCode :id="id"/>
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