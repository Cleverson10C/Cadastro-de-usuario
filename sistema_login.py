import customtkinter as ctk
import os
from janela_login import criar_janela_login

# Funções para salvar e carregar usuários de um arquivo
def carregar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 2:
                    usuarios[partes[0]] = partes[1]
    return usuarios

def salvar_usuarios(usuarios):
    with open("usuarios.txt", "w", encoding="utf-8") as f:
        for usuario, senha in usuarios.items():
            f.write(f"{usuario},{senha}\n")

usuarios = carregar_usuarios()

def validar_login(nome, senha, resultado):
    usuario = nome.get().strip()
    senha_usuario = senha.get().strip()
    if not usuario or not senha_usuario:
        resultado.configure(text="Preencha todos os campos!", text_color="red")
        return
    if usuario in usuarios and usuarios[usuario] == senha_usuario:
        resultado.configure(text="Login realizado com sucesso!", text_color="green")
    else:
        resultado.configure(text="Nome ou senha incorreta.", text_color="red")
        
def cadastrar_usuario(nome, senha, resultado, limpar_campos_func):
    usuario = nome.get().strip()
    senha_usuario = senha.get().strip()
    
    if not usuario or not senha_usuario:
        resultado.configure(text="Preencha todos os campos para cadastrar!", text_color="red")
        return
    
    if usuario in usuarios:
        resultado.configure(text="Usuário já cadastrado!", text_color="orange")
    else:
        usuarios[usuario] = senha_usuario
        salvar_usuarios(usuarios)
        resultado.configure(text="Usuário cadastrado com sucesso!", text_color="green")
        limpar_campos_func()

def limpar_campos(nome, senha, resultado):
    nome.delete(0, 'end')
    senha.delete(0, 'end')
    resultado.configure(text="")

def iniciar_interface():
    criar_janela_login(
        validar_login,
        cadastrar_usuario,
        limpar_campos
    )

iniciar_interface()
