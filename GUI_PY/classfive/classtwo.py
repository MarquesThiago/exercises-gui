import tkinter as thin 
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk
import os 


# pip install ttkthemes para instalar a biblioteca respnsavel pelos temas 



class Player:
    
    
    def __init__(self):
        
        
        self.window = ThemedTk(theme= "black")
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("360x450+150+50")
        self.window.config(bg = "#333333")
        
        self.import_images()
        
    
        self.list  = thin.Listbox(self.window, bg = "#222222", bd = 0, height= 15, fg = "white", selectforeground= "#FFFFFF", selectbackground= "#666666")
        self.list.pack(fill = thin.X, padx= 10, pady= 10) 
        
        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady= 10)
        
        self.remove = ttk.Button(self.frame, image= self.images["remove"], command= self.delete_music)
        self.remove.grid(row= 0, column= 0)
        
        self.add = ttk.Button(self.frame, image= self.images["add"], command= self.select_music)
        self.add.grid(row= 0, column= 1)
        
        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=20)
        
        self.previous = ttk.Button(self.frame2, image= self.images["previus"], command= self.previous_music)
        self.previous.grid(row= 0, column= 0)
        
        self.pause = ttk.Button(self.frame2, image= self.images["play"])
        self.pause.grid(row= 0, column= 1)
        
        self.next = ttk.Button(self.frame2, image= self.images["next"], command= self.next_music)
        self.next.grid(row= 0, column= 2)
        
        # criar uma barra de uma a 100
        self.scale = ttk.Scale(self.window)
        self.scale.pack(fill = thin.X, pady= 20, padx= 10)
        
        
        
        
        
        self.window.mainloop()


    def import_images(self):
            
        images = ["add", "next", "pause", "play", "previus", "remove"]
        
        self.images = {}
        path = os.path.join(os.getcwd(), "assets")
        
        for image in images:
            
            self.images[image] = thin.PhotoImage(file = os.path.join(path, f"{image}.png"))

        return None
    
    def select_music(self):
        
        local = filedialog.askdirectory()
        files = os.listdir(local)
        self.musics = []
        for file in files:
            if file.endswith(".mp3"):
                self.list.insert(thin.END, str(file))
                self.musics.append(os.path.join(local, f"{file}.mp3"))
        self.len_list = self.list.size()
                
    def delete_music(self):
        # delete a musica que esta selecionado o anchor deve ser o objeto selecionado 
        self.list.delete(thin.ANCHOR)
        
    def next_music(self):
        # retorna o valor da linha selecionada 
        # print(self.list.curselection())
        index = self.list.curselection()[0] 
        
        if self.len_list < index + 1:
            index = 0
        else:
            index = index + 1
        
        
    def previous_music(self):
        index = self.list.curselection()[0]
        
        if index - 1 < 0:
            index = self.len_list
        else:
            index = index - 1
        
        
    

Player()