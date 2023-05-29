<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
</script>

<script>
import NavInit from '../components/NavInit.vue'
import DesempenioView from './DesempenioView.vue';
import { VAceEditor } from 'vue3-ace-editor';


const data = ref([
        {
            titulo:"Titulo test",
            tema:"tema test",
            contenido:{}
        }
    ]);
const contenido = ref([{}])
    onMounted(
        axios.get('http://localhost:8000/api/pregunta/1/')
        .then((result) => {
            console.log(result.data);
            data.value = result.data;


            axios.get(data.value.contenido)
            .then((response) => {
                contenido.value = response.data;
                console.log(contenido.description)
            }
            ).catch((error) => {
                    console.log(error)
                })
        })
        .catch((error) => {
            console.log(error)
        }),
    )

export default {
  components: {
    NavInit,
    VAceEditor,
    DesempenioView
},
data() {
    return {
      editor: {
        value: 'print(Hello world!)'
      },
      input_editor: {
        value: '#Your inputs here!'
      }
    }
  },
  methods:{
    test(event){
        console.log("Testing")
    }
  }
}

</script>

<template>
    <div>
        <header>
            <NavInit />
        </header>
        <body style="display: flex; padding-top: 8% width: 100%;">
            <div id="compilador" style="display: flex; width: 100%;">
                <div id="description" style="width: 20%; padding-top: 8%; padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Descripcion</div>
                            <div class="card-body">
                                <h5 class="card-title">{{contenido.title}}</h5>
                                <p class="card-text">{{ contenido.description }}</p>
                                <v-ace-editor
                                v-model:value="input_editor.value"
                                @init="editorInit"
                                lang="python"
                                theme="chrome"
                                style="height: 100px" />
                            </div>
                    </div>
                </div>
                <div id="code" style="width: 50%; padding-top: 8%;padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Codigo</div>
                        <div class="card-body">
                            <h5 class="card-title">{{editor.value}}</h5>
                            <v-ace-editor
                                v-model:value="editor.value"
                                @init="editorInit"
                                lang="python"
                                theme="chrome"
                                style="height: 300px"/>
                        </div>
                    </div>
                </div>
                <div id="code" style="width: 29.5%; padding-top: 8%;padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Header</div>
                        <div class="card-body">
                            <h5 class="card-title">{{editor.value}}</h5>
                             <button type="button">Ejecutar</button> 
                              <button type="button" @click="test">Hacer pruebas</button> 

                              <h5 class="card-title" style="padding-top: 5%;">Output</h5>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        <RouterView />
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