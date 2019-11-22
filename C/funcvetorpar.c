

#include <stdio.h>

int Epar(int x){

	if(x % 2==0){
		return 1;
	}else{
		return 0;
	}
}


int main(){

	int vetor[0];

	for (int i=0; i<10;i++){

		printf("Digite um numero: ");
		scanf("%d",&vetor[i]);
	}

	for (int i=0;i<10;i++){

				if (Epar(vetor[i])==1){
				printf("%i e par\n",vetor[i]);
			}else{
				printf("%i e impar\n",vetor[i]);
			}

	}

	return 0;
}