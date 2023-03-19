import tkinter as thin
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
        
        self.images = self._import_images()
        self.btn_brush = []
        
        self.text_color = thin.Label(self.bar_menu, text= "Colors: ", fg = "white", bg = "gray")
        self.text_color.pack(side = "left", padx= 20)
        
        self.pick_color = {"black", "orange", "pink", "white", "red", "blue", "gray", "green", "purple", "brown"}
        
        for hue in self.pick_color:
            self.btn_color = thin.Button(self.bar_menu, bg= hue, height= 2, width= 4,  command=None )
            self.btn_color.pack(side = "left", padx = 3)
        
        self.text_brush = thin.Label(self.bar_menu, text= "Brush: ", fg = "white", bg = "gray")
        self.text_brush.pack(side = "left", padx= 20)
        
        
        
        for brush in [self.images["line"], self.images["oval"], self.images["square"]]:
            
            # temos o parametro bd que e a densidade da borda ou seja o tamanho da borda
            btn_image = thin.Button(self.bar_menu, image=brush, bd = 0)
            btn_image.pack(side = "left")
            self.btn_brush.append(btn_image)
        
        
        self.canvas = thin.Canvas(self.window, width = self.size[1])
        self.canvas.pack(fill = "both")
        
        self.window.mainloop()
        
        
    def _import_images(self) -> dict:
            
        root = os.path.join(self.root, "../imgs/")
        
        print(os.path.join(root, "eraser.png"))
            
            # O PhotoImage ele importa a imagem para o processo
        return {
                "eraser": thin.PhotoImage(file = os.path.join(root, "eraser.png")),
                "line": thin.PhotoImage(file= os.path.join(root, "line.png")),
                "new": thin.PhotoImage(file = os.path.join(root, "new.png")),
                "oval": thin.PhotoImage(file = os.path.join(root, "oval.png")),
                "save": thin.PhotoImage(file = os.path.join(root, "save.png")),
                "square": thin.PhotoImage(file = os.path.join(root, "square.png"))
        }


Paint()