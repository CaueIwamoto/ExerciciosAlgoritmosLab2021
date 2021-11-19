#Importando:
import os 
from tkinter import *
from tkinter import font
#Import aleatório:
from random import randrange
#Import do dia/mês/ano:
from datetime import date
#Import da mensagem de aviso:
from tkinter import messagebox

#Criando a janela:
window = Tk()
window.title("Janela de Cadastro")
window.geometry("1000x700")

#Textos na janela:
titulo = Label(window, text = "Cadastro", font = ("Arial", 25))
titulo.place(relx = 0.50, rely = 0.04, anchor = CENTER)

nome = Label(window, text = "Digite o seu nome:", font = ("Arial", 15))
nome.place(relx = 0.05, rely = 0.08)

nasc = Label(window, text = "Digite a sua data de nascimento:", font = ("Arial", 15))
nasc.place(relx = 0.05, rely = 0.16)

endereco = Label(window, text = "Digite o seu endereço:", font = ("Arial", 15))
endereco.place(relx = 0.05, rely = 0.24)

profissao = Label(window, text = "Digite a sua profissão:", font = ("Arial", 15))
profissao.place(relx = 0.05, rely = 0.32)

cpf = Label(window, text = "Digite o seu CPF:", font = ("Arial", 15))
cpf.place(relx = 0.05, rely = 0.39)

#Caixas de textos na janela:
caixaNome = Entry(window, width = 15, font = ("Arial", 15))
caixaNome.place(relx = 0.23, rely = 0.08)

caixaNascimento = Entry(window, width = 15, font = ("Arial", 15))
caixaNascimento.place(relx = 0.35, rely = 0.16)

caixaEndereco = Entry(window, width = 15, font = ("Arial", 15))
caixaEndereco.place(relx = 0.26, rely = 0.24)

caixaProfissao = Entry(window, width = 15, font = ("Arial", 15))
caixaProfissao.place(relx = 0.26, rely = 0.32)

caixaCPF = Entry(window, width = 15, font = ("Arial", 15))
caixaCPF.place(relx = 0.22, rely = 0.39)

#Código para o programa criar um arquivo .txt e registrar o usuário no sistema:
def perfil():
  ID = []
  for i in range(5):
    ID.append(str(randrange(9)))
  print(ID)
  #CPF, nome, data de nascimento, endereco e profissão:
  cpf = caixaCPF.get()
  nome = caixaNome.get()
  dataNascimento = caixaNascimento.get().replace("-", "/").split("/")
  endereco = caixaEndereco.get()
  profissao = caixaProfissao.get()
  
  #Cálcular a idade:
  idade = date.today().year - int(dataNascimento[-1])
  
  if os.path.isfile(cpf+'.txt'):
    messagebox.showinfo("Aviso", "Usuário já registrado!")
  else:
    arquivo = open(cpf + ".txt", "w")
    arquivo.write(f'ID: {"".join(ID)}\n')
    arquivo.write(f'Nome: {nome}\n')
    arquivo.write(f'Data de Nascimento: {dataNascimento}\n')
    arquivo.write(f'Idade: {idade}\n')
    arquivo.write(f'Endereço: {endereco}\n')
    arquivo.write(f'Profissão: {profissao}\n')
    #Mensagem de aviso para avisar ao usuário que sua conta foi cadastrada:
    messagebox.showinfo("Aviso", "Usuário cadastrado com sucesso!")
    arquivo.close()


#Botão "Cadastrar":
botao = Button(window, text = "Cadastrar!", command = perfil)
botao.place(relx = 0.50, rely = 0.45)


#Loop da janela:
window.mainloop()
