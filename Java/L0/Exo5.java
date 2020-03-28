//  Faça um programa em Java imprima na tela a seguinte frase:
// 1 Java atrapalha muita gente
// 2 Java atrapalham atrapalham muita gente
// 3 Java atrapalham atrapalham atrapalham muita gente
// 4 Java atrapalham atrapalham atrapalham atrapalham muita gente
// …
// 100 Java atrapalham atrapalham ... atrapalham atrapalham muita gente

package L0;

/**
 * Exo5
 */
public class Exo5 {

    public static void main(String[] args) {
        
        for (int i=1;i<=100;i++){
            String b=" Atrapalha ".repeat(i);
            System.out.println(i+ " "+ (b) + " muita gente");
        }
    }
}