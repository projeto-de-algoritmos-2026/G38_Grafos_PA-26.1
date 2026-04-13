import tkinter as tk
from tkinter import messagebox, ttk

from grafo import RedeSocialGrafo


class InterfaceRedeSocial:
    def __init__(self, root):
        self.root = root
        self.root.title("Rede Social com Grafos")
        self.root.geometry("1000x620")
        self.root.minsize(900, 560)

        self.rede = RedeSocialGrafo()

        self._montar_interface()
        self._carregar_dados_iniciais()
        self.atualizar_tela()

    def _montar_interface(self):
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)

        painel_esquerdo = ttk.Frame(self.root, padding=16)
        painel_esquerdo.grid(row=0, column=0, sticky="nsew")
        painel_esquerdo.columnconfigure(0, weight=1)
        painel_esquerdo.rowconfigure(2, weight=1)
        painel_esquerdo.rowconfigure(4, weight=1)

        painel_direito = ttk.Frame(self.root, padding=16)
        painel_direito.grid(row=0, column=1, sticky="nsew")
        painel_direito.columnconfigure(0, weight=1)
        painel_direito.rowconfigure(2, weight=1)
        painel_direito.rowconfigure(4, weight=1)

        titulo = ttk.Label(
            painel_esquerdo,
            text="Simulador de Rede Social",
            font=("Segoe UI", 18, "bold"),
        )
        titulo.grid(row=0, column=0, sticky="w", pady=(0, 12))

        bloco_usuario = ttk.LabelFrame(painel_esquerdo, text="Cadastrar Usuario", padding=12)
        bloco_usuario.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        bloco_usuario.columnconfigure(0, weight=1)

        self.entrada_usuario = ttk.Entry(bloco_usuario)
        self.entrada_usuario.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        botao_usuario = ttk.Button(
            bloco_usuario,
            text="Adicionar",
            command=self.adicionar_usuario,
        )
        botao_usuario.grid(row=0, column=1)

        bloco_usuarios = ttk.LabelFrame(painel_esquerdo, text="Usuarios", padding=12)
        bloco_usuarios.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        bloco_usuarios.columnconfigure(0, weight=1)
        bloco_usuarios.rowconfigure(0, weight=1)

        self.lista_usuarios = tk.Listbox(
            bloco_usuarios,
            font=("Consolas", 11),
            exportselection=False,
        )
        self.lista_usuarios.grid(row=0, column=0, sticky="nsew")
        self.lista_usuarios.bind("<<ListboxSelect>>", lambda _event: self.atualizar_detalhes_usuario())

        barra_usuarios = ttk.Scrollbar(bloco_usuarios, orient="vertical", command=self.lista_usuarios.yview)
        barra_usuarios.grid(row=0, column=1, sticky="ns")
        self.lista_usuarios.configure(yscrollcommand=barra_usuarios.set)

        bloco_conexoes = ttk.LabelFrame(painel_esquerdo, text="Conexoes da Rede", padding=12)
        bloco_conexoes.grid(row=4, column=0, sticky="nsew")
        bloco_conexoes.columnconfigure(0, weight=1)
        bloco_conexoes.rowconfigure(0, weight=1)

        self.texto_conexoes = tk.Text(
            bloco_conexoes,
            height=10,
            wrap="word",
            font=("Consolas", 11),
            state="disabled",
        )
        self.texto_conexoes.grid(row=0, column=0, sticky="nsew")

        barra_conexoes = ttk.Scrollbar(bloco_conexoes, orient="vertical", command=self.texto_conexoes.yview)
        barra_conexoes.grid(row=0, column=1, sticky="ns")
        self.texto_conexoes.configure(yscrollcommand=barra_conexoes.set)

        bloco_amizade = ttk.LabelFrame(painel_direito, text="Criar Amizade", padding=12)
        bloco_amizade.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        bloco_amizade.columnconfigure(1, weight=1)

        ttk.Label(bloco_amizade, text="Usuario 1").grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Label(bloco_amizade, text="Usuario 2").grid(row=1, column=0, sticky="w")

        self.combo_usuario_1 = ttk.Combobox(bloco_amizade, state="readonly")
        self.combo_usuario_1.grid(row=0, column=1, sticky="ew", pady=(0, 6))

        self.combo_usuario_2 = ttk.Combobox(bloco_amizade, state="readonly")
        self.combo_usuario_2.grid(row=1, column=1, sticky="ew")

        botao_amizade = ttk.Button(
            bloco_amizade,
            text="Conectar",
            command=self.criar_amizade,
        )
        botao_amizade.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        bloco_caminho = ttk.LabelFrame(painel_direito, text="Caminho Mais Curto", padding=12)
        bloco_caminho.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        bloco_caminho.columnconfigure(1, weight=1)

        ttk.Label(bloco_caminho, text="Origem").grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Label(bloco_caminho, text="Destino").grid(row=1, column=0, sticky="w")

        self.combo_caminho_origem = ttk.Combobox(bloco_caminho, state="readonly")
        self.combo_caminho_origem.grid(row=0, column=1, sticky="ew", pady=(0, 6))

        self.combo_caminho_destino = ttk.Combobox(bloco_caminho, state="readonly")
        self.combo_caminho_destino.grid(row=1, column=1, sticky="ew")

        botao_caminho = ttk.Button(
            bloco_caminho,
            text="Buscar",
            command=self.buscar_caminho,
        )
        botao_caminho.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        bloco_detalhes = ttk.LabelFrame(painel_direito, text="Detalhes do Usuario", padding=12)
        bloco_detalhes.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        bloco_detalhes.columnconfigure(0, weight=1)
        bloco_detalhes.rowconfigure(0, weight=1)

        self.texto_detalhes = tk.Text(
            bloco_detalhes,
            wrap="word",
            font=("Consolas", 11),
            height=12,
            state="disabled",
        )
        self.texto_detalhes.grid(row=0, column=0, sticky="nsew")

        bloco_analise = ttk.LabelFrame(painel_direito, text="Analise da Rede", padding=12)
        bloco_analise.grid(row=4, column=0, sticky="nsew")
        bloco_analise.columnconfigure(0, weight=1)
        bloco_analise.rowconfigure(0, weight=1)

        self.texto_analise = tk.Text(
            bloco_analise,
            wrap="word",
            font=("Consolas", 11),
            height=10,
            state="disabled",
        )
        self.texto_analise.grid(row=0, column=0, sticky="nsew")

    def _carregar_dados_iniciais(self):
        for nome in ("Ana", "Bruno", "Carla", "Diego", "Elisa"):
            self.rede.adicionar_usuario(nome)

        for usuario_a, usuario_b in (
            ("Ana", "Bruno"),
            ("Ana", "Carla"),
            ("Bruno", "Diego"),
            ("Carla", "Elisa"),
        ):
            self.rede.criar_amizade(usuario_a, usuario_b)

    def adicionar_usuario(self):
        nome = self.entrada_usuario.get()

        try:
            self.rede.adicionar_usuario(nome)
        except ValueError as erro:
            messagebox.showerror("Cadastro invalido", str(erro))
            return

        self.entrada_usuario.delete(0, tk.END)
        self.atualizar_tela()
        messagebox.showinfo("Sucesso", f"Usuario '{nome.strip()}' cadastrado.")

    def criar_amizade(self):
        usuario_a = self.combo_usuario_1.get()
        usuario_b = self.combo_usuario_2.get()

        try:
            self.rede.criar_amizade(usuario_a, usuario_b)
        except ValueError as erro:
            messagebox.showerror("Conexao invalida", str(erro))
            return

        self.atualizar_tela()
        messagebox.showinfo("Sucesso", f"Amizade criada entre {usuario_a} e {usuario_b}.")

    def buscar_caminho(self):
        origem = self.combo_caminho_origem.get()
        destino = self.combo_caminho_destino.get()

        if not origem or not destino:
            messagebox.showerror("Busca invalida", "Selecione usuarios de origem e destino.")
            return

        try:
            caminho, distancia = self.rede.caminho_mais_curto(origem, destino)
        except ValueError as erro:
            messagebox.showerror("Busca invalida", str(erro))
            return

        if not caminho:
            messagebox.showinfo(
                "Caminho nao encontrado",
                f"Nao existe caminho entre {origem} e {destino}.",
            )
            return

        descricao_caminho = " -> ".join(caminho)
        messagebox.showinfo(
            "Caminho encontrado",
            f"Caminho: {descricao_caminho}\nDistancia: {distancia} conexoes",
        )

    def atualizar_tela(self):
        usuarios = self.rede.listar_usuarios()

        self.lista_usuarios.delete(0, tk.END)
        for usuario in usuarios:
            self.lista_usuarios.insert(tk.END, usuario)

        self.combo_usuario_1["values"] = usuarios
        self.combo_usuario_2["values"] = usuarios
        self.combo_caminho_origem["values"] = usuarios
        self.combo_caminho_destino["values"] = usuarios

        self._atualizar_texto_conexoes()
        self._atualizar_texto_analise()
        self.atualizar_detalhes_usuario()

    def atualizar_detalhes_usuario(self):
        selecao = self.lista_usuarios.curselection()

        if not selecao:
            self._definir_texto(
                self.texto_detalhes,
                "Selecione um usuario para visualizar suas conexoes.",
            )
            return

        usuario = self.lista_usuarios.get(selecao[0])
        amigos = self.rede.obter_amigos(usuario)

        linhas = [f"Usuario: {usuario}", ""]
        linhas.append(f"Total de amigos: {len(amigos)}")
        linhas.append("")
        linhas.append("Lista de amigos:")

        if amigos:
            linhas.extend(f"- {amigo}" for amigo in amigos)
        else:
            linhas.append("- Nenhuma conexao cadastrada")

        outros = [nome for nome in self.rede.listar_usuarios() if nome != usuario]
        if outros:
            comparado = outros[0]
            comuns = self.rede.amigos_em_comum(usuario, comparado)
            linhas.append("")
            linhas.append(f"Amigos em comum com {comparado}:")
            if comuns:
                linhas.extend(f"- {nome}" for nome in comuns)
            else:
                linhas.append("- Nenhum amigo em comum")

        self._definir_texto(self.texto_detalhes, "\n".join(linhas))

    def _atualizar_texto_conexoes(self):
        conexoes = self.rede.listar_conexoes()

        if not conexoes:
            texto = "Nenhuma conexao cadastrada."
        else:
            linhas = [f"{usuario_a} <-> {usuario_b}" for usuario_a, usuario_b in conexoes]
            texto = "\n".join(linhas)

        self._definir_texto(self.texto_conexoes, texto)

    def _atualizar_texto_analise(self):
        usuarios = self.rede.listar_usuarios()
        usuario_mais_conectado, maior_grau = self.rede.usuario_mais_conectado()

        if usuario_mais_conectado is None:
            usuario_mais_conectado = "Ninguem"

        linhas = [
            f"Total de usuarios: {self.rede.quantidade_usuarios()}",
            f"Total de conexoes: {self.rede.quantidade_conexoes()}",
            f"Usuario mais conectado: {usuario_mais_conectado}",
            f"Quantidade de amizades dele: {maior_grau}",
        ]

        if usuarios:
            linhas.append("")
            linhas.append("Grau de cada usuario:")
            for usuario in usuarios:
                linhas.append(f"- {usuario}: {self.rede.grau_usuario(usuario)} conexao(oes)")

        self._definir_texto(self.texto_analise, "\n".join(linhas))

    @staticmethod
    def _definir_texto(widget, conteudo):
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert("1.0", conteudo)
        widget.configure(state="disabled")


def main():
    root = tk.Tk()
    estilo = ttk.Style()
    if "clam" in estilo.theme_names():
        estilo.theme_use("clam")

    InterfaceRedeSocial(root)
    root.mainloop()


if __name__ == "__main__":
    main()
