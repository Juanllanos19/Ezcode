<template>
    <form>
        <h3>Iniciar sesión</h3>

        <div class="form-group">
            <label>Correo electronico</label>
            <input type="email" class="form-control" placeholder="Correo electronico"/>
        </div>

        <div class="form-group">
            <label>Contrasena</label>
            <input type="password" class="form-control" placeholder="Contrasena"/>
        </div>

        <button class="btn btn-primary btn-block">Iniciar sesión</button>
    </form>
</template>

<script>
    export default {
        name: 'Login'
    }
</script>