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

const modulos = ref([{
  id: "",
  nombre: "",
  tipo: ""
}])

onMounted(
  axios.get('http://localhost:8000/api/tema')
  .then((result) => {
    console.log(result.data);
    modulos.value = result.data;
  })
  .catch((error) => {
    console.log(error);
  })
)

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
  <div class="accordion" id="accordionExample">
    <div class="accordion-item" v-for="(accordionItem1, i) in modulos" :key="i">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapseOne' + i" aria-expanded="false" :aria-controls="'collapseOne' + i">
          {{ accordionItem1.tipo }}
        </button>
      </h2>
      <div :id="'collapseOne' + i" class="accordion-collapse collapse" :data-bs-parent="'#accordionExample' + i">
        <div class="accordion-body">
          <div class="accordion" :id="'accordionExample' + i">
            <div class="accordion-item" v-for="(accordionItem, index) in data" :key="index">
              <div v-if="accordionItem1.tipo == accordionItem.tema.tipo">
                <h2 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapseTwo' + i + index" aria-expanded="false" :aria-controls="'collapseTwo' + i + index">
                    <strong>{{ accordionItem.titulo}}</strong>
                  </button>
                </h2>
                <div :id="'collapseTwo' + i + index" class="accordion-collapse collapse" :data-bs-parent="'#accordionExample' + i">
                  <div class="accordion-body">
                    <strong>Profesor:</strong> {{ accordionItem.profesor.nombre + ' ' + accordionItem.profesor.apellidoPat+ ' ' + accordionItem.profesor.apellidoMat}} <br>
                    <strong>Dificultad:</strong> {{ accordionItem.dificultad.rango }} <br>
                    <strong>Especialidad:</strong> {{ accordionItem.profesor.especialidad }}
                  </div>
                </div>
              </div>
              <div v-else>
                <div class="alert alert-primary d-flex align-items-center" role="alert" style="margin-bottom: 0;">
                  <svg xmlns="http://www.w3.org/2000/svg" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:" style="width: 5%; height: auto;">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                  </svg>
                  <div>
                    No hay actividades en este modulo.
                  </div>
                </div>
              </div>
            </div>
          </div>
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
  
