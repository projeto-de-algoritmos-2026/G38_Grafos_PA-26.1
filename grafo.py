class RedeSocialGrafo:
    """Representa uma rede social como um grafo nao direcionado.

    - Cada usuario e um vertice.
    - Cada amizade e uma aresta.
    - Como a amizade e mutua, a conexao e armazenada nos dois sentidos.
    """

    def __init__(self):
        # Lista de adjacencia: cada vertice aponta para os vertices conectados.
        self._adjacencias = {}

    def adicionar_usuario(self, nome):
        nome = nome.strip()
        if not nome:
            raise ValueError("Informe um nome de usuario valido.")
        if nome in self._adjacencias:
            raise ValueError("Esse usuario ja existe.")
        self._adjacencias[nome] = set()

    def usuario_existe(self, nome):
        return nome in self._adjacencias

    def criar_amizade(self, usuario_a, usuario_b):
        if usuario_a == usuario_b:
            raise ValueError("Um usuario nao pode ser amigo de si mesmo.")
        if not self.usuario_existe(usuario_a) or not self.usuario_existe(usuario_b):
            raise ValueError("Selecione usuarios validos.")
        if usuario_b in self._adjacencias[usuario_a]:
            raise ValueError("Essa amizade ja existe.")

        # Grafo nao direcionado: a aresta e registrada para os dois usuarios.
        self._adjacencias[usuario_a].add(usuario_b)
        self._adjacencias[usuario_b].add(usuario_a)

    def listar_usuarios(self):
        return sorted(self._adjacencias.keys())

    def listar_conexoes(self):
        conexoes = []
        visitadas = set()

        for usuario, amigos in self._adjacencias.items():
            for amigo in amigos:
                aresta = tuple(sorted((usuario, amigo)))
                if aresta in visitadas:
                    continue
                visitadas.add(aresta)
                conexoes.append(aresta)

        return sorted(conexoes)

    def obter_amigos(self, usuario):
        if not self.usuario_existe(usuario):
            return []
        return sorted(self._adjacencias[usuario])

    def amigos_em_comum(self, usuario_a, usuario_b):
        if not self.usuario_existe(usuario_a) or not self.usuario_existe(usuario_b):
            return []
        return sorted(self._adjacencias[usuario_a] & self._adjacencias[usuario_b])

    def quantidade_usuarios(self):
        return len(self._adjacencias)

    def quantidade_conexoes(self):
        return len(self.listar_conexoes())

    def grau_usuario(self, usuario):
        if not self.usuario_existe(usuario):
            return 0
        return len(self._adjacencias[usuario])

    def usuario_mais_conectado(self):
        usuarios = self.listar_usuarios()
        if not usuarios:
            return None, 0

        usuario = max(usuarios, key=self.grau_usuario)
        return usuario, self.grau_usuario(usuario)
