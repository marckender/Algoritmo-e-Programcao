

class conta{
    double saldo;
    int agencia=42;
    int numero;
    cliente titular;




    void deposita(double valor){
        this.saldo+=this.saldo +valor;
    }

    public boolean saca(double valor){
        if (this.saldo>=valor){
            this.saldo-=valor;
            return true;
        } else{
            return false;
        }
    }

    public boolean transfere(double valor, conta destino){
       if (this.saldo>=valor){
           this.saldo-=valor;
           destino.deposita(valor);
           return true;
       } else{
           return false;
       }
    }
}