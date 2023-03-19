import tkinter as thin 
from tkinter import Message, Toplevel, ttk, filedialog
from ttkthemes import ThemedTk
from  pygame import mixer
import os 


# pip install ttkthemes para instalar a biblioteca respnsavel pelos temas 



class Player:
    
    
    def __init__(self):
        
        mixer.init()
        
        self.window = ThemedTk(theme= "black")
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("360x450+150+50")
        self.window.config(bg = "#333333")
        
        self.import_images()
        self.play = False
        self.last_index = None
        self.musics = []
    
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
        
        self.pause = ttk.Button(self.frame2, image= self.images["play"], command= self.play_music)
        self.pause.grid(row= 0, column= 1)
        
        self.next = ttk.Button(self.frame2, image= self.images["next"], command= self.next_music)
        self.next.grid(row= 0, column= 2)
        
        # criar uma barra de uma a 100
        # adicionamos o calor inicial de 30 mudamos a ancora e setamos o calor para 30 tambem
        self.scale = ttk.Scale(self.window, from_ = 0, to = 100, value = 30, command= self.volume_set)
        self.scale.anchor = 30
        self.scale.setvar("30")
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
        for file in files:
            if file.endswith(".mp3"):
                self.list.insert(thin.END, str(file))
                self.musics.append(os.path.join(local, f"{file}"))
        self.len_list = self.list.size()
                
    def delete_music(self):
        self.list.delete(thin.ANCHOR)
        
    def next_music(self):
        if self.message():
            index = self.list.curselection()[0] 
            
            if self.len_list - 1  < index + 1:
                index = 0
            else:
                index = index + 1
            
            self.list.select_clear(0, thin.END)
            self.list.yview(index)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.select_anchor(index)
            self.play_music(play = False)
            
    def get_play(self):
        return self.get_play
        
        
    def previous_music(self):
        if self.message():
            index = self.list.curselection()[0]
            
            if index - 1 < 0:
                index = self.len_list - 1
            else:
                index = index - 1
            
            # primeiro limpamos a selecão
            # depois reatribuimos o index com activate
            # depois selecionameos o index
            self.list.select_clear(0, thin.END)
            self.list.yview(index)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.select_anchor(index)
            self.play_music(play = False)
            
            # ele praticamente move a visão para a com forme forem sendo incrementado os index
            self.list.yview(index)
            
            # essas funções parecem ser similares ao javascript
            # self.list.yview_moveto(float)
            # self.list.yview_scroll(int)
            
    # musica koad carrega a musica e o play reproduz e  o pause simplesmente pausa   
    def play_music(self, index  = thin.ANCHOR, play = None):
        if self.message(): 
            play =  play is None if self.play else play
            index = self.list.index(index)
            try:
                print(index)
                if not self.last_index == index or not play:
                    mixer.music.load(self.musics[index])
                    mixer.music.play()
                    self.pause.config(image = self.images["pause"])
                    self.play = True
                    self.last_index = index
                    
                else:
                    mixer.music.pause()
                    self.play = False
                    self.last_index = None
                    self.pause.config(image = self.images["play"])
                    
            except IndexError:
                self.list.activate(0)
                self.list.select_set(0)
                self.list.select_anchor(0)
                self.play_music()
                self.last_play = 0
           
    def message(self):
        if len(self.musics) is 0:
            
            window = Toplevel()
            window.title("Error: NOT FOUND MUSIC")
            window.geometry("340x200+200+200")
            window.resizable(0,0)
            window.config(bg = "#444444")
            
            label = ttk.Label(window, text = "Program not found music, added \nmusic to you listen", font= "Arial 16")
            label.pack(pady=20, padx=10)
            
            button = ttk.Button(window, text = "Ok", width= 7, command= window.destroy)
            button.pack()
            return False
        
        return True
    
    def volume_set(self, var):
        # ele precisa dessa carialvel para não dar erro mais não implica no valor 
        # pegamos o valor que vai de 0 a 100 de dividimos por 100 que e valo do mixer e entre 0 e 1 
        mixer.music.set_volume(self.scale.get()/100)
         

Player()