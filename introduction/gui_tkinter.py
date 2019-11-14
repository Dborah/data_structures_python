from tkinter import *

#cria um nova janela
window = Tk()

#seta o titulo da janela
window.title('Meu programa')

#entra de texto
entry_text = Entry(window, width=30)
entry_text.pack()
entry_text.focus_set()

def click_button():
    print(entry_text.get())


#cria um botão
btn = Button(window, text='Clique aqui', width=20, command=click_button)
btn.pack()

#tamanho da janela
window.geometry('300x150')


#desenha e exibe a janela
window.mainloop()