public class criaConta{
        public static void main(String[] args) {
            conta primeiraConta =new conta();
            primeiraConta.saldo=200;
            

            conta segundaConta=new conta();
            segundaConta.saldo=50;

            System.out.println("Primeira Conta tem: " + primeiraConta.saldo );
            System.out.println("Segunda Conta tem: " + segundaConta.saldo );

            System.out.println(primeiraConta.agencia);
            System.out.println(primeiraConta.numero);

            System.out.println(segundaConta.agencia);


        }
}