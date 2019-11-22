//leia dois conjunto de num inteiros
//de 10 e de 20 elementos
//podem se repetir mas nao podem aparecer repetidas na saida

#include <stdio.h>

int main(){
	int x=0,y=0;
	int vet1[5],vet2[8],vet3[x];


	for (int i=0;i<5;i++){
		printf("Digite um vetor de [10] elementos: ");
		scanf("%d",&vet1[i]);
	}

	//
	for (int j=0;j<8;j++){
	printf("Digite mais um de [20] elementos: ");
	scanf("%d",&vet2[j]);
	}

	//
	for (int i=0; i<10;i++){
		for(int j=0;j<20;j++){

			if (vet1[i]==vet2[j]){
				vet3[x]=vet1[j];
					x+=1;
			}
		}
	}

		for (int i=0;i<x;i++){
			printf(" %d",vet3[i]);
		}

	return 0;
}