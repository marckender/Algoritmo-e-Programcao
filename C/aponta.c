#include <stdio.h>

int main(){

	int x=10;
	int *p;

	//ponteiro p aponta para a variavel x

	p= &x;

	printf("x= %d\n",x);
	printf("p= %p\n",p);
	printf("*p= %d\n",*p);
	return 0;
}