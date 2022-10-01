personas = [];
let bottomBuscar = document.getElementById("bottomBuscarPersona")

let getPersonaUrl = "http://127.0.0.1:8000/personas/consultarPersona/";

function clickBuscarPersona(){
    // console.log("Hola")
    getPersona();
}

function getPersona(){
    const NumDocumento = document.formConsulta.num_documento.value;
    console.log(NumDocumento)

    fetch(getPersonaUrl + NumDocumento)
        .then((response) => {
        console.log(response.ok);
        if (response.ok || response.status == 400) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
        })
        //recibimos un json en data
        .then((data) => {
            if (data.includes("No existe persona")) {
                funcionError(data);
            }
            //convertir objeto del back en objecto json.
            personas = JSON.parse(data);
            console.log("Llamando a procesar");

            procesarPersonas();
        })
        .catch((err) => {
        console.log("Catch: " + err.message);
        });
}

function procesarPersonas() {
    console.log(personas);
    document.getElementById("main").innerHTML = "";
    const tabla = document.createElement("table");
    const hileraHeader = document.createElement("tr");
  
    for (let k in personas[0]) {
      const celdaHeder = document.createElement("td");
      const textoHeaders = document.createTextNode(k);
      celdaHeder.appendChild(textoHeaders);
      hileraHeader.appendChild(celdaHeder);
    }
    tabla.appendChild(hileraHeader);
    for (let i = 0; i < personas.length; i++) {
      const hilera = document.createElement("tr");
      for (let j in personas[i]) {
        const celda = document.createElement("td");
        const textoCelda = document.createTextNode(personas[i][j]);
        celda.appendChild(textoCelda);
        hilera.appendChild(celda);
      }
      tabla.appendChild(hilera);
    }
    // if (document.getElementById("contenido") != null) {
    //   document.getElementById("contenido").remove();
    // }
    if (personas.length == 0) {
      document.getElementById("main").innerHTML = `
      <h2>No existe coincidencia. Intente buscar de nuevo</h2>
      `;
    }
    const info = document.getElementById("main");
    info.appendChild(tabla);
  }

function funcionError(err) {
    if (err) {
      document.getElementById("main").innerHTML = `
      <h2>${err}</h2>
      `;
    }
  }

bottomBuscar.addEventListener("click", clickBuscarPersona)