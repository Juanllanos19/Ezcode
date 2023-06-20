

<script>
    import NavInit from '../components/NavInitProf.vue'
    import DesempenioView from './DesempenioView.vue';
    import {onMounted, ref} from 'vue'
    import axios from 'axios'
    import Chart from 'chart.js/auto'

    

    const baseUrl = "http://127.0.0.1:8000";



    import {
        Chart as ChartJS,
        CategoryScale,
        LinearScale,
        PointElement,
        LineElement,
        Title,
        Tooltip,
        Legend
    } from 'chart.js'
    import { Line } from 'vue-chartjs'


        





    function loadLabels(lista)
    {
        console.log("tratando de cargar grafica");
        console.log(lista.length);
        //data.labels = [];
        for (var i = 0; i < lista.length; i++)
        {
            data.labels.push(lista[i].nombre)
        }
    };



    

    export default {
        name: 'Stats',
        props: ['idUsuario','idGrupo'],
        components: {
            Line,
            NavInit
        },
        data() {
            return{
                dataAlumnos: [{matricula: "a00830026"}],
                dataActividades: [{id: 2}],
                dataCalificaciones: [{'a00830026': {0: null}}],
                grupo: {
                    uf: {siglas: "hjm,"},
                    nombre: "esperando respuesta"
                },
                data: {},
                options: {}
            };
        },
        methods: {
        filterActivities(listona)
        {
            var respuesta = [];
            for (var i = 0; i < listona.length; i++)
            {
                if (listona[i].grupo.id == this.idGrupo)
                {
                    respuesta.push(listona[i].actividad)
                }
            }
            return respuesta;
        },
        filterStudents(listona)
        {
            var respuesta = [];
            for (var i = 0; i < listona.length; i++)
            {
                if (listona[i].grupo.id == this.idGrupo)
                {
                    respuesta.push(listona[i].estudiante);
                }
            }
            console.log("Estudiantes: ", respuesta)
            return respuesta;
        },
        arrangeGrades(listona)
        {
            let respuesta = {};
            for (var i = 0; i < this.dataAlumnos.length; i++)
            {
                respuesta[this.dataAlumnos[i].matricula] = {};  
            }
            console.log("Respuesta interina", respuesta);
            for (var i = 0; i < listona.length; i++)
            {
                console.log(i);
                console.log(listona[i]);
                if (respuesta[listona[i].estudiante.matricula] != null)
                {
                    if (respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad] == null)
                    {
                        respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad] = 0;
                    }

                    respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad] += (listona[i].ponderacion / listona[i].puntosTotal) * listona[i].actividad.valor; 
                }
            
                
            }
            return respuesta;
        },
        loadGraph(calif, acti)
        {
            console.log("cali");
            console.log(calif);
            console.log("acti");
            console.log(acti)
            for (var i = 0; i < acti.length; i++)
            {
                this.data.labels.push(acti[i].nombre);
            }

            for (let matricula in calif)
            {
                var values = [];
                for (var i = 0; i < acti.length; i++)
                {
                    values.push(calif[matricula][acti[i].id]);
                }
                this.data.datasets.push({
                    label: matricula,
                    //backgroundColor: '',
                    data: values
                })
            }
        }
        },
        created(){
            console.log("Grupo Id= ", this.idGrupo);

            this.data = {
                labels: [],
                datasets: [

                ]
            }

            this.options = {
                responsive: true,
                maintainAspectRatio: true
            }

            ChartJS.register(
                CategoryScale,
                LinearScale,
                PointElement,
                LineElement,
                Title,
                Tooltip,
                Legend
            )
            this.grupo = {
                uf: {siglas: "hjm,"},
                nombre: "esperando respuesta"
            };
            axios.get('http://localhost:8000/api/grupo/' + this.idGrupo)
            .then((result) => {
                console.log("grupoimportado");
                this.grupo = result.data;
                console.log("Grupo: ", this.grupo);
                axios.get('http://localhost:8000/api/actividaGrupo/')
                .then((result) => {
                    console.log("actividadGrupo importado");
                    //grupoActividad.value = result.data;
                    this.dataActividades = this.filterActivities(result.data);

                    axios.get('http://localhost:8000/api/estudianteGrupo/')
                    .then((result) => {
                        console.log("estudianteGrupo imported");
                        //grupoActividad.value = result.data;
                        this.dataAlumnos = this.filterStudents(result.data);
                        console.log("Alumnos v1.5", result.data);
                        console.log("Alumnos v2", this.dataAlumnos);

                        axios.get('http://localhost:8000/api/calificacion/')
                        .then((result) => {
                            console.log("calificacion importado");
                            console.log(result.data);
                            //dataCalificaciones.value = result.data;
                            this.dataCalificaciones = this.arrangeGrades(result.data);
                            console.log("Estudiantes: ", this.dataAlumnos);
                            console.log("Calis: ", this.dataCalificaciones);
                            console.log("Act: ", this.dataActividades);
                            this.loadGraph(this.dataCalificaciones, this.dataActividades);
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                })
                .catch((error) => {
                    console.log(error)
                })
            })
            .catch((error) => {
                console.log(error)
            })
        },
    }
</script>



<template>
    <div>
        <header>
            <NavInit />
        </header>
        <body style="display: flex; padding-top: 8% width: 100%;">
            <div id="compilador" style="display: flex; width: 100%;">
                <div id="description" style="width: 100%; padding-top: 8%; padding-left: 0.5%; padding-right: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Descripcion</div>
                            <div class="card-body">
                                <h5 class="card-title" style="font-size: 32px;">{{grupo.uf.siglas + ': ' + grupo.nombre}}</h5>
                                <table class="table table">
                                    <thead>
                                        <tr>
                                        <th scope="col">Matricula</th>
                                        <th scope="col">Nombre</th>
                                        <template v-for="(item, index) in dataActividades" :key="index">
                                            <th scope="col">{{ item.nombre }}</th>
                                        </template>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <template v-for="(item, index) in dataAlumnos" :key="index">
                                            <tr>
                                            <th scope="row">{{item.matricula}}</th>
                                            <td>{{item.nombre + ' ' + item.apellidoPat + ' ' + item.apellidoMat}}</td>
                                            <template v-for="(act, index2) in dataActividades" :key="index2">
                                                <td v-if="dataCalificaciones[item.matricula][act.id] != null" scope="col">{{ Math.round(dataCalificaciones[item.matricula][act.id]) }}</td>
                                                <td v-else scope="col">-</td>
                                            </template>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>
            
                        <div class="card" style="width: 100%; margin-top: 2%;">
                            <div class="card-header">Grafica calificaciones alumnos</div>
                            <div class="card-body" style="width: 90%; align-self: center;">
                                <Line :data="data" :options="options" />
                            </div>
                        </div>
                        
                </div>
            </div>
        </body>
    </div>





</template>

<style>
    body{
        width: 100%;
        height: 100%;
        background-color: rgb(26, 22, 64);
        text-shadow: none;
    }
</style>