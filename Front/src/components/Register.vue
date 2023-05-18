<template>
    <form>
        <h3>¡Registrate!</h3>

        <div class="form-group">
            <label>Nombre</label>
            <input type="text" class="form-control" placeholder="Nombre"/>
        </div>

        <div class="form-group">
            <label>Apellidos</label>
            <input type="text" class="form-control" placeholder="Apellidos"/>
        </div>

        <div class="form-group">
            <label>Correo electronico</label>
            <input type="email" class="form-control" placeholder="Correo eletronico"/>
        </div>

        <div class="form-group">
            <label>Contrasena</label>
            <input type="password" class="form-control" placeholder="Contrasena"/>
        </div>

        <div class="form-group">
            <label>Confirma tu contrasena</label>
            <input type="password" class="form-control" placeholder="Confirma tu contrasena"/>
        </div>

        <button class="btn btn-primary btn-block">Regristate</button>
    </form>
</template>

<script>
    export default {
        name: 'Register'
    }
</script>