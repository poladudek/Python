import random
import tkinter as tk
from tkinter import PhotoImage

class RollTheDiceApp:
    def __init__(self, root): #konstruktor tworzy okno aplikacji
        self.root = root
        self.root.title("Rolling the dice!")
        self.root.geometry("700x700")
        self.root.config(bg="#f9f3e6")
        self.dark_pink = "#d89fbc"
        self.light_pink = "#f7c8dd"
        
        self.GUI()

    def GUI(self):
        self.button = tk.Button(self.root, text="Roll the dice", command=self.rollingTheDice, font=("Georgia", 20, "bold"), bg=self.light_pink, fg=self.dark_pink, 
        relief="flat", bd=3, padx=20, pady=10, activebackground="#d37b9b", activeforeground="white", highlightbackground=self.light_pink, highlightcolor=self.light_pink)
        self.button.pack(side="bottom", pady=30) #przycisk wykonuje funkcje rollingTheDice()

        self.resultGraphic = tk.Label(self.root, bg="#f9f3e6")
        self.resultGraphic.pack(pady=50)

    def rollingTheDice(self):
        roll = random.randint(1, 6)
        
        resultsPics = { #slownik aby nie naduzywac else-if
            1: "1.png",
            2: "2.png",
            3: "3.png",
            4: "4.png",
            5: "5.png",
            6: "6.png"
        }

        resultPic = PhotoImage(file=resultsPics[roll])
        
        self.resultGraphic.config(image=resultPic, width=700, height=700)
        self.resultGraphic.image = resultPic

root = tk.Tk()
app = RollTheDiceApp(root)
root.mainloop() #czeka w petli na zachowania uzytkownika
