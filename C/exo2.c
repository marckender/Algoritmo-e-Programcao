/*Escreva um código que contenha duas variáveis para números reais.
 Compare seus endereços e exiba o maior endereço.*/



#include <stdio.h>
int main(){
	float a=3.2;
	float b=4.5;

	float *p;
			p=&a;
			p=&b;
  
if (&a> &b) {
 	printf("variavel A tem o maior endereco de memoria %p \n",&a);
}

else{
   	 printf("variavel B tem o maior endereco de memoria %p \n" ,&b);
}

}