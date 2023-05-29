import { RouterLink} from 'vue-router'

<template>
    <nav class="navbar navbar-expand-lg fixed-top" style="background-color: rgb(113, 132, 158);">
        <div class="container-fluid">
        <RouterLink to="/" class="navbar-brand"  style="width:15%; padding-left: 10%;"><img id="logo-navbar" src="../assets/A01732454_Poster.png" style="width: auto; height: 80px;"></RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" style="padding-right: 10%;">
                <RouterLink to="/inicio" class="nav-link" id="menu-nav" >MENU</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink to="/desempenio" class="nav-link" id="desempenio-nav" >DESEMPEÑO</RouterLink>
            </li>
            <li class="nav-item">
                
            </li>
            </ul>
            <span class="navbar-text" style="padding-right: 3%;">
                <RouterLink to="/" class="navbar-brand logo-text"><img id="logo-notificaciones" src="../assets/icon _bell.png" style="width: 80%;"></RouterLink>
            </span>
            <span class="navbar-text" style="padding-right: 10%;">
                <router-link to="/" class="navbar-brand logo-text"><img id="logo-perfil" src="../assets/icon_profile.png" style="width: 80%;"></router-link>
            </span>
        </div>
        </div>
    </nav>
    <RouterView />
</template>

<script>
export default {
    name: 'NavInit'
}
</script>
  
  