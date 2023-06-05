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
const contenido = ref([{}]);
    onMounted(
        axios.get('http://localhost:8000/api/pregunta/1/')
        .then((result) => {
            console.log(result.data);
            data.value = result.data;


            axios.get(data.value.contenido)
            .then((response) => {
                contenido.value = response.data;
                console.log(contenido.description);
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
        value: 'Your output will be generated here!'
      },
      testcases: {
        value: [],
        results: []
      },
    }
  },
  methods:{
    execute(event){
        console.log("Execute");
        this.output.value = "Loading...";

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
            //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
            'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
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
                //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
                'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
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
                    getData2();
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
        this.testcases.value = [];
        this.testcases.results = [];
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
            //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
            'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
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
                //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
                'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
                'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
            }
        };
        
        const getData = async (index) => {
            try {
                const response = await axios.request(options);
                console.log(response.data);
                options2.url= 'https://judge0-ce.p.rapidapi.com/submissions/' + response.data.token;
                getData2(index);
            } catch (error) {
                console.error(error);
            }
        };

        const getData2 = async (index) => {
            try {
                const response = await axios.request(options2);
                console.log(response.data);
                if (response.data.stdout == null)
                {
                    getData2(index);
                }
                else
                {
                    var salida = atob(response.data.stdout);
                    this.testcases.value[index] = "Output: " + salida;
                    if (salida == atob(response.data.expected_output))
                    {
                        this.testcases.results[index] = "checkmark";
                    }
                    else{
                        this.testcases.results[index] = "tacha";
                    }

                }
            } catch (error) {
                console.error(error);
            }
        };

        for (var i = 0; i < contenido.value.tests.length; i++)
        {
            options.data.stdin = btoa(contenido.value.tests[i].input);
            options.data.expected_output = btoa(contenido.value.tests[i].output);
            this.testcases.results.push(null);
            this.testcases.value.push(null);
            getData(i);
            console.log(options.data.source_code );
            console.log(atob(options.data.source_code));
        }
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
                <div id="description" style="width: 25%; padding-top: 8%; padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Descripcion</div>
                            <div class="card-body">
                                <h5 class="card-title" style="font-size: 32px;">{{contenido.title}}</h5>
                                <p class="card-text" style="font-size: 20px;">{{ contenido.description }}</p>
                                <v-ace-editor
                                v-model:value="input_editor.value"
                                @init="editorInit"
                                lang="python"
                                theme="chrome"
                                style="height: 200px; font-size: 16px;" />
                            </div>
                    </div>
                </div>
                <div id="code" style="width: 45%; padding-top: 8%;padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header" >Codigo</div>
                        <div class="card-body">
                            <h5 class="card-title" style="font-size: 26px;">Tu codigo</h5>
                            <v-ace-editor
                                v-model:value="editor.value"
                                @init="editorInit"
                                lang="python"
                                theme="chrome"
                                style="height: 500px; font-size: 16px;"/>
                        </div>
                    </div>
                </div>
                <div id="code" style="width: 29.5%; padding-top: 8%;padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Outputs</div>
                        <div class="card-body">
                            <h5 class="card-title"></h5>
                             <button type="button" class="btn btn-primary" @click="execute" style="width: 100%;">Ejecutar</button> 
                             
                              <button type="button" class="btn btn-success" @click="test" style="width: 100%; margin-top: 3%;">Hacer pruebas</button> 

                              <h5 class="card-title" style="padding-top: 5%;">Output</h5>
                              {{ output.value }}
                              <h5 class="card-title" style="padding-top: 5%;">Test cases</h5>

                            
                              <div class="accordion" id="accordionExample">
                                <template v-for="(item, index) in contenido.tests" :key="index">
                                    <div class="accordion-item">
                                        <h2 class="accordion-header" id="'#collapse'+index">
                                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse'+index" aria-expanded="false" :aria-controls="'collapse'+index">
                                                Test: {{ item.testId }}
                                                <img v-if="testcases.results[index] != null" :src="'../src/assets/' + testcases.results[index]+'.png'" style="max-width: 8%; margin-left: 75%;">
                                            </button>
                                        </h2>
                                        <div :id="'collapse'+index" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                                            <div class="accordion-body">
                                                Input: {{ item.input }}
                                                <br>
                                                Expected output: {{ item.output }}
                                                <br>
                                                {{ testcases.value[index] }}
                                            </div>
                                        </div>
                                    </div>
                                </template>
                               
                            </div>
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