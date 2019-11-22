/* crie um programa que pede que o usuario 
digite 4 notas de 0 a 10(tipo float) de 4 alunos e
 os valores deverao ser amazenados em uma matriz bidimensional
 Faça a media das notas de cada aluno e armazene as 4 media
 em um vetor.
 por fim coloque na tela do usaurio uma mensagem 
 informado a mediade cada aluno
 */


#include <stdio.h>


int main(){

	float notas[4][4]={0};
	float vetor[4]={0};

	float media=0;
	float soma=0; 

	printf("insira as 4 notas: \n");

	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			scanf("%f ", &notas[i][j]);

			soma+=notas[i][j];

		}
		media=soma/4;

		 vetor[i]=media;

		 printf("insira mais 4 notas: \n");
	}
	for (int i=0; i<4; i++){
		printf("a media do aluno %i eh %.2f\n",i+1, vetor[i]);
	}





	return 0;
}