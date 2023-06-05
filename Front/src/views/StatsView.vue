<script setup>
    import {onMounted, ref} from 'vue'
    import axios from 'axios'
</script>

<script>
    import NavInit from '../components/NavInit.vue'
    import DesempenioView from './DesempenioView.vue';

    const dataAlumnos = ref([{}]);
    const dataActividades = ref([{}]);
    const dataCalificaciones = ref([{}]);
    const grupo = ref({
        nombre: "",
        uf: ""
    });
    //const grupoActividad = ref([{}]);
    onMounted(
        /*axios.get('http://localhost:8000/api/estudiante/')
        .then((result) => {
            console.log(result.data);
            dataAlumnos.value = result.data;
        })
        .catch((error) => {
            console.log(error)
        }),*/

        /*axios.get('http://localhost:8000/api/actividad/')
        .then((result) => {
            console.log(result.data);
            dataActividades.value = result.data;
        })
        .catch((error) => {
            console.log(error)
        }),*/


        axios.get('http://localhost:8000/api/grupo/')
        .then((result) => {
            console.log(result.data);
            grupo.value = result.data[0];
        })
        .then((result) => {
            axios.get('http://localhost:8000/api/actividaGrupo/')
            .then((result) => {
                console.log(result.data);
                //grupoActividad.value = result.data;
                dataActividades.value = filterActivities(result.data);
            })
            .catch((error) => {
                console.log(error)
            })
        })
        .then((result) => {
            axios.get('http://localhost:8000/api/estudianteGrupo/')
            .then((result) => {
                console.log(result.data);
                //grupoActividad.value = result.data;
                dataAlumnos.value = filterStudents(result.data);
            })
            .catch((error) => {
                console.log(error)
            })
        })
        .then((result) => {
            axios.get('http://localhost:8000/api/calificacion/')
            .then((result) => {
                console.log(result.data);
                //dataCalificaciones.value = result.data;
                dataCalificaciones.value = arrangeGrades(result.data);
            })
            .catch((error) => {
                console.log(error)
            })
        })
        .catch((error) => {
            console.log(error)
        })
    )

    function filterActivities(listona)
    {
        var respuesta = [];
        for (var i = 0; i < listona.length; i++)
        {
            if (listona[i].grupo.nombre == grupo.value.nombre)
            {
                respuesta.push(listona[i].actividad)
            }
        }
        return respuesta;
    }

    function filterStudents(listona)
    {
        var respuesta = [];
        for (var i = 0; i < listona.length; i++)
        {
            if (listona[i].grupo.nombre == grupo.value.nombre)
            {
                respuesta.push(listona[i].estudiante)
            }
        }
        return respuesta;
    }

    function arrangeGrades(listona)
    {
        let respuesta = {};
        for (var i = 0; i < listona.length; i++)
        {
            if (respuesta[listona[i].estudiante.matricula] == null)
            {
                respuesta[listona[i].estudiante.matricula] = {}; 
            }
            if (respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad.nombre] == null)
            {
                respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad.nombre] = 0;
            }
            respuesta[listona[i].estudiante.matricula][listona[i].actividad.actividad.nombre] += (listona[i].ponderacion / listona[i].puntosTotal) * listona[i].actividad.valor; 

        }
        console.log(respuesta);
        return respuesta;
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
                                                <td v-if="dataCalificaciones[item.matricula][act.nombre] != null" scope="col">{{ Math.round(dataCalificaciones[item.matricula][act.nombre]) }}</td>
                                                <td v-else scope="col">-</td>
                                            </template>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
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