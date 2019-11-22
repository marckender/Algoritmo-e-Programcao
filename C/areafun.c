#include <stdio.h>

float calcularAreaRetang(float base,float altura){
	float area=base*altura;

	return area;
}

int main(){

	 float area=calcularAreaRetang(10.0,20.0);

	printf("A area eh: %f\n",area);
	return 0;
}