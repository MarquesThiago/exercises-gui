import tkinter as thin 
from tkinter import Toplevel, filedialog
from pytube import YouTube
import os 

class Dowloader:
    
    
    # colocar o pack na mesma linha que você define uma frame ele não reconhece,
    # os elementos que forem colocados dentro dele e necessario sempre colocar uma linha para so o pack
    
    
    def __init__(self) -> None:
        
        self.window = thin.Tk()
        self.window.title("Dowloader Youtube")
        self.window.resizable(0,0)
        self.window.geometry("1260x720+50+20")
        
        self.logo = thin.PhotoImage(file = os.path.join(os.getcwd(), "square.png"))
        
        self.frame = thin.Frame(self.window, bg = "#3b3b3b", height= 100)
        self.frame.pack(fill = "x")
        
        self.label = thin.Label(self.frame, image = self.logo,  bd = 0)
        self.label.pack(pady=30)
        
        self.content = thin.Frame(self.window)
        self.content.pack(pady = 20)
        
        self.first_sect = thin.Frame(self.content)
        self.first_sect.pack()
        
        self.text_insert = thin.Label(self.first_sect, text = "Insert link of video: " ,font = "Arial 20")
        self.text_insert.pack(side = "left")

        self.link = thin.Entry(self.first_sect, font="Arial 20", width = 50)
        self.link.pack(side = "left")
        
        self.play = thin.Button(self.first_sect, bg = "red", fg  = "white", bd= 0, text = "-->" , width = 6,  height = 2, command= lambda: self.download(self.link.get()))
        self.play.pack(side = "left")
        
        
        self.second_sect = thin.Frame(self.content)
        self.second_sect.pack(pady= 20)
        
        self.audio = True
        self.video = True
        
        # radiobutton e um radio button como os outros 
        self.only_audio = thin.Radiobutton(self.second_sect, text = "Only Audio", value = 0, name = "audio",state= "normal", command= lambda: self.type_dowload("audio")).pack(side = "left")
        self.only_video = thin.Radiobutton(self.second_sect, text = "Only Video", value = 1, name = "video",state= "active" , command= lambda: self.type_dowload("video")).pack(side = "left")
        self.dual = thin.Radiobutton(self.second_sect, text = "Video & Audio", value = 2, name= "dual", state= "active",command= lambda: self.type_dowload("dual")).pack(side = "left")
        
        self.window.mainloop()
        
        
    def type_dowload(self, type:str):
            
        if type is "audio":
            self.audio, self.video = [True, False]
        elif type is "video":
            self.audio, self.video = [False, True]
        else:
            self.audio, self.video = [True, True]
            
        
    def download(self, link: str):
        try: 
            # filedialog:  e perfito pra pregar nome de pasta e noem de arquivos ele abre o explorer 
            if self.audio and self.video:
                pasta = filedialog.asksaveasfile()
                YouTube(link).streams.first().download(pasta)
            elif self.audio and not self.video:
                pasta = filedialog.asksaveasfile()
                YouTube(link).streams.filter(only_audio= True).first().download(pasta)
            elif self.video and not self.audio:
                pasta = filedialog.asksaveasfile()
                YouTube(link).streams.filter(only_video= True).first().download(pasta)
            else:
                pass
        except:
            self.message()
        
        
    def message(self):
        
        # toplevel cria uma window que se sobre põem a janela principal perfeito pra mensagem e mais 
        # funciona semelhante a woindow
        
        window = Toplevel()
        window.title("Error") 
        window.resizable(0,0)
        window.geometry("500x500+250+150") 
        
        text = thin.Label(window, text = "Link not valid", font = "Arial 25")    
        text.pack(padx = 10, pady= 10)
        
        button = thin.Button(window, text = "OK", command= window.destroy)               
        button.pack(padx = 10, pady= 10)
        
Dowloader()