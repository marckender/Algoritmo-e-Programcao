struct aluno{
    int matricula;
    char nome [30];
    float n1,n2,n3;

};

typedef struct hash Hash;
Hash* criaHashc(int TABLE_SIZE);

void liberaHash(Hash* ha);
int valorString(char *str);

int insereHash_semColisao(Hash* ha,struct aluno al);
int buscaHash_semColisao(Hash* ha,int mat,struct aluno* al);

int insereHash_enderAberto(Hash*ha,struct aluno al);
int buscaHash_enderAberto (Hash* ha,int mat,struct aluno* al);