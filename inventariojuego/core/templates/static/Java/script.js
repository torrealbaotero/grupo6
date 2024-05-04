function mostrarRegistro() {
    $('#registrarUsuario').show();
}

function validarRegistro() {
    var contraseña = $('#contraseñaRegistro').val();
    var confirmarContraseña = $('#confirmarContraseña').val();

    if (contraseña !== confirmarContraseña) {
        alert("Las contraseñas no coinciden");
        return;
    }

    if (!contraseña.match(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{7,20}$/)) {
        alert("La contraseña debe contener entre 7 y 20 caracteres, al menos una mayúscula, un símbolo y un número.");
        return;
    }

    alert("Usuario registrado con éxito");

    var nombreUsuario = $('#nombreUsuario').val();
    $('#mensajeBienvenida').text("Bienvenido/a " + nombreUsuario);
}

function recuperarContraseña() {
    var email = prompt("Para recuperar su contraseña, coloque su email:");

    if (email) {
        alert("Se ha enviado a su correo un email para recuperar su contraseña");
    }
}

function validarInicioSesion() {
    var nombreUsuario = $('#usuario').val();
    if (nombreUsuario) {
        $('#mensajeBienvenida').text("Bienvenido/a " + nombreUsuario);
        $('#botonModificarPerfil').show(); // Mostrar el botón "Modificar perfil"
    } else {
        alert("Por favor, ingrese un nombre de usuario.");
    }
}

function mostrarVentanaModificarPerfil() {
    $('#ventanaModificarPerfil').show();
}

function guardarCambiosPerfil() {
    alert("Los cambios han sido guardados con éxito");

}




// CARRITO //

let carrito = [];

// Función para agregar un juego al carrito
function agregarAlCarrito(nombreJuego, precioJuego) {
    let juego = {
        nombre: nombreJuego,
        precio: precioJuego
    };

    carrito.push(juego);
    actualizarInterfazUsuario();
}

// Función para actualizar la interfaz de usuario con los juegos en el carrito
function actualizarInterfazUsuario() {
    let listaJuegosHTML = document.getElementById('lista-juegos');
    let totalPrecioHTML = document.getElementById('total-precio');

    // Limpiar la lista de juegos antes de agregar los juegos actualizados
    listaJuegosHTML.innerHTML = '';

    // Iterar sobre los juegos en el carrito y agregarlos a la lista de juegos
    let total = 0;
    carrito.forEach(juego => {
        let juegoItem = document.createElement('li');
        juegoItem.textContent = `${juego.nombre}: $${juego.precio} CLP`;
        listaJuegosHTML.appendChild(juegoItem);
        total += juego.precio;
    });

    // Actualizar la visualización del total del carrito
    totalPrecioHTML.textContent = `$${total.toFixed(2)} CLP`;
}

// Función para realizar la compra
function realizarCompra() {
    // Implementa la lógica para realizar la compra aquí
}

// Función para vaciar el carrito
function vaciarCarrito() {
    carrito = [];
    actualizarInterfazUsuario();
}
