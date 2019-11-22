/* Implemente um código que tenha duas variáveis para inteiros (a, b).
 Em seguida uma função que retorne a soma do cubo dos dois inteiros.
 A função também deve armazenar o cubo de "a" e "b" nas variáveis de origem. */

#include <stdio.h>
#include <math.h>





 int soma(int *a, int *b){

 		int n=(*a)*(*a)*(*a);
 		int m=(*b)*(*b)*(*b);

 		*a=n;
 		*b=m;
 		return n+m;
 }


int main(){
	int x,y;
	x=6;
	y=7;

	int t=soma(&x,&y);
	printf("%p",&t);

	return 0;
}