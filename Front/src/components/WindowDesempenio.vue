<template>
  <div class="card text-bg-dark mb-3" >
    <div class="card-header">
      <!-- Example single danger button -->
    <div class="btn-group" style="padding-left: 3%;">
      <button type="button" class="btn btn-warning dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Temas
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">Separated link</a></li>
      </ul>
    </div>
    <div class="btn-group" style="padding-left: 5%;">
      <button type="button" class="btn btn-warning dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Dificultad
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Ultimo resultado</a></li>
        <li><a class="dropdown-item" href="#">Titulo</a></li>
        <li><a class="dropdown-item" href="#">Tema</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">Separated link</a></li>
      </ul>
    </div>
  </div>
    
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Ultimo resultado</th>
            <th scope="col">Titulo</th>
            <th scope="col">Tema</th>
            <th scope="col">Dificultad</th>
            <th scope="col">Resultado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td colspan="2">Larry the Bird</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
  .card{
    width: 60%;
  }
</style>

<script>
export default {
    name: 'WindowDesempenio'
}
</script>