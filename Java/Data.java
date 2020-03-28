// Faça um programa em Java que utilize um objeto da classe Data.
// a classe data possui atributos inteiros que representaem o mes,dia,hora,minutos
// A lem disso a classe Date possui dois metodos: 
// um que imprime todos os atributos do objetos, 
//e outro que imprime na tela "AM" se a hora do objeto for menor que 12
//ou "PM" se a hora for maior que 12.


public class Data{
    public int mes;
    public int dia;
    public int hora;
    public int minutos;

    public void hora(){
        if (this.hora<12){
            System.out.println(this.hora+ " AM");
        }else{
            System.out.println(this.hora + " PM");
        }
    }
}