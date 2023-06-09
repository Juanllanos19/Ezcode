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
                                    <option>Facil</option>
                                    <option>Medio</option>
                                    <option>Dificil</option>
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
                                <th>Created</th>
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
                                <td>{{ task.created }}</td>
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
                    dificultad: 'Dificil',
                    tema: 'Variables',
                    autor: 'Larry',
                },
                {
                    id: 2,
                    title: 'Task title 2',
                    created: '03/14/2015',
                    dificultad: 'Facil',
                    tema: 'If',
                    autor: 'Larry',
                },
                {
                    id: 3,
                    title: 'Task title 3',
                    created: '11/16/2014',
                    dificultad: 'Facil',
                    tema: 'Arrays',
                    autor: 'Donald',
                },
                {
                    id: 4,
                    title: 'Task title 4',
                    created: '11/16/2014',
                    dificultad: 'Medio',
                    tema: 'Variables',
                    autor: 'Donald',
                }
            ],
            selectedTasks: []
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
            console.log(this.selectedTasks);// Hacer algo con las tareas seleccionadas
        }
    }
};
</script>
  
<style>
body {
    background-color: white;
}

.blue-text {
    color: white;
}

.red-text {
    color: white;
}
</style>
  