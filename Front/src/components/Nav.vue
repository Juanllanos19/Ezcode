<template>
<nav id="navbarExample" class="navbar navbar-expand-lg fixed-top navbar-light" aria-label="Main navigation">
    <div class="container">
      <RouterLink to="/" class="navbar-brand logo-text"><img id="logo-navbar" src="../assets/A01732454_Poster.png" alt=""></RouterLink>
      <button style="background-color: gainsboro;" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <div class="navbar-nav">
                <RouterLink to="/" class="nav-link text-white">PRODUCTO</RouterLink>
                <RouterLink to="/" class="nav-link text-white">NOSOTROS</RouterLink>
                <RouterLink to="/login" id="sign-up-navbar" class="nav-link text-white" data-bs-toggle="modal" data-bs-target="#exampleModal">SIGN UP</RouterLink>
              </div>
      </div>
    </div>
</nav>
</template>
  
  <style>
  #navbarExample{
    backdrop-filter: blur(10px);
    height: 15%;
  }
  #logo-navbar {
    width: 25%;
  }
  .nav-link{
    margin-left: 5%;
    letter-spacing: 7px;
    width: 100%;
    white-space: nowrap;
    font-size: large;
  }
  </style>

<script>
export default {
    name: 'Nav'
}
</script>
  
  