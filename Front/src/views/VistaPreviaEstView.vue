  <script>
  import Nav from '../components/Nav.vue'
  import Background from '../components/Background.vue'
  import VistapreviaEst from '../components/vistapreviaEst.vue';
  
  export default {
    components: {
    Nav,
    Background,
    VistapreviaEst,
}
  }
  </script>
  
  <template>
      <Background />
      <Nav />
      <VistapreviaEst />
      <RouterView />
  </template>