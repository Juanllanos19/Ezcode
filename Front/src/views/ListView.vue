<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import router from '../router';

const dificultad = ref([
    {
        id: "",
        rango: ""
    }
])

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

onMounted(() => {
    axios.get('http://localhost:8000/api/dificultad/')
        .then(result => {
            console.log(result.data)
            dificultad.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
})

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
</script>

<template>
    <div>
        <header>
            <NavInit />
        </header>

        <body style="padding-top: 6%;">

            <h2>Elija las preguntas para su Actividad</h2>
            <hr><br>
            <div>
                <div class="container">
                    <div class="row">
                        <table class="table">
                            <thead class="blue-text">
                                <tr class="filters">
                                    <th>Autor
                                        <select id="autor-filter" class="form-control" v-model="filters.autor"
                                            @change="changeFilter('autor')">
                                            <option v-for="(item, i) in profesor" :key="i"> {{ item.nombre }}</option>
                                        </select>
                                    </th>
                                    <th>Tema
                                        <select id="tema-filter" class="form-control" v-model="filters.tema"
                                            @change="changeFilter('tema')">
                                            <option v-for="(item, i) in modulos" :key="i"> {{ item.tipo }}</option>

                                        </select>
                                    </th>
                                    <th>Dificultad
                                        <select id="dificultad-filter" class="form-control" v-model="filters.dificultad"
                                            @change="changeFilter('dificultad')">
                                            <option v-for="(item, i) in dificultad" :key="i"> {{ item.rango }}</option>
                                        </select>
                                    </th>
                                </tr>
                            </thead>
                        </table>

                        <div class="panel panel-primary filterable">
                            <div class="panel-heading">
                                <h3 class="panel-title">Preguntas</h3>
                                <div class="pull-right"></div>
                            </div>

                            <table id="task-list-tbl" class="table">
                                <thead>
                                    <tr class="blue-text">
                                        <th>Check</th>
                                        <th>Title</th>
                                        <th>Dificultad</th>
                                        <th>Tema</th>
                                        <th>Autor</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="color: white;" v-for="task in filteredTasks" :key="task.id"
                                        class="task-list-row" :data-task-id="task.id" :data-autor="task.autor"
                                        :data-tema="task.tema" :data-dificultad="task.dificultad">
                                        <td>
                                            <input type="checkbox" :value="task.id" v-model="selectedTasks">
                                        </td>
                                        <td>{{ task.title }}</td>
                                        <td>{{ task.dificultad }}</td>
                                        <td>{{ task.tema }}</td>
                                        <td>{{ task.autor }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="row">
                    <div class="col-md-8 cart">
                        <div class="title">
                            <div class="col">
                                <h4><b>previsualizar Actividad</b></h4>
                            </div>
                        </div>
                        <div class="row border-top border-bottom" v-for="(taskTitle, index) in selectedTaskTitles"
                            :key="index">
                            <div class="row main align-items-center">
                                <div class="col">
                                    <div class="row">{{ taskTitle }}</div>
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
                            <input placeholder="Tiutlo de la Actividad">
                        </form>
                        <button class="btn">Subir Actividad</button>
                    </div>
                </div>
            </div>
        </body>
    </div>
</template>
  
<script>
import NavInit from '../components/NavInitProf.vue'

export default {
    data() {
        return {
            filters: {
                autor: null,
                tema: null,
                dificultad: null,
            },
            tasks: [
                {
                    id: 1,
                    title: 'title 1',
                    dificultad: 'Difícil',
                    tema: 'Variables',
                    autor: 'Larry',
                },
                {
                    id: 2,
                    title: 'title 2',
                    dificultad: 'Fácil',
                    tema: 'If',
                    autor: 'Larry',
                },
                {
                    id: 3,
                    title: 'title 3',
                    dificultad: 'Normal',
                    tema: 'Arrays',
                    autor: 'Jesús',
                },
                {
                    id: 4,
                    title: 'title 4',
                    dificultad: 'Difícil',
                    tema: 'Variables',
                    autor: 'Donald',
                }
            ],
            selectedTasks: [],
            selectedTaskTitles: [],
        };
    },
    components: {
        NavInit
    },
    computed: {
        filteredTasks() {
            return this.tasks.filter(task => {
                let result = true; // not guilty until proven guilty

                Object.keys(this.filters).forEach(filter => {
                    if (
                        this.filters[filter] &&
                        this.filters[filter] !== 'None' &&
                        this.filters[filter] !== 'Any'
                    ) {
                        result = result && this.filters[filter] === task[filter];
                    }
                });

                return result;
            });
        }
    },
    methods: {
        changeFilter(filterName) {
            this.updateFilters();
        },
        updateFilters() {
            // No es necesario hacer nada aquí, ya que computed 'filteredTasks' se actualiza automáticamente
        },
        handleTaskSelection() {
            this.selectedTaskTitles = this.selectedTasks.map(taskId => {
                const task = this.tasks.find(t => t.id === taskId);
                return task ? task.title : '';
            });
        },
        subirActividad() {
            // ... lógica para subir la actividad

            // Al finalizar la subida de la actividad, actualiza el store de Vuex
            this.$store.commit('setActividad', actividad);
        },
    },
    watch: {
        selectedTasks: {
            handler: 'handleTaskSelection',
            deep: true,
        },
    },
};
</script>
  
<style>
body {
    background-image: url("http://i.imgur.com/w16HASj.png");
}

.blue-text {
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
    background-color: #1c3166;
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
    color: rgb(65, 65, 65);
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
    padding: 1.5vh 1vh;
    margin-bottom: 4vh;
    outline: none;
    width: 100%;
    background-color: rgb(247, 247, 247);
}

input {
    border: 1px solid rgba(0, 0, 0, 0.137);
    padding: 1vh;
    margin-bottom: 4vh;
    outline: none;
    width: 100%;
    background-color: rgb(247, 247, 247);
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
  