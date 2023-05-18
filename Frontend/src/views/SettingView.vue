<script setup>
import { ref } from 'vue'
const darkMode = ref(false);
</script>

<template>
    <body :class="{ 'dark-mode': darkMode }">
        <h1>Settings</h1>
        <div class="containerbox">
            <div class="mb-3 row">
                <label for="staticUser" class="col-sm-2 col-form-label">User</label>
                <div class="col-sm-10">
                    <input type="text" readonly class="form-control-plaintext" id="staticUser" value="A000000">
                </div>
            </div>
            <div class="mb-3 row">
                <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                <div class="col-sm-10">
                    <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com">
                </div>
            </div>
            <div class="mb-3 row">
                <label for="inputPassword" class="col-sm-2 col-form-label">Contraseña</label>
                <div class="col-sm-10">
                    <span class="text-muted">
                        <a href="#" class="text-reset">Cambiar contraseña</a>.
                    </span>
                </div>
            </div>


            <!-- Color Mode -->
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" v-model="darkMode" id="flexSwitchCheckChecked">
                <label class="form-check-label" for="flexSwitchCheckChecked">Cambiar modo oscuro</label>
            </div>


            <!-- Change Language -->

            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
                <label class="form-check-label" for="flexSwitchCheckChecked">Cambiar idioma</label>
            </div>

        </div>
        <RouterView />
    </body>
</template>

<style>
body {
    background-color: var(--background-color);
    color: var(--text-color);
    transition: background-color 0.3s, color 0.3s;
}

:root {
    --background-color-light: #4444b8;
    --background-color-dark: #111;
    --text-color-light: #000;
    --text-color-dark: #fff;
}

.dark-mode {
    --background-color: var(--background-color-dark);
    --text-color: var(--text-color-dark);
}

.containerbox {
    background-color: #7890A8;
    margin: auto;
    width: 70%;
    border-radius: 5%;
    padding: 10px;
    height: 500px;
}

.mb-3 {
    margin-bottom: 20px;
    /* Ajusta la distancia vertical */
}

.col-sm-2 {
    padding-top: 10px;
    /* Ajusta la distancia vertical */
}

.col-sm-10 {
    padding-top: 10px;
    /* Ajusta la distancia vertical */
}

.form-check.form-switch {
    margin-bottom: 20px;
    /* Ajusta la distancia vertical */
}
</style>