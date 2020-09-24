class Endereco {

    constructor ( rua, bairro, cidade, estado) {
        this.rua = rua;
        this.bairro = bairro;
        this.cidade = cidade;
        this.estado = estado;
    }

    set novaRua(novaRua) {
        this.rua = novaRua;
    }

}

let endereco = new Endereco("Rua gracilliano", "JD", "CH", "SC" );
console.log(endereco);

endereco.novaRua= "Rua dos pardais";
console.log(endereco);