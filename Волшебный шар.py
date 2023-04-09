import random
from tkinter import *
from tkinter import messagebox
from  random import  randint
def click():
    Answer = random.randint(1, 5)
    End = Answers.get(Answer)
    messagebox.showinfo("Шар предсказал тебе...", End)
root = Tk()
root.title('Magick bull')
root.geometry('500x300')
Answers = {1: 'Ты НЕ ПРОЙДЁШЬ', 2: 'Оставь надежду всяк сюда входящий', 3: 'Я ГУЛЬ', 4: 'Я не умру в туалете', 5: 'Dolche Milk'}

B = Button(root, text='Тыкни на кнопку', width=15, height=2, bg='white', command=click)
B.pack()

root.mainloop()