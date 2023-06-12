<template>
    <div>
      <h2>Informe de Calificaciones</h2>
      <table class="grades-table">
        <thead>
          <tr>
            <th>Nombre del Alumno</th>
            <th>Calificación</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(alumno, index) in alumnos" :key="index">
            <td>{{ alumno.nombre }}</td>
            <td>{{ alumno.calificacion }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        alumnos: [
          { nombre: "Alumno 1", calificacion: 90 },
          { nombre: "Alumno 2", calificacion: 85 },
          { nombre: "Alumno 3", calificacion: 95 },
          // Agrega más alumnos y calificaciones según necesites
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .grades-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .grades-table th,
  .grades-table td {
    border: 1px solid #ccc;
    padding: 8px;
  }
  
  .grades-table th {
    background-color: #000;
    color: #fff;
  }
  
  .grades-table tr:nth-child(even) {
    background-color: #000;
    color: #fff;
  }
  
  .grades-table tr:nth-child(odd) {
    background-color: #000;
    color: #fff;
  }
  </style>
  
  