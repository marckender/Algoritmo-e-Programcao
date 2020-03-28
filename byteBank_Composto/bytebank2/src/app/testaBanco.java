package app;

/**
 * testaBanco
 */
class testaBanco {
    public static void main(String[] args) {

        cliente paulo= new cliente();
        paulo.nome ="paulo Silveira";
        paulo.cpf="222.222.222-22";
        paulo.profissao="programador";
        
        conta contaDoPaulo= new conta();
            contaDoPaulo.deposita(100);

            contaDoPaulo.titular=paulo;
            System.out.println(contaDoPaulo.titular.nome);
            System.out.println(contaDoPaulo.titular);
    }
        
}