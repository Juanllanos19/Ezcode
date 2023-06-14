<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
const props = defineProps(['id'])
</script>

<script>
import NavInit from '../components/NavInit.vue'
import TaskMultiple from '../components/Task.vue'


export default {
  components: {
    NavInit,
    TaskMultiple
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body>
          <TaskMultiple :id="id"/>
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