/**
 * testaMetodo
 */
public class testaMetodo {

    public static void main(String[] args) {
        conta contaDoPaulo= new conta();
        contaDoPaulo.saldo=100;
        contaDoPaulo.deposita(50);

        System.out.println(contaDoPaulo.saldo);

    }
}