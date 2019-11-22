//Distribuiçao Accumulada

#include<stdio.h>
#include<math.h>
int fat1(int t,int sous);
int fat2(int t1);
int  myfuncao(int n,int x,float ps){
	int fat3,fat4,sous,c;
	float q,db=0.0,t,aux,w,z,a;
    long double p;
	q=1-ps;
	for(int i=0;i<=x;i++){
		t=0;
		aux=ps;
		z=q;
		p=0.0;
		sous=n-i;
		fat3=fat1(n,sous);
		fat4=fat2(i);
		c=fat3/fat4;
		p=pow(0.15,5);
        printf("%ld\n",p);
		a=pow(z,sous);
		t=c*p*a;
		db+=t;

	}
	//printf("%.4f\n",db);
}
int main(){
  int n,x;
  float ps,Dt;
  printf("digite o numero de observacoes:");
  scanf("%d",&n);
  printf("digite o numero de sucesso:");
  scanf("%d",&x);
  printf("digite o probabilidade de sucesso:");
  scanf("%f",&ps);
  myfuncao(n,x,ps);

  return 0;

}
int fat1(int t,int sous){
  int resultado1=1;
  for(int i=t;i>sous;i--){
    resultado1=resultado1*i;
  }

  return resultado1;
}
int fat2(int t1){
  int resultado2;
  if(t1==0){
    resultado2=1;
  }else{
    resultado2=t1*fat2(t1-1);
  }
  return resultado2;

}