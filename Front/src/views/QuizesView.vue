<script setup>
    import {ref, onMounted} from "vue"
    import axios from 'axios'
    import router from '../router';
  
    const quizes = ref([{
      id: "",
      actividad: "",
      pregunta: "",
      valor: ""
    }])
    const search = ref("")

    onMounted(
      axios.get('http://localhost:8000/api/actividaPregunta/')
      .then((result) => {
        console.log(result.data);
        quizes.value = result.data;
      })
      .catch((error) => {
        console.log(error);
      })
    )

    function goQuiz(id){
      router.push({ name: 'quiz', params: { id: id } })
    }

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
    <header>
      <NavInit />
    </header>
    <body style="padding-top: 8%;">
      <div class="container">
      <h1>Quizes</h1>
      <div class="row row-cols-2 row-cols-lg-5 g-5">
        <div class="col" v-for="(item,i) in quizes" :key="i" 
        @click="goQuiz(item.id)">
          <div class="card">
            <div class="card-header">
              <h3 class="card-title">{{ item.actividad.nombre }}</h3>
            </div>
            <div class="card-body">
              <strong>Fecha limite:</strong> {{ item.actividad.fechaInicio}} <br>
              <strong>Porcentaje:</strong> {{ item.valor}} <br>
              
            <a class="btn btn-primary" @click="goQuiz(item.id)">Manos a la obra</a>
            </div>
          </div>
        </div>
      </div>
      </div>
    </body>
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