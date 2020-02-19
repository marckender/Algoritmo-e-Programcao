#include <stdlib.h>
#include <string.h>
#include "TabelaHash.h"

//definiçao de tipo Hash

struct hash{
    int qtd, TABLE_SIZE;
    struct aluno **itens;
};
