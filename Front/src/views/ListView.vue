<template>
    <div>
        <h2>Testing Task List Filters</h2>
        <hr><br>
        <div class="container">
            <div class="row">
                <table class="table">
                    <thead class="blue-text">
                        <tr class="filters">
                            <th>Autor
                                <select id="autor-filter" class="form-control" v-model="filters.autor"
                                    @change="changeFilter('autor')">
                                    <option>None</option>
                                    <option>Larry</option>
                                    <option>Donald</option>
                                    <option>Roger</option>
                                </select>
                            </th>
                            <th>Tema
                                <select id="tema-filter" class="form-control" v-model="filters.tema"
                                    @change="changeFilter('tema')">
                                    <option>None</option>
                                    <option>If</option>
                                    <option>Arrays</option>
                                    <option>Variables</option>
                                </select>
                            </th>
                            <th>Dificultad
                                <select id="dificultad-filter" class="form-control" v-model="filters.dificultad"
                                    @change="changeFilter('dificultad')">
                                    <option>Any</option>
                                    <option>Difícil</option>
                                    <option>Normal</option>
                                    <option>Fácil</option>
                                </select>
                            </th>
                        </tr>
                    </thead>
                </table>

                <div class="panel panel-primary filterable">
                    <div class="panel-heading">
                        <h3 class="panel-title">Tasks</h3>
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
                            <tr style="color: white;" v-for="task in filteredTasks" :key="task.id" class="task-list-row"
                                :data-task-id="task.id" :data-autor="task.autor" :data-tema="task.tema"
                                :data-dificultad="task.dificultad">
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
                <div class="row border-top border-bottom" v-for="(taskTitle, index) in selectedTaskTitles" :key="index">
                    <div class="row main align-items-center">
                        <div class="col">
                            <div class="row">{{ taskTitle }}</div>
                        </div>
                        <div class="col">
                            <input type="number" id="typeNumber" class="form-control-sm" placeholder="0.0" />
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="row main align-items-center">
                        <div class="col">
                            <div class="row">TaskTit</div>
                        </div>
                        <div class="col">
                            <input type="number" class="form-control-sm" placeholder="0.0" />
                        </div>
                    </div>
                </div>
                <div class="row border-top border-bottom">
                    <div class="row main align-items-center">
                        <div class="col">
                            <div class="row">TaskTit</div>
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
                </form>
                <button class="btn">Subir Actividad</button>
            </div>
        </div>
    </div>
</template>
  
<script>
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
                    title: 'Task title 1',
                    created: '01/24/2015',
                    dificultad: 'Difícil',
                    tema: 'Variables',
                    autor: 'Larry',
                },
                {
                    id: 2,
                    title: 'Task title 2',
                    created: '03/14/2015',
                    dificultad: 'Fácil',
                    tema: 'If',
                    autor: 'Larry',
                },
                {
                    id: 3,
                    title: 'Task title 3',
                    created: '11/16/2014',
                    dificultad: 'Normal',
                    tema: 'Arrays',
                    autor: 'Donald',
                },
                {
                    id: 4,
                    title: 'Task title 4',
                    created: '11/16/2014',
                    dificultad: 'Difícil',
                    tema: 'Variables',
                    autor: 'Donald',
                }
            ],
            selectedTasks: [],
            selectedTaskTitles: [],
        };
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
    background-color: #4d4242;
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
    background-color: #bc7272;
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
    -webkit-user-select: none;
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
  