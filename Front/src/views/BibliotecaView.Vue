<script>
</script>


<template>
    <div class="wrapper d-flex">
        <div class="sidebar">
            <small class="text-muted pl-3">Activdades</small>
            <ul>
                <li>
                    <div class="dropdown">
                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Tareas
                        </button>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <a class="dropdown-item" href="#">Tarea 1</a>
                            <a class="dropdown-item" href="#">Tarea 2</a>
                            <a class="dropdown-item" href="#">Tarea 3</a>
                        </div>
                    </div>
                </li>
                <li><a href="#"><i class="fas fa-file-invoice"></i>Quizes</a></li>
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

ul {
    padding-bottom: 20px;
}

.sidebar ul li {
    padding: 15px;
}

.sidebar ul li a {
    color: #fff;
    display: block;
}

/* Estilo para el botón del dropdown */
.dropdown .btn {
  background-color: #304878; /* Cambia el color de fondo del botón */
  color: #FFFFFF; /* Cambia el color del texto del botón */
}

/* Estilo para el menú desplegable del dropdown */
.dropdown-menu {
  background-color: #304878; /* Cambia el color de fondo del menú desplegable */
}
/* Estilo para los elementos del menú del dropdown cuando se les pasa el mouse por encima */
.dropdown-item:hover {
  background-color: #fff; /* Cambia el color de fondo de los elementos del menú al pasar el mouse por encima */
  color: #000000; /* Cambia el color del texto de los elementos del menú al pasar el mouse por encima */
}

</style>