import customtkinter as ctk

def criar_janela_login(validar_login, cadastrar_usuario, limpar_campos):
    janela = ctk.CTk()
    janela.title("Cadastro de Usuário")
    janela.geometry("500x400")
    janela.resizable(False, False)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    titulo = ctk.CTkLabel(janela, text="Sistema de Login", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    texto_nome = ctk.CTkLabel(janela, text="Nome:")
    texto_nome.pack(pady=(10, 5))
    nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome", justify="center", width=300)
    nome.pack(pady=5)

    # ...campo de e-mail removido...

    texto_senha = ctk.CTkLabel(janela, text="Senha:")
    texto_senha.pack(pady=(10, 5))
    senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", justify="center", width=300, show="*")
    senha.pack(pady=5)

    checkbox = ctk.CTkCheckBox(janela, text="Lembrar Login")
    checkbox.pack(pady=10)

    frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
    frame_botoes.pack(pady=10)

    resultado = ctk.CTkLabel(janela, text="", font=("Arial", 12))
    resultado.pack(pady=10)

    botao_login = ctk.CTkButton(
        frame_botoes,
        text="Login",
        command=lambda: validar_login(nome, senha, resultado),
        width=120
    )
    botao_login.pack(side="left", padx=10)

    botao_cadastrar = ctk.CTkButton(
        frame_botoes,
        text="Cadastrar",
        command=lambda: cadastrar_usuario(nome, senha, resultado, lambda: limpar_campos(nome, senha, resultado)),
        width=120
    )
    botao_cadastrar.pack(side="left", padx=10)

    botao_limpar = ctk.CTkButton(
        frame_botoes,
        text="Limpar",
        command=lambda: limpar_campos(nome, senha, resultado),
        width=120
    )
    botao_limpar.pack(side="left", padx=10)

    # Corrigido: passar os argumentos corretos no bind
    senha.bind(
        "<Return>",
        lambda event: validar_login(nome, senha, resultado)
    )

    janela.mainloop()


