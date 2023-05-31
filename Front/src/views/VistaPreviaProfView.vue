  <script>
  import Nav from '../components/Nav.vue'
  import Background from '../components/Background.vue'
  import VistapreviaProf from '../components/vistapreviaProf.vue';
  
  export default {
    components: {
    Nav,
    Background,
    VistapreviaProf,
}
  }
  </script>
  
  <template>
      <Background />
      <Nav />
      <VistapreviaProf/>
      <RouterView />
  </template>