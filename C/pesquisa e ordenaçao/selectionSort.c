#include <stdio.h>
#include <stdio.h>

void selectionSort(int vetor[],int n){
    int menor,aux;

    for (int i=0; i<n-i; i++){
        menor=i;
        for (int j=i+1; j<n; j++){
            if ( vetor[menor] > vetor[j] ){
                menor=j;
            }
        }
            if( i!=menor){
                aux=vetor[i];
                vetor[i]=vetor[menor];
                vetor[menor]=aux;
            }

    }
}
int main(void){
    int vetor[]={29,0,14,14,25,8,37};
    int n=7;
    for (int i=0;i<n;i++){
        printf("%d ",vetor[i]);
    }
    printf("\n\n");

    selectionSort(vetor, n);
    for (int i=0;i<n;i++){
       printf("%d ",vetor[i]); 
    }
    printf("\n\n");

    return 0;
}