<script setup>
import NavInit from '../components/NavInitProf.vue'
import { defineProps, onMounted, ref } from 'vue'
import axios from 'axios'
import router from '../router';
import Popup from '../components/Popup.vue'

const props = defineProps(['idUsuario'])

console.log("Id del profesor es: " + props.idUsuario);


const showPopup = ref({
    exito: false,
    error: false
});

const questionType = ref('codigo')
const title = ref('')
const author = ref('')
const driver = ref('')
const description = ref('')
const selectedDifficulty = ref('')
const selectedTheme = ref('')
const inputs = ref([])
const outputs = ref([])
const answer = ref('')
const hints = ref(true)
const options = ref([
    { text: '', explanation: '', isAnswer: false },
    { text: '', explanation: '', isAnswer: false },
    { text: '', explanation: '', isAnswer: false },
    { text: '', explanation: '', isAnswer: false }
])

function summonExito(){
    showPopup.value.exito = true;
}

function summonError(){
    showPopup.value.error = true;
}

function closeError(){
    console.log("Cerrando popup");
    showPopup.value.error = false;
}

function goToMenu(){
    router.push({ path: `/biblio/${props.idUsuario}` })
}

function newQuestion(){
    window.location.reload();
}


function addInputOutput() {
    if (inputs.value.length < 4 && outputs.value.length < 4) {
        inputs.value.push('')
        outputs.value.push('')
    }
}

function generateJSON() {
    //if (questionType.value === 'codigo') {

        var questionData = {};

        if (questionType.value == "codigo")
        {
            questionData = {
                id: `TC1028_23_C_${Date.now()}`,
                author: props.idUsuario,
                title: title.value,
                description: description.value,
                topic: selectedTheme.value,
                difficulty: selectedDifficulty.value,
                driver: driver.value,
                tests: []
            }

            for (let i = 0; i < inputs.value.length; i++) 
            {
                const test = {
                    testId: (i + 1).toString(),
                    input: inputs.value[i],
                    output: outputs.value[i]
                }
                questionData.tests.push(test)
            }
        }
        else
        {
            questionData = {
                id: `TC1028_23_OM_${Date.now()}`,
                author: props.idUsuario,
                title: title.value,
                description: description.value,
                topic: selectedTheme.value,
                difficulty: selectedDifficulty.value,
                answer: answer.value,
                hints: hints.value,
                options: options.value
            }

            questionData.options[answer.value].isAnswer = true;
        }


        const jsonData = JSON.stringify(questionData, null, 2)

        const element = document.createElement('a')
        const file = new Blob([jsonData], { type: 'application/json' })
        //element.href = URL.createObjectURL(file)
        //element.download = 'question.json'


        ///Hay que agregar que la info del profe sea automatica

        /*var pregunta = {
            "titulo": title.value,
            "tema": selectedTheme.value,
            "contenido": element,
            "profesor": 1,
            "tipoP": questionType.value,
            "estado": false,
            "dificultad": selectedDifficulty.value
        };*/
        let pregunta = new FormData();
        pregunta.append("titulo", title.value);
        pregunta.append("tema", selectedTheme.value);
        pregunta.append("contenido", file);
        pregunta.append("profesor", props.idUsuario);

        if (questionType.value == "codigo")
        {
            pregunta.append("tipoP", false);
        }
        else
        {
            pregunta.append("tipoP", true);
        }
    
        pregunta.append("estado", false);
        pregunta.append("dificultad", selectedDifficulty.value);


        console.log(pregunta);
        axios.post('http://localhost:8000/api/pregunta/', pregunta, {
        headers: {"Content-Type": "multipart/form-data"},
    })
            .then(response => {
                console.log('Solicitud exitosa:', response.data),
                summonExito()
            })
            .catch(error => {
                console.error('Error al realizar la solicitud:', error),
                summonError()
            })
        document.body.appendChild(element)
        element.click()
        document.body.removeChild(element)

        //router.push('/pregu');
    /*} else if (questionType.value === 'multiple') {
        const questionData = {
            id: `TC1028_23_OM_${Date.now()}`,
            author: author.value,
            title: title.value,
            description: description.value,
            topic: selectedTheme.value,
            difficulty: selectedDifficulty.value,
            answer: answer.value,
            hints: hints.value,
            options: options.value
        }

        const jsonData = JSON.stringify(questionData, null, 2)

        const element = document.createElement('a')
        const file = new Blob([jsonData], { type: 'application/json' })
        element.href = URL.createObjectURL(file)
        element.download = 'question.json'
        document.body.appendChild(element)
        element.click()
        document.body.removeChild(element)

        router.push('/pregu');
    }*/
}

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
        "tema": selectedTheme.value,
        "contenido": description.value,
        "profesor": 1,
        "tipoP": questionType.value,
        "estado": false,
        "dificultad": selectedDifficulty.value
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

const dificultad = ref([
    {
        id: 0,
        rango: ""
    }
])

const modulos = ref([{
    id: "",
    nombre: "",
    tipo: ""
}])

onMounted(() => {
    axios.get('http://localhost:8000/api/dificultad/')
        .then(result => {
            console.log(result.data)
            dificultad.value = result.data
            console.log("PK?")
            console.log(result.data[0].pk)
        })
        .catch(error => {
            console.log(error)
        })
})

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
</script>


<template>
    <div>
        <header>
            <NavInit />
        </header>

        <body style="padding-top: 6%;">
            <Popup v-if="showPopup.exito">
                <h2>¡Se ha subido la pregunta con exito!</h2>
                <button type="button" class="btn btn-primary" @click="newQuestion" style="width: 100%; margin-top: 3%;">Subir otra pregunta</button> 
                <button type="button" class="btn btn-secondary" @click="goToMenu" style="width: 100%; margin-top: 3%;">Salir al menu</button> 
            </Popup>
            <Popup v-if="showPopup.error">
                <h2>Ha habido un error :(</h2>
                Favor de revisar bien los valores, si el problema persiste <br> 
                favor de ponerse en contacto con el administrador.
                <button type="button" class="btn btn-primary" @click="closeError()" style="width: 100%; margin-top: 3%;">Ok</button> 
            </Popup>
            <div class="container mt-5 mb-5 d-flex justify-content-center">
                <div class="card px-1 py-4">
                    <div class="card-body">
                        <h6 class="card-title mb-3">Seleccione el tipo de pregunta</h6>
                        <div class="d-flex flex-row">
                            <label class="radio mr-1">
                                <input type="radio" name="questionType" value="codigo" v-model="questionType">
                                <span><i class="fa fa-user"></i> Codigo</span>
                            </label>
                            <label class="radio">
                                <input type="radio" name="questionType" value="multiple" v-model="questionType">
                                <span><i class="fa fa-plus-circle"></i> Multiple</span>
                            </label>
                        </div>
                        <h6 class="information mt-4">Personalice la pregunta</h6>
                        <div v-if="questionType === 'codigo'">
                            <!-- Contenido para el tipo de pregunta "codigo" -->
                            <div class="row">
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <input id="titulo" class="form-control" type="text" placeholder="Titulo"
                                            v-model="title">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <div class="input-group">
                                            <input class="form-control" type="text" placeholder="Driver" v-model="driver">
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="input-group">
                                    <textarea class="form-control" aria-label="With textarea" placeholder="Descripción"
                                        v-model="description"></textarea>
                                </div>
                            </div>
                            <!-- Filtro seccion -->
                            <div class="d-flex flex-row">
                                <label for="referrer"> ¿Cual es la dificultad?
                                    <select id="inputState" class="form-select" v-model="selectedDifficulty">
                                        <option v-for="(item, i) in dificultad" :key="i" :value="item.id"> {{ item.rango }}</option>
                                    </select>
                                </label>
                                &nbsp;&nbsp;
                                <div class="col-md-4">
                                    <label for="referrer"> ¿Cual es el tema?
                                        <select id="inputState" class="form-select" v-model="selectedTheme">
                                            <option v-for="(item, i) in modulos" :key="i" :value="item.id"> {{ item.nombre + " " + item.tipo
                                            }} </option>
                                        </select>
                                    </label>
                                </div>
                            </div>
                            <div class="d-flex flex-row">
                                <div class="row">
                                    <div class="input-group mb-3" v-for="(input, index) in inputs" :key="index">
                                        <textarea class="form-control" rows="2" placeholder="Input"
                                            v-model="inputs[index]"></textarea>
                                        <textarea class="form-control" rows="2" placeholder="Output"
                                            v-model="outputs[index]"></textarea>
                                    </div>
                                    <div>
                                        <button class="btn btn-sm btn-primary ml-3"
                                            @click="addInputOutput">Agregarcaso</button>
                                    </div>
                                </div>
                            </div>
                            <div class="mt-3 d-flex justify-content-end">
                                <button class="btn btn-primary" @click="generateJSON">Subir la pregunta</button>
                            </div>
                            <div>
                                <!--<label for="jsonFile">Subir archivo JSON:</label>
                                <input id="jsonFile" class="form-control-file" type="file" accept=".json"
                                    @change="handleFileUpload"> -->
                            </div>
                        </div>
                        <div v-if="questionType === 'multiple'">
                            <!-- Contenido para el tipo de pregunta "multiple" -->
                            <div class="row">
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Titulo" v-model="title" />
                                    </div>
                                </div>
                            </div>
                            <!--
                            <div class="row">
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <div class="input-group">
                                            <input class="form-control" type="text" placeholder="Autor" v-model="author" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            -->
                            <div class="row">
                                <div class="input-group">
                                    <textarea class="form-control" aria-label="With textarea" placeholder="Descripción"
                                        v-model="description"></textarea>
                                </div>
                            </div>
                            <!-- Filtro seccion -->
                            <div class="d-flex flex-row">
                                <label for="referrer"> ¿Cual es la dificultad?
                                    <select id="inputState" class="form-select" v-model="selectedDifficulty">
                                        <option v-for="(item, i) in dificultad" :key="i" :value="item.id"> {{ item.rango }}</option>
                                    </select>
                                </label>
                                &nbsp;&nbsp;
                                <div class="col-md-4">
                                    <label for="referrer"> ¿Cual es el tema?
                                        <select id="inputState" class="form-select" v-model="selectedTheme">
                                            <option v-for="(item, i) in modulos" :key="i" :value="item.id"> {{ item.tipo }}</option>
                                        </select>
                                    </label>
                                </div>
                            </div>
                            <!-- Seleccion Input seccion -->
                            <!--
                            <div class="form-check form-switch">
                                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked
                                    v-model="hints" />
                                <label class="form-check-label" for="flexSwitchCheckChecked">Habilitar pista</label>
                            </div>-->
                            <div class="d-flex flex-row">
                                <div class="row">
                                    <h6 class="mt-4">Opciones:</h6>
                                    <div class="mb-3" v-for="(option, index) in options" :key="index">
                                        <label>Opción {{ index + 1 }}:</label>
                                        <input type="text" class="form-control" v-model="options[index].text" />
                                        <label>Explicación:</label>
                                        <input type="text" class="form-control" v-model="options[index].explanation" />
                                    </div>
                                    <div class="mb-3">
                                        <label>Respuesta correcta:</label>
                                        <select class="form-select" v-model="answer">
                                            <option v-for="(option, index) in options" :key="index" :value="index">{{
                                                option.text }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <button class="btn btn-primary" @click="generateJSON">Subir la pregunta</button>
                            <!--<div>
                                <label for="jsonFile">Subir archivo JSON:</label>
                                <input id="jsonFile" class="form-control-file" type="file" accept=".json"
                                    @change="handleFileUpload">
                            </div> -->
                        </div>
                    </div>
                </div>
            </div>
        </body>
    </div>
</template>

<!-- Style -->
<style scoped>
body {
    background-image: url("http://i.imgur.com/w16HASj.png");
}

.card {
    width: 100%;
    background-color: #fff;
    border: none;
    border-radius: 12px
}

label.radio {
    cursor: pointer;
    width: 100%
}

/* Lo de label de opciones */

label.radio {
    cursor: pointer;
    width: 100%
}

label.radio input {
    position: absolute;
    top: 0;
    left: 0;
    visibility: hidden;
    pointer-events: none
}

label.radio span {
    padding: 7px 14px;
    border: 2px solid #eee;
    display: inline-block;
    color: #000000;
    border-radius: 10px;
    width: 100%;
    height: 48px;
    line-height: 27px
}

label.radio input:checked+span {
    border-color: #00a9d4;
    background-color: #00a9d4;
    color: #fff;
    border-radius: 9px;
    height: 48px;
    line-height: 27px
}

.form-control {
    margin-top: 10px;
    height: 48px;
    border: 2px solid #eee;
    border-radius: 10px
}

.form-control:focus {
    box-shadow: none;
    border: 2px solid #00a9d4
}

.agree-text {
    font-size: 12px
}
</style>
  