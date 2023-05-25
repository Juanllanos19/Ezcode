  <script>
  import Login from '../components/Login.vue'
  import Nav from '../components/Nav.vue'
  import Background from '../components/Background.vue'
  
  export default {
    components: {
      Login,
      Nav,
      Background
    }
  }
  </script>
  
  <template>
      <Background />
      <Nav />
      <Login />
      <RouterView />
  </template>