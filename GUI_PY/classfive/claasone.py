import tkinter as thin 
from tkinter import ttk
from ttkthemes import ThemedTk
import os 


# pip install ttkthemes para instalar a biblioteca respnsavel pelos temas 



class Player:
    
    
    def __init__(self):
        
        # themedTK aplca um tema do padrão 
        
        self.window = ThemedTk(theme= "black")
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("360x450+150+50")
        self.window.config(bg = "#333333")
        
        self.import_images()
        
        # o tamanho do liste e sobre a quantidade de linhsa que nos queremos 
        # na bibliotecja ttk temos os nossos widgwts que pegam automaticamente as configuraç~eos 
        # de tema mas o listbox não tem nele
        self.list  = thin.Listbox(self.window, bg = "#444444", bd = 0, height= 15)
        self.list.pack(fill = thin.X, padx= 10, pady= 10) 
        
        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady= 10)
        
        self.remove = ttk.Button(self.frame, image= self.images["remove"])
        self.remove.grid(row= 0, column= 0)
        
        self.add = ttk.Button(self.frame, image= self.images["add"])
        self.add.grid(row= 0, column= 1)
        
        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=20)
        
        self.previous = ttk.Button(self.frame2, image= self.images["previus"])
        self.previous.grid(row= 0, column= 0)
        
        self.pause = ttk.Button(self.frame2, image= self.images["play"])
        self.pause.grid(row= 0, column= 1)
        
        self.next = ttk.Button(self.frame2, image= self.images["next"])
        self.next.grid(row= 0, column= 2)
        
        
        
        self.window.mainloop()


    def import_images(self):
            
        images = ["add", "next", "pause", "play", "previus", "remove"]
        
        self.images = {}
        path = os.path.join(os.getcwd(), "assets")
        
        for image in images:
            
            self.images[image] = thin.PhotoImage(file = os.path.join(path, f"{image}.png"))

        return None


Player()