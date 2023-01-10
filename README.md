![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Avaliação IV - Ordenação por Merge-Sort externo

### Descrição de implementação Merge-Sort externo:

Desenvolver um módulo, em C++ ou Python, que implementa a ordenação de um arquivo de registros pelo método Merge-Sort Externo e utilizá-lo para solucionar o problema descrito a seguir.

É comum aplicações computacionais manipularem arquivos de dados muitos extensos. Muitos desses arquivos possuem tamanhos maiores que a memória principal (RAM) disponível para a carga de dados da aplicação. Nesses casos são utilizadas estruturas de dados e algoritmos específicos para que as operações com tais tipos de arquivos não sejam muito ineficientes, ou mesmo demoradas, algo que se torna crítico quando a aplicação é utilizada por múltiplos usuários concomitantemente e, assim, poderá haver múltiplos acessos aos arquivos de dados extensos.

Um exemplo bem comum de operação feita em análise de dados cadastrais, que envolve tais tipos de arquivos extensos, é aquela que realiza o “cálculo de funções de agregação em agrupamentos de registros”, ou seja, aplicar uma função de agregação, tais como, realizar uma contagem de registros em cada agrupamento, ou o somatório dos valores em um dos seus atributos, ou a média, ou outra função estatística qualquer. O critério de agrupamento de registros se dá tão somente pelo valor em comum de algum dos seus atributos, ou conjunto de atributos.

Essas operações em geral são aplicadas em “arquivo de registros de um cadastro”, que pode ter um formato binário ou texto, onde cada linha corresponde aos dados de um certo registro, e é subdivida em vários campos de dados (atributos), de diversos tamanhos e tipos. Por exemplo, em um cadastro de Aluno de uma Universidade, o registro de cada “Aluno” teria os campos (atributos) DRE, Nome do Aluno, CPF do Aluno, Data de Nascimento, Sexo, Endereço (composto por logradouro, número, bairro etc.), lista de telefones, Nome da Mãe, Nome do Pai etc. Um típico exemplo são arquivos de dados no formato .CSV. 

Esses arquivos podem até ter alguma “organização primária”, porém o normal é não estar ordenado pelos valores de nenhum dos seus campos. Um exemplo de “cálculo de funções de agregação em agrupamentos de registros”, neste caso, poderia ser o cálculo de quantos alunos em cada bairro existem no cadastro, ou mesmo refinar, agrupando em cada bairro por sexo, ou faixa etária. Outro exemplo, poderia ser calcular a média de idade dos alunos em cada bairro.

Um algoritmo trivial para esse procedimento é realizar a ordenação do arquivo pelo valor da “chave de agrupamento” e, posteriormente, percorrer o arquivo ordenado aplicando as funções de agregação a cada grupo formado pela ordenação.

Assuma o arquivo de registro no formato texto (ou mesmo .CSV), onde cada registro está armazenado em uma linha do arquivo texto, e os campos na linha são separados por um caractere especial chamado “delimitador” (em geral o caractere ‘;’). Desenvolva um procedimento que receba como parâmetros a lista de campos que compõem a “chave de agrupamento”, e uma lista de pares de “funções de agregação” com o respectivo campo onde será aplicada a função. O procedimento deverá:

1. Ordenar os registros no arquivo, criando um novo arquivo ordenado, pelo valor do “campo de agrupamento”, usando o algoritmo de Merge-Sort externo.

2. Retornar um arquivo com os primeiros campos compostos dos valores do “campo de agrupamento” e, em seguida, os valores resultantes da aplicação de cada “função de agregação” aos seus respectivos campos. 

3. O cabeçalho desses campos no arquivo podem ser tão somente o nome de cada campo, por exemplo “Bairro” e “Sexo”. No caso do resultado dos campos com os resultados das funções de agregação, o nome do campo poderia ser o nome da função seguida do nome do campo, por exemplo, “Somatório de CPF”.
