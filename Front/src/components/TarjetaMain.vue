<script setup>
import {ref , onMounted} from 'vue'
import axios from 'axios'
import router from '../router';

const data = ref([{
  id: "",
  nombre: "",
  tipo: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/tema')
  .then((result) => {
    console.log(result.data);
    data.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

</script>

<template>
    <div class="row row-cols-2 row-cols-lg-2 g-1">
    <div style="padding-bottom: 1%;" class="col" v-for="(item,i) in data" :key="i" >
        <div class="card overflow-auto" >
        <div class="card-body" style="width: 100%;">
            <p class="card-text" style="text-align: center;">{{ item.tipo }}</p>
        </div>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'Tarjeta'
}
</script>