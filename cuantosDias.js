// Programa que retorna cuantos dias hay entre dos cadenas de texto que representen fechas.

function cuantosDias(fecha1, fecha2) {
    let fecha1Array = fecha1.split("/");
    let fecha2Array = fecha2.split("/");
    let fecha1Date = new Date(fecha1Array[2], fecha1Array[1] - 1, fecha1Array[0]);
    let fecha2Date = new Date(fecha2Array[2], fecha2Array[1] - 1, fecha2Array[0]);
    let diferencia = fecha2Date - fecha1Date;
    let dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));
    return dias;
}

console.log(cuantosDias("01/01/2021", "01/01/2022")); // 365