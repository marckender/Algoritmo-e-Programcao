#include <stdio.h>
#include <stdlib.h>

int main(){

  int x;
  printf("Digite um inteiro: ");
  scanf("%d",&x);

  if (x%2==0){
    printf("%d e par \n",x);
  }

  else{
    printf("%d e impar \n",x );
  }
 

}
