import tkinter as thin
import os
from typing import Any 

class Paint():

    def __init__(self):
        self.root = os.getcwd()
        self.window = thin.Tk()
        self.window.title("Painter")
        self.size = [1200, 620]
        self.window.minsize(width = self.size[0], height = self.size[1])
        self.window.resizable(0,0)
        self.bar_menu = thin.Frame(self.window, bg = "gray", height = 30)
        self.bar_menu.pack(fill = "x")       
        
       
        
        self.text_color = self._create_label("Colors")
        
        self.pick_color = {"black", "orange", "pink", "white", "red", "blue", "gray", "green", "purple", "brown"}
        
        # para implementar a troca de ele para por paramentro a cor para o lambda atribuindo para uma variavel e usa a variavel para trocar a cor 
        
        for hue in self.pick_color:
            self.btn_color = thin.Button(self.bar_menu, bg= hue, height= 2, width= 4,  command= lambda hue = hue: self.alternate_color_brush(color = hue) )
            self.btn_color.pack(side = "left", padx = 3)
        
        
        self.text_size = self._create_label("Size")
        
        self.spin_size = thin.Spinbox(self.bar_menu, from_ = 1, to = 50, width = 3)
        self.spin_size.pack(side = "left")
        
        
        
        self.images = self._import_images()
        self.btn_brush = []
        
        self.text_brush = self._create_label("Brush")
    
        for brush in [self.images["line"], self.images["oval"], self.images["square"]]:
            
            btn_image = thin.Button(self.bar_menu, image=brush, bd = 0)
            btn_image.pack(side = "left")
            self.btn_brush.append(btn_image)
        
        self.btn_opt = []
        
        self.text_options = self._create_label("Options")
        
        for brush in [self.images["new"], self.images["save"]]:
                
            btn_image = thin.Button(self.bar_menu, image=brush, bd = 0)
            btn_image.pack(side = "left")
            self.btn_opt.append(btn_image)
        
        
        
        self.canvas = thin.Canvas(self.window, height= self.size[1])
        self.canvas.pack(fill = "both")
        
        # O B1-motion e um evento de mousse 
        self.canvas.bind("<B1-Motion>", self.draw)
        

        self.color_brush = "Black"


        self.window.mainloop()
        
        
    def _import_images(self) -> dict:
            
        root = os.path.join(self.root, "../imgs/")
            
        images =  {
                "eraser": thin.PhotoImage(file = os.path.join(root, "eraser.png")),
                "line": thin.PhotoImage(file= os.path.join(root, "line.png")),
                "new": thin.PhotoImage(file = os.path.join(root, "new.png")),
                "oval": thin.PhotoImage(file = os.path.join(root, "oval.png")),
                "save": thin.PhotoImage(file = os.path.join(root, "save.png")),
                "square": thin.PhotoImage(file = os.path.join(root, "square.png"))}
        return images
    

    def _create_label(self, name: str )-> thin.Button:
        
        button = thin.Label(self.bar_menu, text= f"{name}: ", fg = "white", bg = "gray")
        button.pack(side = "left", padx= 20)
        return button
    
    # outline = parametro para definição do contorno da forma
    
    def draw(self, event)-> None:
        x1 , y1= (event.x) , (event.y)
        x2 , y2= (event.x) , (event.y)
        self.canvas.create_oval(x1, y1, x2, y2, fill = self.color_brush, outline= self.color_brush, width= 20 )
        return None
    
    def alternate_color_brush(self, color:str) -> None:
        
        self.color_brush = color
        
        return None
    

Paint()