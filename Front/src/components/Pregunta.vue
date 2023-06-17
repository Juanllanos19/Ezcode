
<template>
    <br><br><br><br><br><br><br><br>
    <div class="auth-container">
        <div class="auth-content">
            <h2 class="auth-title">¡Registrate!</h2>
            <form @submit.prevent="registerPregunta">
                <div class="form-group">
                    <label for="titulo">Título</label>
                    <input type="text" class="form-control" id="titulo" v-model="titulo" placeholder="Ingrese el título"
                        required>
                </div>
                <div>
                    <label for="jsonFile">Subir archivo JSON:</label>
                    <input id="jsonFile" class="form-control-file" type="file" accept=".json" @change="handleFileUpload">
                </div>
                <div class="form-group">
                    <label for="tipoP">Tipo de pregunta</label>
                    <select id="tipoP" class="form-control" v-model="tipoP" required>
                        <option value=false>Abierta</option>
                        <option value=true>Cerrada</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="estado">Estado</label>
                    <input type="checkbox" id="estado" v-model="estado">
                </div>
                <div class="form-group">
                    <label for="modulos"> ¿Cual es el tema? </label>

                    <select id="inputState" class="form-select" v-model="tema">
                        <option v-for="(item, i) in modulos" :key="i" :value="item.id"> {{ item.nombre + " " + item.tipo
                        }} </option>
                    </select> 
                </div>
                <div class="form-group">
                    <label for="dificultad">Dificultad</label>
                    <select id="inputState" class="form-select" v-model="dificultad">
                        <option v-for="(item, i) in dificultad" :key="i" :value="item.id"> {{ item.rango }}</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">Subir tarea</button>
            </form>
        </div>
    </div>
</template>


<script setup>
import { onMounted, ref } from 'vue'



function handleFileUpload(event) {
    const file = event.target.files[0]
    const reader = new FileReader()

    reader.onload = (e) => {
        const jsonData = e.target.result
        // Aquí puedes realizar cualquier acción adicional con el archivo JSON,
        // como mostrar los datos en la interfaz o enviarlos al servidor.

        // Por ejemplo, podrías asignar el contenido del archivo a las propiedades
        // del componente para mostrarlo o procesarlo más adelante.
        const parsedData = JSON.parse(jsonData)
        // Asignar los datos del archivo a las propiedades correspondientes
        title.value = parsedData.title
        author.value = parsedData.author
        // ...

        // También podrías enviar el archivo al servidor si es necesario.
        // Puedes hacer una solicitud POST al servidor con axios o cualquier otra
        // biblioteca de manejo de solicitudes HTTP.
    }

    reader.readAsText(file)
}

function agregaPreguntaCodigo() {
    var pregunta = {
        "titulo": title.value,
        "contenido": '', // Espacio para subir archivos JSON
        "tipoP": false, // Tipo de pregunta: Abierta (0) o Cerrada (1)
        "estado": false,
        "tema": null,
        "profesor": null,
        "dificultad": null
    };
    console.log(pregunta);
    axios.post('http://localhost:8000/api/pregunta/', pregunta)
        .then(response => {
            console.log('Solicitud exitosa:', response.data)
        })
        .catch(error => {
            console.error('Error al realizar la solicitud:', error)
        })
}

const modulos = ref([{
    id: "",
    nombre: "",
    tipo: ""
}])

const profesor = ref([{
    id: "",
    nombre: "",
    apellidoPat: "",
    apellidoMat: ""
}])

const dificultad = ref([
    {
        id: "",
        rango: ""
    }
])

onMounted(() => {
    axios.get('http://localhost:8000/api/tema')
        .then(result => {
            console.log(result.data);
            modulos.value = result.data;
        })
        .catch(error => {
            console.log(error);
        })
})

onMounted(() => {
    axios.get('http://localhost:8000/api/profesor/')
        .then(result => {
            console.log(result.data)
            profesor.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
})

onMounted(() => {
    axios.get('http://localhost:8000/api/dificultad/')
        .then(result => {
            console.log(result.data)
            dificultad.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
});


</script>
  
<script>
import axios from 'axios';
import router from '../router';


export default {
    methods: {
        registerPregunta(e) {
            const formData = {
                titulo: this.titulo,
                dificultad: this.dificultad,
                contenido: this.contenido, // Espacio para subir archivos JSON
                tipoP: this.tipoP, // Tipo de pregunta: Abierta (0) o Cerrada (1)
                estado: this.estado,
                tema: this.tema,
                profesor: this.profesor
            }

            axios
                .post('http://127.0.0.1:8000/api/pregunta/', formData)
                .then(response => {
                    this.$router.push({ name: 'biblio', params: { idUsuario: idUsuario } })
                    console.log('pregunta agregado:', response)
                })
                .catch(error => {
                    console.log('Error al agregar el pregunta:', error)
                })

        }
    }
}
</script>
  
<style>
/* Your component styles here */
</style>
  