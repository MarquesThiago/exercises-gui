import tkinter as tk
from PIL import ImageTk, Image
import os 



window = tk.Tk()
window.title("test bg")
window.geometry("800x500")

bg = "#f3f3f3"

# window.wm_attributes('-transparentcolor', "#f3f3f3" )

# window.wm_overrideredirect(True)
# window.wm_attributes('-topmost', True)
window.wm_attributes('-transparent', window["bg"])

w  = window.winfo_width()
h = window.winfo_height()

canvas = tk.Canvas(window, width = w, height= h)
canvas.pack(fill = "both", expand = True)


back = Image.open(os.path.join(os.getcwd(), 'bg.jpg'))
test =  back.resize((w,h), Image.ANTIALIAS)
image = ImageTk.PhotoImage(back)

canvas.create_image(0,0, image = image, anchor = "nw")

frame = tk.Frame(window, width= w, height= h)
frame.place(x = 0, y = 0, relwidth= 1, relheight= 1 )

label = tk.Label(frame, text = "test")

label.pack()

label2 = tk.Label(frame, text = "test", bg = bg, font= "Arial 60")
label2.pack()
label3 = tk.Label(frame, text = "test")
label3.pack()
label4 = tk.Label(frame, text = "test")
label4.pack()
label5 = tk.Label(frame, text = "test")
label5.pack()


canvas.create_window(0,0,anchor="nw", window=frame)

window.mainloop()