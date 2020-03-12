#include <stdio.h>

void bubbleSort(int vet[],int x){
    int i, j,aux;
     for (i=0;i<x; i++){
        for (j=0;j<x-i;j++){
            if (vet[j]>vet[j+1]){
                aux=vet[j];
                vet[j]=vet[j+1];
                vet[j+1]=aux;
            }
        }
    }
}
int main (void){
    int vet[7]={29,10,14,14,25,8,37};
    int x=7;
    for (int i=0;i<x;i++){
        printf("%d ",vet[i]);
    }
    printf("\n\n");

    bubbleSort(vet,x);
    for(int i=0;i<x;i++){
        printf("%d ",vet[i]);
    }
    return 0;
}