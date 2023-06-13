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
              <div v-if="accordionItem1.tipo === accordionItem.tema.tipo">
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
  name: 'AcordeonInit',
  computed: {
    divVacio() {
      return this.modulos.filter(item => item.items && item.items.length > 0).length === 0;
    }
  }
}
</script>



  
