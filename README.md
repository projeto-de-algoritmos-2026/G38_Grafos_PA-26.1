# Rede Social com Grafos

Projeto em Python que simula uma rede social usando a teoria dos grafos. Cada usuario e tratado como um vertice, e cada amizade entre dois usuarios e representada como uma aresta.

O sistema possui uma interface grafica simples em `tkinter` e foi desenvolvido para demonstrar, de forma pratica, como grafos podem ser usados para modelar relacoes sociais.

## Objetivo

O objetivo deste projeto e construir uma simulacao de rede social com base em grafos, permitindo:

- cadastrar usuarios
- criar amizades entre usuarios
- visualizar conexoes existentes
- analisar a estrutura da rede

## Modelagem com Grafos

A rede social foi modelada como um **grafo nao direcionado**.

- cada usuario corresponde a um vertice
- cada amizade corresponde a uma aresta
- como a amizade e mutua, a conexao e registrada nos dois sentidos

### Exemplo conceitual

Se `Ana` e amiga de `Bruno`, o grafo registra:

- `Ana -> Bruno`
- `Bruno -> Ana`

Na pratica, isso significa que a amizade e compartilhada entre os dois usuarios, caracterizando um grafo nao direcionado.

## Funcionalidades

O programa atualmente oferece:

- cadastro de novos usuarios
- criacao de amizades
- listagem de usuarios
- exibicao das conexoes da rede
- visualizacao dos amigos de um usuario
- identificacao de amigos em comum
- busca do menor caminho entre dois usuarios, com destaque da distancia
- sugestoes de amizade (pessoas que voce talvez conheca) baseadas em amigos dos amigos
- analise basica da rede, como total de usuarios, total de conexoes e usuario mais conectado

## Interface

A interface foi criada inteiramente em Python com `tkinter`, sem depender de bibliotecas externas.

Ela possui:

- area para cadastro de usuarios
- area para criar conexoes entre dois usuarios
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
- busca por amizades
- calculo do grau de cada vertice

### 2. Regras de negocio

O sistema impede algumas operacoes invalidas:

- cadastrar usuario com nome vazio
- cadastrar usuario repetido
- criar amizade entre o mesmo usuario
- criar amizade com usuarios inexistentes
- duplicar uma amizade ja existente

### 3. Analise da rede e caminhos

O programa permite observar algumas propriedades do grafo:

- quantidade total de vertices
- quantidade total de arestas
- grau de cada usuario
- usuario com maior numero de conexoes
- amigos em comum entre usuarios
- menor caminho entre dois usuarios (usando Dijkstra com distancias unitarias)
- sugestoes de amizade calculadas com amigos dos amigos (BFS limitada a dois niveis)

## Exemplo de Uso

Ao iniciar o programa, alguns usuarios ja sao carregados para demonstracao:

- Ana
- Bruno
- Carla
- Diego
- Elisa

Com isso, o usuario pode testar imediatamente a criacao de novas conexoes e a visualizacao da rede.

## Aplicacao Academica

Este projeto e adequado para atividades e apresentacoes sobre:

- teoria dos grafos
- estruturas de dados
- modelagem de redes sociais
- representacao de relacionamentos em sistemas computacionais

## Possiveis Melhorias Futuras

- remocao de usuarios
- remocao de amizades
- persistencia em arquivo ou banco de dados
- visualizacao grafica do grafo com desenho dos vertices e arestas

## Conclusao

O projeto demonstra de forma clara como grafos podem ser aplicados na simulacao de uma rede social. A separacao entre interface e estrutura de dados facilita a manutencao do codigo e torna o sistema mais organizado para evolucoes futuras.
