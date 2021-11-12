from tkinter import *
from tkinter import scrolledtext
from tkinter import font

#criando a janela:
window = Tk ()
window.title("Filtro de palavras")
window.geometry("1000x700")

#palavras:
suspeito = Label(window, text = "Palavra Suspeita: ", font = ("Arial", 13))
suspeito.place(relx = 0.05, rely = 0.08)

frequencia = Label(window, text = "Frequência: ", font = ("Arial", 13))
frequencia.place(relx = 0.05, rely = 0.13)

ocorrencia = Label(window, text = "Ocorrências: ", font = ("Arial", 13))
ocorrencia.place(relx = 0.05, rely = 0.20)

#scrolledtext:
txt = scrolledtext.ScrolledText(window, width = 100, height = 25)
txt.place(relx = 0.5, rely = 0.55, anchor = CENTER)

#parte das caixas de texto:
suspeitaCaixa = Entry(window, width = 15, font = ("Arial", 13))
suspeitaCaixa.place(relx = 0.19, rely = 0.08)

frequenciaCaixa = Entry(window, width = 15, font = ("Arial", 13))
frequenciaCaixa.place(relx = 0.15, rely = 0.13)

#código para identificar as palavras:
def searchWords():
  frequenciaCaixa.delete(0, END)
  txt.delete(1.0, END)
  frequencia2 = 0
  palavra = suspeitaCaixa.get()
  
  arquivoChat = []
  arquivo = open("chat.txt", "r")
  for i in arquivo.readlines():
    arquivoChat.append(i.strip().split())
  
  arquivo.close()
  
  for i in range(len(arquivoChat)):
    for k in range(len(arquivoChat[i])):
      if palavra.lower() == arquivoChat[i][k].lower().replace("?", "").replace("!", "").replace(",", "").replace("*", "").replace(".", ""):
        arquivoChat[i][-1] = arquivoChat[i][-1]+"\n\n"
        txt.insert(1.0, " ".join(arquivoChat[i]))
        frequencia2 += 1
  
  frequenciaCaixa.insert(0, frequencia2)

#botão "Pesquisar!":
button = Button(window, text = "Pesquisar!", command = searchWords)
button.place(relx = 0.35, rely = 0.08)



#loop da janela:
window.mainloop()
