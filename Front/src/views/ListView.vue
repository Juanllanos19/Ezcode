<template>
    <div>
        <header>
            <NavInit />
        </header>

        <body style="padding-top: 6%;">
            <h2>{{ nombre }} elige las preguntas para su Actividad</h2>
            <div>
                <table>
                    <thead>
                        <tr>
                            <th>Check</th>
                            <th>Título</th>
                            <th>Tema</th>
                            <th>Dificultad</th>
                            <th>Profesor</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in items" :key="item.id">
                            <td>
                                <input type="checkbox" v-model="item.checked" @change="updateSelectedQuestions(item)" />
                            </td>
                            <td>{{ item.titulo }}</td>
                            <td>{{ item.tema }}</td>
                            <td>{{ item.dificultad }}</td>
                            <td>{{ item.nombreProfesor }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="card">
                <div class="row">
                    <div class="col-md-8 cart">
                        <div class="title">
                            <div class="row">
                                <div class="col">
                                    <h4><b>Previsualizador de Actividad</b></h4>
                                </div>
                            </div>
                        </div>
                        <div class="row border-top border-bottom" v-for="(task, index) in selectedTasks" :key="index">
                            <div class="row main align-items-center">
                                <div class="col">
                                    <div class="row">{{ task.titulo }}</div>
                                </div>
                                <div class="col">
                                    <input type="number" id="typeNumber" class="form-control-sm" placeholder="0.0" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 summary">
                        <div>
                            <h5><b>Configuración</b></h5>
                        </div>
                        <hr>
                        <form>
                            <p>Tiempo Limite</p>
                            <input type="date" id="date" placeholder="Select a date">
                            <input type="time" id="time" placeholder="Select a time">
                            <p>Titulo</p>
                            <input placeholder="Titulo de la Actividad">
                            <p>Grupo</p>
                            <select id="grupo-filter" class="form-control" v-model="selectedGroupId">
                                <option v-for="(item, i) in selectedGroup" :key="i">{{ item.nombre }}</option>
                            </select>

                        </form>
                        <button class="btn">Subir Actividad</button>
                    </div>
                </div>
            </div>
        </body>
    </div>
</template>
  
<script setup>
import { onMounted, ref, defineProps } from 'vue';
import axios from 'axios';
import NavInit from '../components/NavInitProf.vue';

const items = ref([]);
const selectedTasks = ref([]); // Tareas seleccionadas en la card
const nombre = ref(null);
const selectedGroup = ref(''); // Grupo seleccionado en el formulario


onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/pregunta/')
        .then(result => {
            const data = result.data.map(item => ({
                titulo: item.titulo,
                dificultad: item.dificultad.rango,
                tema: item.tema.tipo,
                nombreProfesor: item.profesor.nombre,
                checked: false, // Agregamos la propiedad "checked" a cada pregunta
            }));
            items.value = data;
        })
        .catch(error => {
            console.log(error);
        });
});

onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/grupo/')
        .then(result => {
            console.log(result.data)
            selectedGroup.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
})

const { idUsuario } = defineProps(['idUsuario']);

axios.get(`http://127.0.0.1:8000/api/profesor/${idUsuario}`)
    .then(response => {
        nombre.value = response.data.nombre;
    })
    .catch(error => {
        console.error(error);
    });

function updateSelectedQuestions(item) {
    if (item.checked) {
        selectedTasks.value.push(item);
    } else {
        const index = selectedTasks.value.findIndex(task => task.id === item.id);
        if (index !== -1) {
            selectedTasks.value.splice(index, 1);
        }
    }
}
</script>
  
  

<style scoped>
body {
    background-image: url("http://i.imgur.com/w16HASj.png");
    color: white;
}

.blue-text {
    color: white;
}

h2 {
    color: white;
}

.red-text {
    color: white;
}

.title {
    margin-bottom: 5vh;
}

.card {
    margin: auto;
    max-width: 950px;
    width: 90%;
    box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius: 1rem;
    border: transparent;
}

@media(max-width:767px) {
    .card {
        margin: 3vh auto;
    }
}

.cart {
    background-color: #44749d;
    padding: 4vh 5vh;
    border-bottom-left-radius: 1rem;
    border-top-left-radius: 1rem;
}

@media(max-width:767px) {
    .cart {
        padding: 4vh;
        border-bottom-left-radius: unset;
        border-top-right-radius: 1rem;
    }
}

.summary {
    background-color: #00a9d4;
    border-top-right-radius: 1rem;
    border-bottom-right-radius: 1rem;
    padding: 4vh;
    color: white;
}

@media(max-width:767px) {
    .summary {
        border-top-right-radius: unset;
        border-bottom-left-radius: 1rem;
    }
}

.summary .col-2 {
    padding: 0;
}

.summary .col-10 {
    padding: 0;
}

.row {
    margin: 0;
    color: white;
}

.title b {
    font-size: 1.5rem;
}

.main {
    margin: 0;
    padding: 2vh 0;
    width: 100%;
}

.col-2,
.col {
    padding: 0 1vh;
}

a {
    padding: 0 1vh;
}

.close {
    margin-left: auto;
    font-size: 0.7rem;
}

img {
    width: 3.5rem;
}

.back-to-shop {
    margin-top: 4.5rem;
}

h5 {
    margin-top: 4vh;
}

hr {
    margin-top: 1.25rem;
}

form {
    padding: 2vh 0;
}

select {
    border: 1px solid rgba(0, 0, 0, 0.137);
    padding: 1vh 1vh;
    margin-bottom: 4vh;
    outline: none;
    width: 100%;
    background-color: #44749d;
}

input {
    border: 1px solid rgba(0, 0, 0, 0.137);
    padding: 1vh;
    margin-bottom: 4vh;
    outline: none;
    width: 100%;
    background-color: #44749d;
}

input:focus::-webkit-input-placeholder {
    color: transparent;
}

.btn {
    background-color: #000;
    border-color: #000;
    color: white;
    width: 100%;
    font-size: 0.7rem;
    margin-top: 4vh;
    padding: 1vh;
    border-radius: 0;
}

.btn:focus {
    box-shadow: none;
    outline: none;
    box-shadow: none;
    color: white;
    -webkit-box-shadow: none;
    transition: none;
}

.btn:hover {
    color: white;
}

a {
    color: black;
}

a:hover {
    color: black;
    text-decoration: none;
}

#code {
    background-image: linear-gradient(to left, rgba(255, 255, 255, 0.253), rgba(255, 255, 255, 0.185)), url("https://img.icons8.com/small/16/000000/long-arrow-right.png");
    background-repeat: no-repeat;
    background-position-x: 95%;
    background-position-y: center;
}
</style>
  