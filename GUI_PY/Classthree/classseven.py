# prara salvar a imagem e necessario instalar duas bibliotecas a pillow, pillow-PIL e pyscrenshot
import tkinter as thin
from tkinter.colorchooser import askcolor
import pyscreenshot
import os


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
        
       # variaveis de controle de uso dos pinceis 
        self.oval = True
        self.line = False
        self.eraser = False
       
       
       
       
        
        self.text_color = self._create_label("Colors")
        
        self.pick_color = {"black", "orange", "pink", "white", "red", "blue", "gray", "green", "purple", "brown"}
        
        
        for hue in self.pick_color:
            self.btn_color = thin.Button(self.bar_menu, bg= hue, height= 2, width= 4,  command= lambda hue = hue: self.alternate_color_brush(color = hue) )
            self.btn_color.pack(side = "left", padx = 3)
        
        
        self.text_size = self._create_label("Size")
        
        self.spin_size = thin.Spinbox(self.bar_menu, from_ = 1, to = 50, width = 3)
        self.spin_size.pack(side = "left")
        
        
        
        self.images = self._import_images()
        self.btn_brush = []
        
        self.text_brush = self._create_label("Brush")
    
        for brush in ["line", "oval","square"]:
            
            btn_image = thin.Button(self.bar_menu, image=self.images[brush], bd = 0, command= lambda brush = brush : self.alternate_brush(brush=brush))
            btn_image.pack(side = "left")
            self.btn_brush.append(btn_image)
        
        self.btn_opt = []
        
        self.text_options = self._create_label("Options")
        
        for option in ["new", "save"]:
                
            btn_image = thin.Button(self.bar_menu, image=self.images[option], bd = 0, command= lambda opt = option: self.options_events(opt = opt))
            btn_image.pack(side = "left")
            self.btn_opt.append(btn_image)
        
        self.text_pick_color = self._create_label("Choose Color:") 
        self.picke_color = thin.Button(self.bar_menu, image= self.images["square"], bd = 0, command= self.picker_hue)
        self.picke_color.pack()
        
        
        self.canvas = thin.Canvas(self.window, height= self.size[1])
        self.canvas.pack(fill = "both")
        
        self.canvas.bind("<B1-Motion>", self.draw)
        
        # para adicionar uma atalho e necessario instanciar a janela principal e tambem a coloca a tecla entre as tags
        
        self.window.bind("<s>", self.options_events("save"))
        self.window.bind("<d>", self.options_events("new"))
        
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
   
    def draw(self, event)-> None:
        x1 , y1= (event.x) , (event.y)
        x2 , y2= (event.x) , (event.y)
        
        if self.oval:
            self.canvas.create_oval(x1, y1, x2, y2, fill = self.color_brush, outline= self.color_brush, width= self.spin_size.get())
            return None
        elif self.line:
            self.canvas.create_line(x1 - 10, y1 - 10, x2, y2, fill = self.color_brush, width= self.spin_size.get())
            return None
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill = "gainsboro", outline= "gainsboro", width= self.spin_size.get())
            return None
    
    def alternate_color_brush(self, color:str) -> None:
        
        self.color_brush = color
        
        return None
    
    def alternate_brush(self, brush: str) -> None:
        
        if brush is "oval":
            self.oval = True
            self.line, self.eraser = [False, False]
        elif brush is "line":
            self.line = True
            self.oval, self.eraser = [False, False]
        else:
            self.eraser = True
            self.line, self.oval = [False, False]
        return None

    def clear_draw(self) -> None:
        
        self.canvas.delete("all")
    
    def save(self):
        
        x = self.window.winfo_rootx() + self.canvas.winfo_x()
        y = self.window.winfo_rootx() + self.canvas.winfo_x()
        w = self.window.winfo_rootx() + self.canvas.winfo_width()
        h = self.window.winfo_rootx() + self.canvas.winfo_height()
        
        
        image = pyscreenshot.grab(bbox=[x, y, w, h])
        image.save("tentando.jpeg", "jpeg")
    
        
    def options_events(self, opt:str) -> None:
        
        if opt is "new":
            self.clear_draw()
        elif opt is "save":
            self.save()
        else:
            pass
        return None
    
    # ask abre uma menu picker color para escolher a cor 
    def picker_hue(self):
       color = askcolor()
       self.color_brush = color[1]

Paint()