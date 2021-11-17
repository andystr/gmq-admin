"use strict";
// Equipamiento
function equipamientoLista(datas, placa) {
    var dataFinal = new Array();
    var dataBruta = datas.split(',');
    //var htmlElement = document.getElementById("langDiv");
    dataFinal = dataBruta.reverse();
    var langDiv = document.getElementById("langDiv");
    langDiv.id = "newId" + placa;  // here you can assign new Id

    var html = "<form>";

    for (var i = 0; i < (dataFinal.length); i++) {
        //html += "<input type='checkbox' name='" + dataFinal[i] + "' value='" + i + "' onClick=\"setValue(this.value);\">" + dataFinal[i] + "<br>";
        html += "<span class='badge badge-default'>" + dataFinal[i] + "</span>&nbsp;";
    }
    html += "</form>";

    langDiv.innerHTML = html;
}
function formatoMoneda(numero, idDivCampo, idVehiculo) {
    var datosParaFormato = numero.split(',');
    var dataFinalParaFormato = datosParaFormato[0];
    var numeroFormateadoMoneda = numeral(dataFinalParaFormato).format('$0,0.00');
    var idDiv = document.getElementById(datosParaFormato[1]);
    idDiv.id = "newId" + Math.floor(Math.random() * 11000);  // here you can assign new Id
    switch (datosParaFormato[1]) {
        case "costoCampo":
            var html = "<strong data-toggle='modal' data-target='#datosCostosModal" + datosParaFormato[2] + "'>" + numeroFormateadoMoneda + "</strong>";
            break;
        case "precioCampo":
            var html = "<strong>" + numeroFormateadoMoneda + "</strong>";
            break;
        default:
        // code block
    }


    idDiv.innerHTML = html;
}

function formatoKilometraje(numero, idDivCampo) {
    var datosParaFormato = numero.split(',');
    var dataFinalParaFormato = datosParaFormato[0];
    var numeroFormateadoKilometraje = numeral(dataFinalParaFormato).format('0,0');
    var idDiv = document.getElementById(datosParaFormato[1]);
    idDiv.id = "newId" + Math.floor(Math.random() * 11000);  // here you can assign new Id
    var html = "<i class='fas fa-road'></i>&nbsp;&nbsp;" + numeroFormateadoKilometraje;
    idDiv.innerHTML = html;
}