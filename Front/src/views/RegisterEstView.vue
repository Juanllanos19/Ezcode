  <script>
  import RegisterEst from '../components/RegisterEst.vue'
  import Nav from '../components/Nav.vue'
  import Background from '../components/Background.vue'
  
  export default {
    components: {
      RegisterEst,
      Nav,
      Background
    }
  }
  </script>
  
  <template>
      <Background />
      <Nav />
      <RegisterEst />
      <RouterView />
  </template>