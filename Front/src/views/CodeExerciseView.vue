<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
</script>

<script>
import NavInit from '../components/NavInit.vue'
import DesempenioView from './DesempenioView.vue';

export default {
  components: {
    NavInit,
    DesempenioView
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
                <div id="description" style="width: 40%; padding-top: 8%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Descripcion</div>
                            <div class="card-body">
                                <h5 class="card-title">Primary card title</h5>
                                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            </div>
                    </div>
                </div>
                <div id="code" style="width: 60%; padding-top: 8%;padding-left: 0.5%;">
                    <div class="card" style="width: 100%;">
                        <div class="card-header">Header</div>
                        <div class="card-body">
                            <h5 class="card-title">Primary card title</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
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