/**
 * testaMetodo
 */
public class testaMetodo {

    public static void main(String[] args) {
        conta contaDoPaulo= new conta();
        contaDoPaulo.saldo=100;
        contaDoPaulo.deposita(50);
        System.out.println(contaDoPaulo.saldo);

        boolean conseguiuRetirar=contaDoPaulo.saca(20);
        System.out.println(contaDoPaulo.saldo);
        System.out.println(conseguiuRetirar); 

        conta contaDaMarcela= new conta();
        contaDaMarcela.deposita(1000);

        contaDaMarcela.transfere(300,contaDoPaulo);
        System.out.println(contaDaMarcela.saldo);
        System.out.println(contaDoPaulo.saldo);

    }
}