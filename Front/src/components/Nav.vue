<template>
<nav id="navbarExample" class="navbar navbar-expand-lg fixed-top navbar-light" aria-label="Main navigation">
    <div class="container">
      <RouterLink to="/" class="navbar-brand logo-text"><img id="logo-navbar" src="../assets/A01732454Poster.png" alt=""></RouterLink>
      <button style="background-color: gainsboro;" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <div class="navbar-nav">
            <a class="nav-link text-white" href="#producto" @click="scrollToSection">PRODUCTO</a>
            <a class="nav-link text-white" href="#nosotros" @click="scrollToSection">NOSOTROS</a>
                <RouterLink to="/login" id="sign-up-navbar" class="nav-link text-white" style="font-size: large; font-family: 'Russo One', sans-serif;">LOG IN</RouterLink>
              </div>
      </div>
    </div>
</nav>
<RouterView />
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
    margin-left: 2%;
    letter-spacing: 7px;
    width: 100%;
    white-space: nowrap;
    font-size: large;
  }
  </style>

<script>
export default {
  name: 'Nav',
  methods: {
    scrollToSection(event) {
      event.preventDefault();
      const targetId = event.target.getAttribute("href");
      const targetElement = document.querySelector(targetId);
      window.scrollTo({
        top: targetElement.offsetTop,
        behavior: "smooth",
      });
    },
  },
};
</script>
  