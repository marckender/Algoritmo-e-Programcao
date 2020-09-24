#include <stdio.h>

#define MAX 15
int main() {

  char buf[Max];

  fgets(buf, Max, stdin);
  printf("string is : %d\n", buf);

  return 0;
}