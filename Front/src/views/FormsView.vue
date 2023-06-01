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
                                <div class="input-group"> <input class="form-control" type="text" placeholder="Driver">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-group">
                            <textarea class="form-control" aria-label="With textarea" placeholder="Descripción"></textarea>
                        </div>
                    </div>

                    <!-- Filtro seccion -->
                    <div class="d-flex flex-row">
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
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Input">
                                <input type="text" class="form-control" placeholder="Output">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Input">
                                <input type="text" class="form-control" placeholder="Output">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Input">
                                <input type="text" class="form-control" placeholder="Output">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Input">
                                <input type="text" class="form-control" placeholder="Output">
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
                        <div class="input-group">
                            <textarea class="form-control" aria-label="With textarea" placeholder="Descripción"></textarea>
                        </div>
                    </div>
                    <!-- Filtro seccion -->
                    <div class="d-flex flex-row">
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
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
                        <label class="form-check-label" for="flexSwitchCheckChecked">Habilitar pista</label>
                    </div>
                    <div class="d-flex flex-row">
                        <div class="row">
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Respuesta correcta">
                                <input type="text" class="form-control" placeholder="Explicación">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Opción 1">
                                <input type="text" class="form-control" placeholder="Explicación">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Opción 2">
                                <input type="text" class="form-control" placeholder="Explicación">
                            </div>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Opción 3">
                                <input type="text" class="form-control" placeholder="Explicación">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { ref, computed } from 'vue';

export default {
    setup() {
        const questionType = ref('codigo');

        const isCodigoQuestionType = computed(() => questionType.value === 'codigo');
        const isMultipleQuestionType = computed(() => questionType.value === 'multiple');

        // Remaining setup logic

        return {
            questionType,
            isCodigoQuestionType,
            isMultipleQuestionType
        };
    },
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
  