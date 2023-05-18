<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
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
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
        </div>
        </div>
    </div>
    </div>
</template>

<script>
    export default {
        name: 'Login'
    }
</script>