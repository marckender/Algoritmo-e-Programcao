#include <stdio.h>

int main(){
  int num,horas;

  float salario,SALARY;

  scanf("%d",&num);
  scanf("%d",&horas);
  scanf("%f",&salario);

  SALARY = horas*salario;

    printf("NUMBER = %d\n",num);
    printf("SALARY = U$ %.2f\n",SALARY);

  return 0;
}
