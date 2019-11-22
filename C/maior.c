#include <stdio.h>
#include <stdlib.h>

int main(){
 int num;
 printf("Digite um numero: ");
 scanf("%d", &num );

 if (num==0){
   printf("O numero e igual a 0 \n");
 }
 else{
   if (num<0)
      printf("O numero e menor que 0 \n");
    else
      printf("O numero e maior que 0\n");
 }

  return 0;

}
