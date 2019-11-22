/* Escreva uma função chamada "swap" 
que troca os valores dos parâmetros recebidos */

#include <stdio.h>
void swap(float *a,float *b){
	float recebidos;
	recebidos=*a;
	*a=*b;
	*b=recebidos;
}

int main(void){
	float a,b;
	a=5;
	b=6;

	printf(" a=%f b=%f \n", a, b);
	swap(&a,&b);
	printf(" a=%f b=%f \n", a, b);

	return 0;

}