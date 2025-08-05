import customtkinter as ctk

# Configurações iniciais do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criação da janela principal
janela = ctk.CTk()
janela.title("Janela de Login")
janela.geometry("500x400")  # Aumentei um pouco a altura
janela.resizable(False, False)

def validar_login():
    usuario = email.get().strip()  # Remove espaços em branco
    senha_usuario = senha.get().strip()
    
    # Verificar se os campos não estão vazios
    if not usuario or not senha_usuario:
        resultado.configure(text="Preencha todos os campos!", text_color="red")
        return
    
    if usuario == "admin@gmail.com" and senha_usuario == "123456":
        resultado.configure(text="Login realizado com sucesso!", text_color="green")
        # Aqui você pode adicionar código para abrir uma nova janela
    else:
        resultado.configure(text="E-mail ou senha incorreta.", text_color="red")

def limpar_campos():
    email.delete(0, 'end')
    senha.delete(0, 'end')
    resultado.configure(text="")

# Criação dos campos de entrada e botões
titulo = ctk.CTkLabel(janela, text="Sistema de Login", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

texto = ctk.CTkLabel(janela, text="E-mail:")
texto.pack(pady=(10, 5))

email = ctk.CTkEntry(janela, placeholder_text="Digite seu email", justify="center", width=300)
email.pack(pady=5)

texto_senha = ctk.CTkLabel(janela, text="Senha:")
texto_senha.pack(pady=(10, 5))

senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", show="*", justify="center", width=300)
senha.pack(pady=5)

checkbox = ctk.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(pady=10)

# Frame para os botões
frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(pady=10)

botao = ctk.CTkButton(frame_botoes, text="Login", command=validar_login, width=120)
botao.pack(side="left", padx=5)

botao_limpar = ctk.CTkButton(frame_botoes, text="Limpar", command=limpar_campos, width=120)
botao_limpar.pack(side="left", padx=5)

resultado = ctk.CTkLabel(janela, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Permitir login com Enter
senha.bind("<Return>", lambda event: validar_login())

janela.mainloop()
