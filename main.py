from AI import Ai
from tkinter import *
from threading import Thread

def ask():
    ai_answer.config(text="Fetching response...")
    Thread(target=update).start()

def update():
    answer = local_ai.ask(prompt=ai_entry.get())
    ai_answer.config(text=answer)
    ai_entry.delete(first="0", last=END)

local_ai = Ai()

window = Tk()
window.geometry("1200x600")
window.config(bg="#FEFAE0", padx=50, pady=50)
window.title("Llama3.1 Chatbot")

ai_entry = Entry(window, width=100)
ai_entry.grid(row=2, column=1, columnspan=3)

submit_button = Button(window, text="Ask!", width=40, command=ask)
submit_button.grid(row=3, column=2)

title = Label(window, text="Chatbot!", font=("Sans-Serrif", 40, "bold"), bg="#FEFAE0", pady=20)
title.grid(row=1, column=1, columnspan=3)

ai_answer = Label(window, text="Waiting for prompt...", font=("Sans-Serrif", 15, "normal"), bg="#FEFAE0", pady=20, wraplength=600)
ai_answer.grid(row=4, column=1, columnspan=3)

window.mainloop()
