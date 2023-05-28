<script>
</script>


<template>
    <div class="wrapper d-flex">
        <div class="sidebar">
            <small class="text-muted pl-3">Activdades</small>
            <ul>
                <li><a href="#"><i class="far fa-credit-card"></i>Tareas<img
                            src="https://img.icons8.com/material-outlined/24/000000/new.png" /></a></li>
                <li><a href="#"><i class="fas fa-file-invoice"></i>Quizes <img
                            src="https://img.icons8.com/material-outlined/24/000000/2.png" /></a></li>
            </ul>
            <small class="text-muted px-3"> TOOLS</small>
            <ul>
                <li><a href="#"><i class="far fa-calendar-alt"></i>ink 3</a></li>
                <li><a href="#"><i class="fas fa-video"></i>ink 4</a></li>
                <li><a href="#"><i class="fas fa-id-badge"></i>ink 5</a></li>
            </ul>
            <small class="text-muted px-3">BASE</small>
            <ul>
                <li><a href="#"><i class="fas fa-external-link-alt"></i>link 6</a></li>
                <li><a href="#"><i class="fas fa-code"></i>link 7</a></li>
            </ul>
        </div>
    </div>

    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-lg-6 mb-4 mb-lg-0">
                <div class="card mb-3" style="border-radius: .5rem;">
                    <div class="row g-0">
                        <div class="col-md-4 gradient-custom text-center text-white"
                            style="border-top-left-radius: .5rem; border-bottom-left-radius: .5rem;">
                            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                                alt="Avatar" class="img-fluid my-5" style="width: 80px;" />
                            <h5>Marie Horwitz</h5>
                            <p>Web Designer</p>
                            <i class="far fa-edit mb-5"></i>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body p-4">
                                <h6>Titulo</h6>
                                <hr class="mt-0 mb-4">
                                <div class="row pt-1">
                                    <div class="col-6 mb-3">
                                        <h6>Dificultad</h6>
                                        <p class="text-muted">Facil</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <h6>Tiempo</h6>
                                        <p class="text-muted">50 minutos</p>
                                    </div>
                                </div>
                                <h6>10 preguntas</h6>
                                <hr class="mt-0 mb-4">
                                <div class="row pt-1">
                                    <div class="col-6 mb-3">
                                        <h6>Tema</h6>
                                        <p class="text-muted">Variables</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <h6>Grupo</h6>
                                        <p class="text-muted">1</p>
                                    </div>
                                    <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                                        style="z-index: 1;">
                                        Editar
                                    </button>
                                </div>
                                <div class="d-flex justify-content-start">
                                    <a href="#!"><i class="fab fa-facebook-f fa-lg me-3"></i></a>
                                    <a href="#!"><i class="fab fa-twitter fa-lg me-3"></i></a>
                                    <a href="#!"><i class="fab fa-instagram fa-lg"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style>
.container.py-5.h-100 {
    margin-top: 120px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    list-style: none;
    text-decoration: none;
    font-family: arial;
}

body {
    background: #304878;
}

.wrapper {
    position: relative;
    margin-top: 120px;

}

.sidebar {
    position: fixed;
    width: 300px;
    height: 100%;
    background: #000000e0;
    padding: 20px 0;
}

.text-muted {
    color: #adb5bd !important;
}

ul {
    padding-bottom: 20px;
}

ul li a img {
    background: #66BB6A;
    top: 0;
    border: none;
    width: 20px;
}

.sidebar ul li {
    padding: 15px;
}

.sidebar ul li a {
    color: #fff;
    display: block;
}

.sidebar ul li a .fas {
    width: 30px;
    color: #bdb8d7 !important;
}

i.fas.fa-home:hover,
i.fas.fa-file-invoice:hover,
i.fas.fa-video:hover,
i.fas.fa-id-badge:hover,
i.fas.fa-external-link-alt:hover,
i.fas.fa-code:hover,
i.far.fa-calendar-alt:hover,
i.far.fa-credit-card:hover {
    color: #304FFE !important;
}

.sidebar ul li a .far {
    width: 30px;
    color: #bdb8d7 !important;
}

.sidebar ul li:hover {
    background: #000;
}

.sidebar ul li a:hover {
    text-decoration: none;
}</style>