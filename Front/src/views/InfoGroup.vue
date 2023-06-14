<template>
    <div>
        <h2>Grupo: {{ grupo.nombre }}</h2>
        <h3>Alumnos:</h3>
        <ul>
            <li v-for="alumno in alumnos" :key="alumno.id">{{ alumno.nombre }}</li>
        </ul>
    </div>
</template>
  
  
<script>
export default {
    props: {
        grupo: {
            type: Object,
            required: true
        },
        alumnos: {
            type: Array,
            required: true
        }
    },
    watch: {
        grupo: {
            immediate: true, // Ejecutar la función de callback inmediatamente
            handler(nuevoGrupo) {
                // Aquí puedes realizar cualquier lógica adicional necesaria
                console.log('Grupo seleccionado:', nuevoGrupo);
            }
        },
        alumnos: {
            immediate: true, // Ejecutar la función de callback inmediatamente
            handler(nuevosAlumnos) {
                // Aquí puedes realizar cualquier lógica adicional necesaria
                console.log('Alumnos del grupo:', nuevosAlumnos);
            }
        }
    }

};
</script>
