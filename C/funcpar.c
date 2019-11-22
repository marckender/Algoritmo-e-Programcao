/*
Funçao chamada EPAR recebendo como parametro
um numero inteiro e retornar 1 se o numero for par
e 0 caso contrario.*/

#include <stdio.h>

int Epar(int x){

	if(x % 2==0){
		return 1;
	}else{
		return 0;
	}
}


int main(){

	int num ;

	printf("Digite um nuero: ");
	scanf("%d",&num);

		//int a=Epar(num);
		//printf("%d",a);

	
	if (Epar(num)==1){
		printf("e par\n");
	}else{
		printf("e impar\n");
	}


	return 0;
}