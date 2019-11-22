#include <stdio.h>
#include <math.h>

int fat1(int t,int sous){
	int resultado1=1;
	for (int i=t; i>sous; i--){

		resultado1=resultado1*i;
	}
	return resultado1;
}
int fat2(int t1){
	int resultado2;

if (t1==0){
	resultado2=1;
}else{
	resultado2=t1*fat2(t1-1);
	}
return resultado2;
}


int main(){

	int x,n,C,fato1,fato2,sous;
	float Db,ps,q;

	//leer os valors

	printf("Digite o numero de Observaçoes: \n");
	scanf("%d",&n);

	printf("Digite o numero de Sucesso: \n");
	scanf("%d",&x);

	printf("Digite a probabilidade de sucesso (valor Absoluto): \n");
	scanf("%f",&ps);

	//calcul de fator

	//probabilite dechec

		q=1-ps;
		sous=n-x;

		fato1=fat1(n,sous);
		fato2=fat2(x);

		C=fato1/fato2;

	//part 2

	ps=pow(ps,x);

	//part3
	q=pow(q,sous);

	//global

	Db=C*ps*q;//Distribuiçao Binomial

	printf("A Distribuiçao Binomial eh: %f\n",Db);




	return 0;
}