'''UFRJ - Universidade Federal do Rio de Janeiro
MAE015 - Tóp. Especiais em Engenharia de dados A: Estrutura de dados
Autores:
Nome: Rhuan Justo
DRE: 118043398

Nome: Davi Richards
DRE: 119022078

Nome: Sebastião Rodrigo
DRE: 117099621

Nome: Yuri Ferreira Melo
DRE: 120081378'''

import random
# Cria o banco de dados a ser utilizado na avaliação 4
# Cada linha possui 5 campos de registros, a saber:
# número de identidade, idade, sexo, região e renda.
# long int, int, char(str), str, int

f = open('bd_mergesort.txt', 'w') 

n = 1000000
step = 420

for _ in range(n):
    #ident;idade;sexo;regiao;renda
    ident = 123456789 + step
    idade = random.randint(18,60)
    aux = random.randint(0,1)
    if aux == 0:
        sexo = 'F'
    else:
        sexo = 'M'
    aux2 = random.randint(0,2)
    if aux2 == 0:
        regiao = 'Capital'
    elif aux2 == 1:
        regiao = 'Baixada Fluminense'
    else:
        regiao = 'Regiao Serrana'
    
    renda = random.randint(0,5000)
    linha = f'{ident};{idade};{sexo};{regiao};{renda}\n'
    step += 69
    f.write(linha)
    
f.close()
