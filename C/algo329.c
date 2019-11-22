//Uma eleiçao presidencial, com 4 candidatos
//os votos sao inrormados pelos codigos
//1,2,3,4= votos para candidatos
//5= voto nulo && 6=voto branco

//calcule e imprime

//----total de votos para cada candidatos
//----total de votos nulos
//----total de votos em brancos
//-----percentual de votos em brancos e nulos sobre o total;


#include <stdio.h>

int main(){
	int cand1=0,cand2=0,cand3=0,cand4=0,vtnulo=0,vtbranco=0;
	int i,voto,tot;
	float percentnulo,percentbranco;
		printf("Digite uma opçao: (1 a 4=canditato)(5=nulo)(6=branco)(o=parar) : ");
		scanf("%d",&voto);

	while (voto !=0){

		if(voto==1){
			cand1+=1;
		}if(voto==2){
			cand2+=1;
		}if (voto==3){
			cand3+=1;
		}if (voto==4){
			cand4+=1;
		} if (voto==5){
			vtnulo+=1;
		} if (voto==6){
			vtbranco+=1;
		}

		printf("Digite uma opçao: (1 a 4=canditato)(5=nulo)(6=branco)(o=parar) : ");
		scanf("%d",&voto);
	}
		tot=cand1+cand2+cand3+cand4+vtnulo+vtbranco;

		percentnulo=(vtnulo*100)/tot;

		percentbranco=(vtbranco*100)/tot;
//

	printf("Candidato1 :%d\n canditato2: %d\n candidato3: %d\n candidato4: %d\n voto nulo: %d\n voto Branco: %d\n Percentual Nulo: %.2f Percentual Branco: %.2f",cand1,cand2,cand3,cand4,vtnulo,vtbranco,percentnulo,percentbranco);
	return 0;
}