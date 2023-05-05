<script setup>
    import{ref} from 'vue'
    const data = ref([
        {
            Fecha: "12 de enero de 1990",
            nombre: "Dante",
            apellido: "Alighieri",
            portada: "/src/assets/img03.jpg"
        },
        {
            Fecha: "13 de enero de 1990",
            nombre: "Antoinie",
            apellido: "Griezman",
            portada: "/src/assets/img04.jpg"
        }
    ])
</script>

<template>
    <div class="container">
      <h1>Autores</h1>
      <table class="table">
        <thead>
          <tr>
            <th>Portada</th>
            <th>Nombre y Apellido</th>
            <th>Fecha</th>
            <th>Información Adicional</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in data" :key="i">
            <td>
              <img :src="item.portada" alt="Portada del libro">
            </td>
            <td>{{ item.nombre }} {{ item.apellido }}</td>
            <td>{{ item.Fecha }}</td>
            <td>
              <a href="#" class="btn btn-primary">Más info</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  