#include <stdio.h>


int fatorial (int x){

	int resultado;

	if (x==0){
		resultado=1;

	}else{
		resultado=x*fatorial(x-1);
	}
	return resultado;
}

int main(void){
	int numero,resultado;

	printf("Digite um numero inteiro: ");
	scanf("%d",&numero);

	resultado=fatorial(numero);

	printf("O fatorial eh %i\n ",resultado);

	return 0;
}