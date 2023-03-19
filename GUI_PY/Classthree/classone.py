import tkinter as thin

class Paint():

    def __init__(self):
        self.window = thin.Tk()
        self.window.title("Painter")
        self.window.minsize(width = 760, height = 860)
        self.window.resizable(0,0)
        self.bar_menu = thin.Frame(self.window, bg = "gray", height = 30)
        
        self.bar_menu.pack(fill = "x")        
        
        
        self.window.mainloop()








Paint()