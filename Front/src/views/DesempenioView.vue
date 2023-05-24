<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import router from '../router';
</script>

<script>
import NavInit from '../components/NavInit.vue'
import WindowDesempenio from '../components/WindowDesempenio.vue'

export default {
  components: {
    NavInit,
    WindowDesempenio
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body style="display: flex; padding-top: 1%;">
        <WindowDesempenio />
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
        justify-content: center;
    }
    #desempenio-nav{
        text-decoration: underline;
    }
    #menu-nav{
        text-decoration: none;
    }
</style>