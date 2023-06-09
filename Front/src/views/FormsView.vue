<template>
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
                                <input class="form-control" type="text" placeholder="Titulo" v-model="title">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <div class="input-group">
                                    <input class="form-control" type="text" placeholder="Autor" v-model="author">
                                </div>
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
                                <option selected>Choose...</option>
                                <option value="Difícil">Dificil</option>
                                <option value="Medio">Medio</option>
                                <option value="Fácil">Facil</option>
                            </select>
                        </label>
                        &nbsp;&nbsp;
                        <div class="col-md-4">
                            <label for="referrer"> ¿Cual es el tema?
                                <select id="inputState" class="form-select" v-model="selectedTheme">
                                    <option selected>Choose...</option>
                                    <option value="arrays">arrays</option>
                                    <option value="if">if</option>
                                    <option value="whiles">whiles</option>
                                </select>
                            </label>
                        </div>
                    </div>
                    <div class="d-flex flex-row">
                        <div class="row">
                            <div class="input-group mb-3" v-for="(input, index) in inputs" :key="index">
                                <input type="text" class="form-control" placeholder="Input" v-model="inputs[index]">
                                <input type="text" class="form-control" placeholder="Output" v-model="outputs[index]">
                            </div>
                            <div>
                                <button class="btn btn-sm btn-primary ml-3" @click="addInputOutput">Agregar caso</button>
                            </div>
                        </div>
                    </div>
                    <div class="mt-3 d-flex justify-content-end">
                        <button class="btn btn-primary" @click="generateJSON">Generar JSON</button>
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
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <div class="input-group">
                                    <input class="form-control" type="text" placeholder="Autor" v-model="author" />
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
                                <option selected>Choose...</option>
                                <option value="Difícil">Dificil</option>
                                <option value="Medio">Medio</option>
                                <option value="Fácil">Facil</option>
                            </select>
                        </label>
                        &nbsp;&nbsp;
                        <div class="col-md-4">
                            <label for="referrer"> ¿Cual es el tema?
                                <select id="inputState" class="form-select" v-model="selectedTheme">
                                    <option selected>Choose...</option>
                                    <option value="1">arrays</option>
                                    <option value="2">if</option>
                                    <option value="3">whiles</option>
                                </select>
                            </label>
                        </div>
                    </div>
                    <!-- Seleccion Input seccion -->
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked
                            v-model="hints" />
                        <label class="form-check-label" for="flexSwitchCheckChecked">Habilitar pista</label>
                    </div>
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
                                    <option v-for="(option, index) in options" :key="index" :value="index">{{ option.text }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-primary" @click="generateJSON">Generar JSON</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            questionType: 'codigo',
            title: '',
            author: '',
            driver: '',
            description: '',
            selectedDifficulty: '',
            selectedTheme: '',
            inputs: [],
            outputs: [],
            answer: '',
            hints: true,
            options: [
                { text: '', explanation: '', isAnswer: false },
                { text: '', explanation: '', isAnswer: false },
                { text: '', explanation: '', isAnswer: false },
                { text: '', explanation: '', isAnswer: false }
            ]
        };
    },
    methods: {
        addInputOutput() {
            if (this.inputs.length < 4 && this.outputs.length < 4) {
                this.inputs.push('');
                this.outputs.push('');
            }
        },
        generateJSON() {
            if (this.questionType === 'codigo') {
                const questionData = {
                    id: `TC1028_23_C_${Date.now()}`,
                    author: this.author,
                    title: this.title,
                    description: this.description,
                    topic: this.selectedTheme,
                    difficulty: this.selectedDifficulty,
                    tests: []
                };

                for (let i = 0; i < this.inputs.length; i++) {
                    const test = {
                        testId: (i + 1).toString(),
                        input: this.inputs[i],
                        output: this.outputs[i]
                    };
                    questionData.tests.push(test);
                }

                const jsonData = JSON.stringify(questionData, null, 2);

                const element = document.createElement("a");
                const file = new Blob([jsonData], { type: "application/json" });
                element.href = URL.createObjectURL(file);
                element.download = "question.json";
                document.body.appendChild(element);
                element.click();
                document.body.removeChild(element);
            } else if (this.questionType === 'multiple') {
                const questionData = {
                    id: `TC1028_23_OM_${Date.now()}`,
                    author: this.author,
                    title: this.title,
                    description: this.description,
                    topic: this.selectedTheme,
                    difficulty: this.selectedDifficulty,
                    answer: this.answer,
                    hints: this.hints,
                    options: this.options
                };

                const jsonData = JSON.stringify(questionData, null, 2);

                const element = document.createElement("a");
                const file = new Blob([jsonData], { type: "application/json" });
                element.href = URL.createObjectURL(file);
                element.download = "question.json";
                document.body.appendChild(element);
                element.click();
                document.body.removeChild(element);
            }
        }
    }
};
</script>

<!-- Style -->
<style >
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
    border-color: #039BE5;
    background-color: #81D4FA;
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
    border: 2px solid #039BE5
}

.agree-text {
    font-size: 12px
}
</style>
  