var addMedicamento = document.getElementById("addMedicamento");
var deleteMedicamento = document.getElementById("#deleteMedicamento");

addMedicamento.addEventListener("click", ()=>{
    document.querySelector(".listaMedicamentos").innerHTML +=`
        <div class="row">
            <div class="col">
                <div class="mb-3">
                    <label for="txtMedicamento" class="form-label">Medicamento</label>
                    <input type="text" class="form-control" id="txtMedicamento" />
                </div>
            </div>
            <div class="col">
                <div class="mb-3">
                    <label for="numCantidad" class="form-label">Cantidad</label>
                    <input type="number" class="form-control" id="numCantidad" />
                </div>
            </div>
            <div class="col">
                <div class="mb-3">
                    <label for="numFrecuencia" class="form-label">Frecuencia de horas</label>
                    <input type="number" class="form-control" id="numFrecuencia" />
                </div>
            </div>
            <div class="col">
                <div class="mb-3">
                    <label for="numDias" class="form-label">Dias de consumo</label>
                    <input type="text" class="form-control" id="numDias" />
                </div>
            </div>
            <div class="col">
                <button type="button" id="deleteMedicamento" class="btn btn-outline-danger">- Eliminar Medicamento</button>
            </div>
        </div>`
})
