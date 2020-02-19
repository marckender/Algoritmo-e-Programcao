public class fatoriel{
    public static void main(String[] args) {
        int fat=1;
        for(int i=1;i<11;i++){
             fat*=i;
             System.out.println("o fatoriel de " +i +" eh " + fat);
        }
    }
}