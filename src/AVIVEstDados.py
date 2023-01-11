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

#Objetivo do Merge Sort Externo é ordenar um arquivo sem extrapolar a memória RAM para arquivos muito grandes, para isso, 
#dividimos o arquivo em um certo número de sub-arquivos (n_chunks), ordenamos cada um desses pelo Merge Sort, e depois 
#juntamos esses arquivos para recuperar o original.

import tempfile
import time

class Merge_Sort_Externo(): #Vamos usar OO para lidar com esse algoritmo
    def __init__(self, campo_agrupamento, func_agregacao, tam_chunks):
        """função de agregação: pode ser sum ou count"""
        self.campo_agrupamento = campo_agrupamento 
        self.func_agregacao = func_agregacao
        self.chunks_ordenados_temp = []
        self.tam_chunks = tam_chunks # tamanho dos sub-arquivos a serem criados, no nosso programa, equivale a 1/10 do tamanho do total 

    def two_way_merge(self,arq1,arq2):
        """Essa função recebe dois arquivos ordenados, ordena seus elementos e retorna
o arquivo ordenado."""
        A = arq1.read().split('\n')[:-1] #lê o arq1 e não utiliza o último termo, pois é um espaço vazio
        
        B = arq2.read().split('\n')[:-1]
        
        A = [int(i) for i in A]
        
        B = [int(i) for i in B]
        
        C = []
        
        i = j = 0

        #Dados os dois subgrupos, vemos qual deve entrar na posição correta
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        
        while i < len(A):
                C.append(A[i])
                i += 1
        while j < len(B):
            C.append(B[j])
            j += 1

        #queremos retornar o arquivo, e não a lista (poderia ser mais rápido retornar somente a lista,
        #mas pela maneira que fizemos o código, isso é o que funciona
        C = [str(C[i])+'\n' for i in range(len(C))] 
        C_arq = tempfile.NamedTemporaryFile(mode = 'w+', delete=False)
        C_arq.writelines(C)
        C_arq.seek(0)

        return C_arq
        
    
    def merge_chk(self):
        '''Essa função junta todos os arquivos menores ordenados em um único arquivo ordenado, de dois em dois'''
        n = len(self.chunks_ordenados_temp)
        
        for _ in range(n-1):
            C_arq = self.two_way_merge(self.chunks_ordenados_temp[0],self.chunks_ordenados_temp[1])
            self.chunks_ordenados_temp = self.chunks_ordenados_temp[2:]
            self.chunks_ordenados_temp.insert(0,C_arq)
            
        return C_arq
    
    def group_by(self):
        "Tendo o arquivo original ordenado, apenas fazemos o group-by pelos campos de agrupamento para as funções de agregação 'sum' e 'count'"
        soma = 0
        cont_homens = 0
        cont_mulheres = 0
        cont_capital = 0
        cont_baixada = 0
        cont_serrana = 0
        
        arq_final = self.merge_chk() #junta os arquivos menores em um arquivo total ordenado
        
        A = arq_final.read().split('\n')[:-1]
        
        A = [int(i) for i in A]
        
        if self.func_agregacao == 'sum': #se a função for 'sum', basta somar os elementos do arquivo.
            #A função de agregação 'sum' só funciona para os campos de agregação 'idade' e 'renda'.
            soma = sum(A)
            
        elif self.func_agregacao == 'count': #se a função for 'count', utilizamos uma legenda para saber onde somar
            #A função de agregação 'count' só funciona para os campos de agregação 'sexo' e 'regiao'
            if self.campo_agrupamento == 'sexo':
                for i in A:
                    if i == 0:
                        cont_homens += 1
                    elif i == 1:
                        cont_mulheres += 1
            elif self.campo_agrupamento == 'regiao':
                for i in A:
                    if i == 0:
                        cont_capital += 1
                    elif i == 1:
                        cont_baixada += 1
                    elif i == 2:
                        cont_serrana += 1

        if self.func_agregacao == 'sum':
            print(f"""{self.campo_agrupamento}   Qnt
Total  {soma}""")
        elif self.func_agregacao == 'count':
            if self.campo_agrupamento == 'sexo':
                print(f"""{self.campo_agrupamento}   Qnt
M  {cont_homens}
F  {cont_mulheres}""")
            elif self.campo_agrupamento == 'regiao':
                print(f"""{self.campo_agrupamento}   Qnt
Capital  {cont_capital}
Baixada Fluminense  {cont_baixada}
Regiao Serrana   {cont_serrana}""")


    def mergeSort(self,array):
        "Método de ordenação Merge Sort"
        if len(array) > 1:

            #  r é o ponto médio do array, dividimos o array em dois.
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            # Ordenamos as duas metades.
            self.mergeSort(L)
            self.mergeSort(M)

            i = j = k = 0

            # Dados os dois subgrupos, vemos qual deve entrar na posição correta
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

        # Se acabarem os elementos de um dos subgrupos, ordenamos o que sobrou
        # do outro subgrupo.
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
    def dividir_arquivo(self,arquivo):
        "Divide o arquivo maior em chunks menores, ordena e cria arquivos temporários com eles."
        file_arquivo = open(arquivo)
        
        buffer_temp = [] #lista temporária para criar os arquivos menores
        tam = 0
        
        while True:
            aux = file_arquivo.readline() 
            if not aux: #quando não tiver mais o que ler do arquivo, o laço é rompido e pegamos o tamanho total do arquivo
                self.tam_arq_final = tam
                break
            indx = aux.split(';')
            
            #podemos agora utilizar os campos de agrupamento para fazer o 'group-by'
            if self.campo_agrupamento == 'sexo': 
                num = indx[2]
                if num == "M":
                    num = 0
                else:
                    num = 1
                self.num_cat = 2 #num_cat é o número de categorias diferente para cada campo qualitativo
                
            elif self.campo_agrupamento == 'regiao':
                num = indx[3]
                if num == 'Capital':
                    num = 0
                elif num == 'Baixada Fluminense':
                    num = 1
                else:
                    num = 2
                self.num_cat = 3
            elif self.campo_agrupamento == 'idade':
                num = int(indx[1])
            elif self.campo_agrupamento == 'renda':
                num = int(indx[4])
            
            buffer_temp.append(num)
            tam += 1
            if tam % self.tam_chunks == 0: #Organizando o tamanho de cada um dos subarquivos
                self.mergeSort(buffer_temp) #Ordenando o subarquivo pelo Merge Sort
                #buffer_temp = sorted(buffer_temp) (se utilizarmos o Timsort - algoritmo interno do python, fica bem mais rápido)
                
                #Depois de ordenado, temos que criar
                #os subarquivos menores, por isso transformamos para string, para conseguir inserir em um arquivo.
                
                buffer_temp = [str(buffer_temp[i])+'\n' for i in range(len(buffer_temp))]
                
                file_temp = tempfile.NamedTemporaryFile(mode = 'w+', delete=False) #Aqui criamos os subarquivos de forma temporária
                file_temp.writelines(buffer_temp)
                file_temp.seek(0)
                self.chunks_ordenados_temp.append(file_temp) #appendamos os arquivos menores em uma lista da classe
                buffer_temp = [] #Depois de criarmos o subarquivo, zeramos o buffer e recomeçamos o loop

file = 'bd_mergesort.txt'

tam_chunks = 100000

st_1 = time.perf_counter()

obj = Merge_Sort_Externo('sexo','count',tam_chunks)
obj.dividir_arquivo(file)
print(f'O tempo gasto p/ dividir foi de {time.perf_counter() - st_1:.2f} segundos')

st_2 = time.perf_counter()
obj.group_by()
print(f'O tempo gasto p/ juntar foi de {time.perf_counter() - st_2:.2f} segundos')

st_3 = time.perf_counter()

d_sexo = {'M': 0, 'F': 0}

f = open(file)
for linha in f.readlines():
    indx = linha.split(';')
    if indx[2] == 'M':
        d_sexo['M'] += 1
    elif indx[2] == 'F':
        d_sexo['F'] += 1

print(f"""sexo  Qnt
M  {d_sexo['M']}
F  {d_sexo['F']}""")

print(f'O tempo gasto utilizando o dict foi de {time.perf_counter() - st_3:.2f} segundos')
