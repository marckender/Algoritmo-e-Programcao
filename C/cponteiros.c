#include <stdio.h>

int main(){

	int *p,*p1 ,x, y;
	p=&x;
	if (p==p1){
		printf("Ponteiros iguais\n");

	}else{
		printf("Ponteiros diferentes\n");
	}
	return 0;
}