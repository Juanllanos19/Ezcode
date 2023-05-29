<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
</script>

<script>
import NavInit from '../components/NavInit.vue'

export default {
  components: {
    NavInit
  }
}
</script>

<template>
  <div>
    <header>
      <NavInit />
    </header>
    <body style="display: flex; padding-top: 6.5%;">

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
</style>