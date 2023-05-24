<script setup>
import { loadFull } from "tsparticles";

const particlesInit = async engine => {
    await loadFull(engine);
};

const particlesLoaded = async container => {
    console.log("Particles container loaded", container);
};
</script>

<template>
     <div>
        <Particles
          id="tsparticles"
          :particlesInit="particlesInit"
          :particlesLoaded="particlesLoaded"
          url="http://foo.bar/particles.json"
      />

      <Particles
          id="tsparticles"
          :particlesInit="particlesInit"
          :particlesLoaded="particlesLoaded"
          :options="{
                  background: {
                      color: {
                          value: '#181848'
                      }
                  },
                  fullScreen:{
                    enable: true,
                    zIndex: -1,
                  },
                  fpsLimit: 120,
                  interactivity: {
                      events: {
                          onClick: {
                              enable: true,
                              mode: 'push'
                          },
                          onHover: {
                              enable: true,
                              mode: 'repulse'
                          },
                          resize: true
                      },
                      modes: {
                          bubble: {
                              distance: 400,
                              duration: 2,
                              opacity: 0.8,
                              size: 40
                          },
                          push: {
                              quantity: 4
                          },
                          repulse: {
                              distance: 200,
                              duration: 0.4
                          }
                      }
                  },
                  particles: {
                      color: {
                          value: '#ffffff'
                          // value: '#4654A6'
                      },
                      links: {
                          color: '#ffffff',
                          // color: '#4EA641',
                          distance: 150,
                          enable: true,
                          opacity: 0.5,
                          width: 1
                      },
                      collisions: {
                          enable: true
                      },
                      move: {
                          direction: 'none',
                          enable: true,
                          outMode: 'bounce',
                          random: false,
                          speed: 1,
                          straight: false
                      },
                      number: {
                          density: {
                              enable: true,
                              area: 800
                          },
                          value: 100
                      },
                      opacity: {
                          value: 0.5
                      },
                      shape: {
                          type: 'circle'
                      },
                      size: {
                          random: true,
                          value: 5
                      }
                  },
                  detectRetina: true
              }"
      />
     </div>
</template>

<script>
export default {
    name: 'Background'
}
</script>
