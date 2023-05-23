<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>
<script>
import Nav from './components/Nav.vue'

export default {
  components: {
    Nav
  }
}
</script>

<template>
  <div id="app">
    <header>
      <!-- <Nav /> -->
    </header>
    <RouterView />
  </div>
</template>