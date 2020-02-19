#include <stdio.h>
#include <math.h>

int fat1(int t,int x){
	int resultado1=1;
	for (int i=t; i>x; i--){

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

int combi(int x,int n,int ps){
    int i,fato1,fato2,c,sous;
    float q,db=0.0,t;
      

    for (i=0; i<=x; i++){
      
            t=0;
            q=1-ps;
		    sous=n-i;
		fato1=fat1(n,i);
		fato2=fat2(sous);

		c=fato1/fato2;

	//part 2
    

	ps=pow(ps,i);

	//part3
	q=pow(q,sous);

    t=c*ps*q;
    db+=t;

	//global

    }
    return db;

}



int main (){
int x,n,C,fato1,fato2;
	float ps,Dt;

	//leer os valors

	printf("Digite o numero de Observaçoes: \n");
	scanf("%d",&n);

	printf("Digite o numero de Sucesso: \n");
	scanf("%d",&x);

	printf("Digite a probabilidade de sucesso (valor Absoluto): \n");
	scanf("%f",&ps);

	//calcul de fator

	//probabilite dechec
    Dt=combi(n,x,ps);

	printf("A Distribuiçao Binomial eh: %4.f\n",Dt);

    return 0;
}