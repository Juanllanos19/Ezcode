<template>
    <div class="container mt-5 mb-5 d-flex justify-content-center">
        <div class="card px-1 py-4">
            <div class="card-body">
                <h6 class="card-title mb-3">Seleccione el tipo de pregunta</h6>
                <div class="d-flex flex-row">
                    <label class="radio mr-1">
                        <input type="radio" name="add" value="anz" v-model="questionType.value"
                            @change="handleQuestionTypeChange('codigo')" checked>
                        <span>
                            <i class="fa fa-user"></i> Codigo
                        </span>
                    </label>
                    <label class="radio">
                        <input type="radio" name="add" value="add" v-model="questionType.value"
                            @change="handleQuestionTypeChange('multiple')" checked>
                        <span>
                            <i class="fa fa-plus-circle"></i> Multiple
                        </span>
                    </label>
                </div>
                <h6 class="information mt-4">Personalice la pregunta</h6>
                <div v-if="questionType === 'codigo'">
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="text" placeholder="Titulo">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <div class="input-group"> <input class="form-control" type="text" placeholder="Autor">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <!-- <label for="name">Name</label> --> <input class="form-control" type="text"
                                    placeholder="Descripción">
                            </div>
                        </div>
                    </div>

                    <!-- Filtro seccion -->
                    <div class="d-flex flex-row">
                        <div class="row">
                            <div class="col-sm-12">
                                <div class="form-group">
                                    <input type="number" id="replyNumber" min="0" data-bind="value:replyNumber"
                                        placeholder="Ponderacion" required v-model="ponderation">
                                </div>
                            </div>
                        </div> &nbsp;&nbsp;
                        <div class="content-wrapper">
                            <label for="datepicker">Fecha y hora</label>
                            <datepicker v-model="selectedDate" format="yyyy-MM-dd HH:mm" :clear-button="true"
                                :editable="false">
                            </datepicker>
                        </div> &nbsp;&nbsp;
                        <label for="referrer"> ¿Cual es la dificultad?
                            <select id="inputState" class="form-select" v-model="selectedDifficulty">
                                <option selected>Choose...</option>
                                <option value="1">Dificil</option>
                                <option value="2">Medio</option>
                                <option value="3">Facil</option>
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
                    <div class="d-flex flex-row">
                        <div class="row">
                            <div v-for="(boxOutCode, index) in boxOutCode" :key="index" class="col-12">
                                <a for="inputAddress" class="form-label">Output {{ index + 1 }}</a>
                                <input type="text" class="form-control" v-model="boxText">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12">
                                <button type="button" class="btn btn-primary" @click="addOutCode">AñadirOut</button>
                                <button type="button" class="btn btn-danger" @click="deleteOutCode">EliminarOut</button>
                            </div>
                        </div>
                        <div class="row">
                            <div v-for="(boxIntCode, index) in boxIntCode" :key="index" class="col-12">
                                <a for="inputAddress" class="form-label"> Input {{ index + 1 }}</a>
                                <input type="text" class="form-control" v-model="boxText">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12">
                                <button type="button" class="btn btn-primary" @click="addIntCode">AñadirInt</button>
                                <button type="button" class="btn btn-danger" @click="deleteIntCode">EliminarInt</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Pestaña de Multiple -->
                <div v-if="questionType === 'multiple'">
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="text" placeholder="Titulo">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <div class="input-group"> <input class="form-control" type="text" placeholder="Autor">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="form-group">
                                <!-- <label for="name">Name</label> --> <input class="form-control" type="text"
                                    placeholder="Descripción">
                            </div>
                        </div>
                    </div>
                    <!-- Filtro seccion -->
                    <div class="d-flex flex-row">
                        <div class="row">
                            <div class="col-sm-12">
                                <div class="form-group">
                                    <input type="number" id="replyNumber" min="0" data-bind="value:replyNumber"
                                        placeholder="Ponderacion" required v-model="ponderation">
                                </div>
                            </div>
                        </div> &nbsp;&nbsp;
                        <div class="content-wrapper">
                            <label for="datepicker">Fecha y hora</label>
                            <datepicker v-model="selectedDate" format="yyyy-MM-dd HH:mm" :clear-button="true"
                                :editable="false">
                            </datepicker>
                        </div> &nbsp;&nbsp;
                        <label for="referrer"> ¿Cual es la dificultad?
                            <select id="inputState" class="form-select" v-model="selectedDifficulty">
                                <option selected>Choose...</option>
                                <option value="1">Dificil</option>
                                <option value="2">Medio</option>
                                <option value="3">Facil</option>
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
                    <div class="input-group">
                        <div class="input-group-text">
                            <input class="form-check-input mt-0" type="radio" name="option" value="option1"
                                aria-label="Radio button 1">
                        </div>
                        <input type="text" class="form-control" aria-label="Text input for option 1">
                    </div>

                    <div class="input-group">
                        <div class="input-group-text">
                            <input class="form-check-input mt-0" type="radio" name="option" value="option2"
                                aria-label="Radio button 2">
                        </div>
                        <input type="text" class="form-control" aria-label="Text input for option 2">
                    </div>

                    <div class="input-group">
                        <div class="input-group-text">
                            <input class="form-check-input mt-0" type="radio" name="option" value="option3"
                                aria-label="Radio button 3">
                        </div>
                        <input type="text" class="form-control" aria-label="Text input for option 3">
                    </div>

                    <div class="input-group">
                        <div class="input-group-text">
                            <input class="form-check-input mt-0" type="radio" name="option" value="option4"
                                aria-label="Radio button 4">
                        </div>
                        <input type="text" class="form-control" aria-label="Text input for option 4">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';
import Datepicker from 'vue3-datepicker';

const questionType = ref('anz');

function handleQuestionTypeChange(type) {
    questionType.value = type;
}

const selectedDate = ref('');
const selectedTheme = ref('');
const selectedDifficulty = ref('');
const ponderation = ref('');
const boxOutCode = ref([]); // Array to hold box texts
const boxIntCode = ref([]);

const addOutCode = () => {
    boxOutCode.value.push('');
};

// Method to delete the last box text
const deleteOutCode = () => {
    boxOutCode.value.pop();
};

const addIntCode = () => {
    boxIntCode.value.push('');
};

// Method to delete the last box text
const deleteIntCode = () => {
    boxIntCode.value.pop();
};
</script>


<!-- Style -->
<style >
body {
    background-color: #304878
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
  