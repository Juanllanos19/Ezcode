<script setup>
import {ref , onMounted} from 'vue'
import axios from 'axios'

const data = ref([{
  id: "",
  tema: "",
  profesor: "",
  dificultad: "",
  titulo: "",
  contenido: "",
  tipoP: "",
  estado: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/pregunta')
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
  <div class="alert alert-primary" role="alert">
  <h3>{{ data[0].tema.tipo }}</h3>
</div>
  <div class="accordion" id="accordionExample">
      <div class="accordion-item" v-for="(accordionItem,index) in data" :key="index" v-if="data[0].tema.tipo">
        <h2 class="accordion-header">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            <strong>{{ accordionItem.titulo }}</strong>
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <strong>Profesor:</strong> {{ accordionItem.profesor.nombre + ' ' + accordionItem.profesor.apellidoPat+ ' ' + accordionItem.profesor.apellidoMat}} <br>
            <strong>Dificultad:</strong> {{ accordionItem.dificultad.rango }} <br>
            <strong>Departamento:</strong> {{ accordionItem.profesor.departamento.nombre }} <br>
            <strong>Especialidad:</strong> {{ accordionItem.profesor.especialidad }}
          </div>
        </div>
      </div>
    </div>
    <RouterView />
</template>

<script>
export default {
    name: 'AcordeonInit'
}
</script>
  
