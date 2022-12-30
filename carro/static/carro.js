const incrementar = (id_libro) => {
    const dataCantidad = document.getElementById(id_libro);
    let cantidad = dataCantidad.value;
    dataCantidad.value = Number(cantidad) + 1;
}

const decrementar = (id_libro) => {
    const dataCantidad = document.getElementById(id_libro);
    let cantidad = dataCantidad.value;
    if (Number(cantidad) > 1){
        dataCantidad.value = Number(cantidad) - 1;
    }  
}