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
        value: 'print("Hello world!")'
      },
      input_editor: {
        value: '#Your inputs here!'
      },
      output: {
        value: 'Output'
      },
    }
  },
  methods:{
    execute(event){
        console.log("Execute")

        const options = {
        method: 'POST',
        url: 'https://judge0-ce.p.rapidapi.com/submissions',
        params: {
            base64_encoded: 'true',
            fields: '*'
        },
        headers: {
            'content-type': 'application/json',
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
            'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        },
        data: {
            language_id: 92,
            source_code: btoa(this.editor.value),
            stdin: btoa(this.input_editor.value),
            redirect_stderr_to_stdout: true,
        }
        };

        const options2 = {
            method: 'GET',
            url: 'https://judge0-ce.p.rapidapi.com/submissions/2e979232-92fd-4012-97cf-3e9177257d10',
            params: {
                base64_encoded: 'true',
                fields: '*'
            },
            headers: {
                'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
                'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
            }
        };

        console.log(options);

        const getData = async () => {
            try {
                const response = await axios.request(options);
                console.log(response.data);
                options2.url= 'https://judge0-ce.p.rapidapi.com/submissions/' + response.data.token;
                getData2();
            } catch (error) {
                console.error(error);
            }
        };

        getData();



        const getData2 = async () => {
            try {
                const response = await axios.request(options2);
                console.log(response.data);
                if (response.data.stdout == null)
                {
                    //getData2();
                }
                else
                {
                    this.output.value = atob(response.data.stdout);
                }
            } catch (error) {
                console.error(error);
            }
        };

    },
    test(event){
        console.log("Testing")
        console.log(btoa(this.editor.value))
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
                             <button type="button" @click="execute" style="width: 100%;">Ejecutar</button> 
                              <button type="button" @click="test" style="width: 100%;">Hacer pruebas</button> 

                              <h5 class="card-title" style="padding-top: 5%;">Output</h5>
                              {{ output.value }}
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