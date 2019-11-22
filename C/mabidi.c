#include <stdio.h>

int main(void){

	int matriz[3][3]={ 	{1,2,3},
						{4,5,6},
						{7,8,9}	};
	int soma=0;

	for (int m=0;m<3;m++){
		for (int n=0;n<3;n++){
			soma=soma+matriz[m][n];
		}
		
	}

	printf("a soma: %i",soma);


	return 0;
}