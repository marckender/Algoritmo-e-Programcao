/*
Leia números de matrículas de alunos e 
armazene-os em um vetor até o vetor ser preenchido por 10 matrículas.
 Esses números são distintos, 
ou seja, o vetor não armazenará valores repetidos.
*/

#include <stdio.h>

int main(){

    int x, numero[x],vetor[10],i;

    for (i=0;i<10;i++){

        printf("Digite um numero inteiro: ");
        scanf("%d",numero);
    }

    for(int x=0;x<10;x++){
        if(vetor[x]!=numero[x]){
            vetor[x]=numero[x];
        }    
    }
    printf("&d",vetor[x]);
    
}