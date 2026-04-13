# Rede Social com Grafos

Projeto em Python que simula uma rede social usando teoria dos grafos. Cada usuario e tratado como um vertice, e cada amizade entre dois usuarios e representada como uma aresta.

O sistema possui interface grafica simples em `tkinter` e foi desenvolvido para mostrar, na pratica, como grafos podem representar relacionamentos sociais.

## Objetivo

O objetivo do projeto e construir uma simulacao de rede social com base em grafos, permitindo:

- cadastrar usuarios
- criar amizades entre usuarios
- visualizar conexoes existentes
- analisar a estrutura da rede
- buscar caminhos entre usuarios
- exibir a rede graficamente

## Modelagem com Grafos

A rede social foi modelada como um **grafo nao direcionado**.

- cada usuario corresponde a um vertice
- cada amizade corresponde a uma aresta
- como a amizade e mutua, a conexao e registrada nos dois sentidos

### Exemplo conceitual

Se `Ana` e amiga de `Bruno`, o grafo registra:

- `Ana -> Bruno`
- `Bruno -> Ana`

Na pratica, isso caracteriza uma relacao bidirecional, propria de um grafo nao direcionado.

## Funcionalidades

O programa atualmente oferece:

- cadastro de novos usuarios
- criacao de amizades
- listagem de usuarios
- exibicao das conexoes da rede
- visualizacao dos amigos de um usuario
- identificacao de amigos em comum
- busca do menor caminho entre dois usuarios
- sugestoes de amizade baseadas em amigos dos amigos
- visualizacao grafica da rede em formato de teia
- analise basica da rede, como total de usuarios, total de conexoes e usuario mais conectado

## Interface

A interface foi criada inteiramente em Python com `tkinter`, sem depender de bibliotecas externas.

Ela possui:

- area para cadastro de usuarios
- area para criar conexoes entre dois usuarios
- area para buscar o caminho mais curto entre dois usuarios
- botao para mostrar a rede graficamente
- lista de usuarios cadastrados
- painel com as conexoes da rede
- painel de detalhes do usuario selecionado
- painel de analise da rede

## Estrutura do Projeto

```text
G38_Grafos_PA-26.1/
|-- app.py
|-- grafo.py
|-- README.md
```

### Arquivos principais

- `app.py`: interface grafica e integracao com a estrutura de dados
- `grafo.py`: implementacao do grafo da rede social
- `README.md`: documentacao do projeto

## Como Executar

### Requisitos

- Python 3 instalado

### Execucao

No terminal, dentro da pasta do projeto, execute:

```bash
python app.py
```

## Como o Projeto Funciona

### 1. Estrutura de dados

O modulo `grafo.py` utiliza uma lista de adjacencia para representar a rede:

- a chave do dicionario e o nome do usuario
- o valor associado e um conjunto com seus amigos

Essa abordagem facilita:

- insercao de usuarios
- criacao de conexoes
- consulta dos vizinhos de cada vertice
- calculo do grau de cada usuario

### 2. Regras de negocio

O sistema impede algumas operacoes invalidas:

- cadastrar usuario com nome vazio
- cadastrar usuario repetido
- criar amizade entre o mesmo usuario
- criar amizade com usuarios inexistentes
- duplicar uma amizade ja existente

### 3. Analise da rede

O programa permite observar algumas propriedades do grafo:

- quantidade total de vertices
- quantidade total de arestas
- grau de cada usuario
- usuario com maior numero de conexoes
- amigos em comum entre usuarios
- menor caminho entre dois usuarios
- sugestoes de amizade
- visualizacao da rede organizada por niveis

## Algoritmos de Grafos Utilizados

Esta secao descreve os principais algoritmos e tecnicas de grafos usados no projeto e onde eles aparecem.

### 1. BFS - Busca em Largura

A BFS (`Breadth-First Search`) percorre o grafo por niveis, visitando primeiro os vizinhos mais proximos e depois os mais distantes.

Ela e usada em:

- `grafo.py`, no metodo `bfs(origem)`
- `grafo.py`, no metodo `caminho_mais_curto(origem, destino)`
- `app.py`, no botao `Mostrar rede`

No projeto, a BFS serve para:

- gerar a ordem de visita dos usuarios
- descobrir o nivel de cada usuario em relacao ao usuario inicial
- definir predecessores durante a exploracao
- organizar a visualizacao da rede em formato de teia

### 2. Menor Caminho em Grafo Nao Ponderado

Como todas as amizades possuem o mesmo peso, o menor caminho entre dois usuarios pode ser encontrado com BFS.

Esse algoritmo e usado em:

- `grafo.py`, no metodo `caminho_mais_curto(origem, destino)`
- `app.py`, na funcionalidade de busca entre origem e destino

O resultado apresentado ao usuario inclui:

- a sequencia de vertices do caminho
- a distancia em numero de arestas

### 3. Lista de Adjacencia

A representacao do grafo foi feita com lista de adjacencia, uma estrutura eficiente para grafos esparsos como redes sociais pequenas e medias.

Ela e usada em:

- `grafo.py`, no atributo `_adjacencias`

Essa estrutura e a base para:

- armazenar usuarios
- registrar amizades
- consultar vizinhos
- percorrer o grafo

### 4. Calculo do Grau dos Vertices

O grau de um vertice corresponde ao numero de conexoes de um usuario.

Esse calculo e usado em:

- `grafo.py`, no metodo `grau_usuario(usuario)`
- `grafo.py`, no metodo `usuario_mais_conectado()`
- `app.py`, no painel `Analise da Rede`

Com isso, o sistema consegue identificar:

- quantas amizades cada usuario possui
- qual usuario possui mais conexoes

### 5. Interseccao de Vizinhos

Para descobrir amigos em comum, o sistema compara os conjuntos de vizinhos de dois usuarios.

Essa tecnica e usada em:

- `grafo.py`, no metodo `amigos_em_comum(usuario_a, usuario_b)`
- `app.py`, no painel `Detalhes do Usuario`

### 6. Recomendacao de Amigos

As recomendacoes sao baseadas na ideia de amigos dos amigos. O sistema analisa usuarios a distancia 2 que ainda nao possuem conexao direta com o usuario principal.

Esse processo e usado em:

- `grafo.py`, no metodo `recomendar_amigos_bfs(usuario, limite=5)`
- `app.py`, na secao `Pessoas que voce talvez conheca`

Na pratica, a recomendacao funciona contando quantos amigos em comum existem entre o usuario e cada candidato.

## Exemplo de Uso

Ao iniciar o programa, alguns usuarios ja sao carregados para demonstracao:

- Ana
- Bruno
- Carla
- Diego
- Elisa

Com isso, o usuario pode testar imediatamente a criacao de novas conexoes, a busca de caminhos e a visualizacao da rede.

## Aplicacao Academica

Este projeto e adequado para atividades e apresentacoes sobre:

- teoria dos grafos
- estruturas de dados
- modelagem de redes sociais
- busca em largura
- menor caminho em grafos nao ponderados

## Possiveis Melhorias Futuras

- remocao de usuarios
- remocao de amizades
- persistencia em arquivo ou banco de dados
- destaque visual do menor caminho encontrado
- animacao da ordem de visita da BFS

## Conclusao

O projeto demonstra de forma clara como grafos podem ser aplicados na simulacao de uma rede social. A separacao entre interface e estrutura de dados facilita a manutencao do codigo e torna o sistema mais organizado para evolucoes futuras.
Link para o vídeo: https://drive.google.com/file/d/1HpClLeTrtk8XtbwES8e6ZKqWGk9ULDdI/view?usp=sharing
