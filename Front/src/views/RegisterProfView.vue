  <script>
  import RegisterProf from '../components/RegisterProf.vue'
  import Nav from '../components/Nav.vue'
  import Background from '../components/Background.vue'
  
  export default {
    components: {
      RegisterProf,
      Nav,
      Background
    }
  }
  </script>

  <template>
      <Background />
      <Nav />
      <RegisterProf />
      <RouterView />
  </template>