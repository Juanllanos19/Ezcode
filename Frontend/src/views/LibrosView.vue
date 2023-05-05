<script setup>
    import{ref} from 'vue'
    const data = ref([
        {
            titulo: "La Divina Comedia",
            autor: "Dante Alighieri",
            num_pag: "304",
            portada: "/src/assets/img01.jpg"
        },
        {
            titulo: "El principito",
            autor: "Antoine Griezman",
            num_pag: "120",
            portada: "/src/assets/img02.jpg"
        }
    ])
</script>

<template>
    <div class="container">
    <h1>Libros</h1>
    <div v-for="(item,i) in data" v-bind:key="i" class="card" style="width: 18rem;">
        <img :src="item.portada" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{{ item.titulo }}</h5>
            <p class="card-text">Autor: {{item.autor}} - Pags. {{ item.num_pag }}</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>
</div>
</template>