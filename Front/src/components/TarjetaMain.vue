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
  <div class="list-group" v-for="(item,i) in data" :key="i">
    <!-- <button type="button" class="list-group-item list-group-item-action active" aria-current="true"> -->
    <button type="button" class="list-group-item list-group-item-action">{{ item.tipo }}</button>
  </div>
</template>

<script>
export default {
    name: 'Tarjeta'
}
</script>