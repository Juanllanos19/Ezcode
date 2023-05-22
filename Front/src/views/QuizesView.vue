<script setup>
    import {ref, onMounted} from "vue"
    import axios from 'axios'
    import router from '../router';
  
    const quizes = ref([{
      id: "",
      valor: "",
      actividad: [{}],
      pregunta: [{}],
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

  <template>
    <div class="container">
      <h1>Quizes</h1>
      <div class="row row-cols-2 row-cols-lg-5 g-5">
        <div class="col" v-for="(item,i) in quizes" :key="i" 
        @click="goQuiz(item.id)">
          <div class="card h-100">
            <div class="card-body">
            <h5 class="card-title">{{ item.pregunta[0].titulo }}</h5>
            <a href="#" class="btn btn-primary">Go to quiz</a>
          </div>
        </div>
      </div>
    </div>
    </div>
  </template>