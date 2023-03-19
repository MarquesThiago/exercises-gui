import tkinter as thin

class Paint():

    def __init__(self):
        self.window = thin.Tk()
        self.window.title("Painter")
        self.size = [760, 520]
        self.window.minsize(width = self.size[0], height = self.size[1])
        self.window.resizable(0,0)
        self.bar_menu = thin.Frame(self.window, bg = "gray", height = 30)
        
        self.bar_menu.pack(fill = "x")        
        
        # canvas é uma area para inserção de formas geometriacas ou desenhos 
        # identico ao seu tradução quadro 
        
        self.canvas = thin.Canvas(self.window, width = self.size[1])
        
        # nos temos no fill both que preencho a area toda 
        
        self.canvas.pack(fill = "both")
        
        self.window.mainloop()


Paint()