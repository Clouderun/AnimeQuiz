import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel('perguntas.xlsx')
# vai pegar aleatoriamente as perguntas
perguntas = df.sample(n=8).values.tolist()

# variaveis globais
score = 0
pergunta_atual = 0

# checar as respostas

def checkAnswer(answer):
    global score, pergunta_atual

    if answer == correctanswer.get():
        score+=1
    pergunta_atual +=1

    if pergunta_atual < len(perguntas):
        displayquestion()
    else:
        showResults()

# funcao para exibir a prox pergunta
def displayquestion():
    pergunta, opcao1, opcao2, opcao3, opcao4, answer = perguntas[pergunta_atual]
    labelperguntas.config(text=pergunta)
    opcao1btn.config(text=opcao1, state=tk.NORMAL, command=lambda:checkAnswer(1))
    opcao2btn.config(text=opcao2, state=tk.NORMAL, command=lambda:checkAnswer(2))
    opcao3btn.config(text=opcao3, state=tk.NORMAL, command=lambda:checkAnswer(3))
    opcao4btn.config(text=opcao4, state=tk.NORMAL, command=lambda:checkAnswer(4))

    correctanswer.set(answer)

# funcao para exibir resultado

def showResults():
    messagebox.showinfo('Quiz Finalizado!ヾ(≧▽≦*)o', f"Parabens!🐻 Conseguiu completar o quiz de Animes. \n\nPontuação final: {score}/{len(perguntas)}")
    opcao1btn.config(state=tk.DISABLED)
    opcao2btn.config(state=tk.DISABLED)
    opcao3btn.config(state=tk.DISABLED)
    opcao4btn.config(state=tk.DISABLED)

    jogarAgainbtn.pack()

# funcao pra jogar de novo
def PlayAgain():
    global score, pergunta_atual
    score = 0
    pergunta_atual = 0
    random.shuffle(perguntas)
    opcao1btn.config(state=tk.NORMAL)
    opcao2btn.config(state=tk.NORMAL)
    opcao3btn.config(state=tk.NORMAL)
    opcao4btn.config(state=tk.NORMAL)
    jogarAgainbtn.pack_forget()

#Janela do projeto
janela = tk.Tk()
janela.title('Anime Quiz🎮')
janela.geometry('400x450')

#cores
backgroundcolor = "#87CEEB"
textcolor = "#000000"
buttoncolor = "#90EE90"
buttontextcolor = "#7B68EE"

janela.config(bg=backgroundcolor)
janela.option_add('*Font', 'Arial')

# icon do quiz

iconeurso = PhotoImage(file="teddy-br.png")
labelurso = tk.Label(janela, image=iconeurso, bg=backgroundcolor)

# para que seja posicionada a tela:
labelurso.pack(pady=10)

#Componentes da interface do quiz
labelperguntas = tk.Label(janela, text="", wraplength=380, bg=backgroundcolor, fg=textcolor, font=("Arial", 12, "bold"))
labelperguntas.pack(pady=20)

#valores que colocamos que é a posiçao da resposta correta
correctanswer = tk.IntVar()

#O state disabled não permite que o botão seja clicavel
opcao1btn = tk.Button(janela, text="", width=30, bg=buttoncolor, fg=buttontextcolor, state=tk.DISABLED, font=("Arial", 10, "italic"))
opcao1btn.pack(pady=10)

opcao2btn = tk.Button(janela, text="", width=30, bg=buttoncolor, fg=buttontextcolor, state=tk.DISABLED, font=("Arial", 10, "italic"))
opcao2btn.pack(pady=10)

opcao3btn = tk.Button(janela, text="", width=30, bg=buttoncolor, fg=buttontextcolor, state=tk.DISABLED, font=("Arial", 10, "italic"))
opcao3btn.pack(pady=10)

opcao4btn = tk.Button(janela, text="", width=30, bg=buttoncolor, fg=buttontextcolor, state=tk.DISABLED, font=("Arial", 10, "italic"))
opcao4btn.pack(pady=10)

# ao tira-lo o btn se torna clicavel
jogarAgainbtn = tk.Button(janela, command= PlayAgain,text="Jogar Novamente", width=30, bg=buttoncolor, fg=buttontextcolor, font=("Arial", 10, "italic"))



displayquestion()

#executa a tela
janela.mainloop()