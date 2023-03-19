from tkinter import *
from Calculator import Calculator

root = Tk()
root.title("Calculator")

entry = Entry(root, width = 70, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

action_cal = Calculator(entry)

def click(value):
    action_cal.click_calc(value)


button_1 = Button(root, text= "1", padx = 45, pady = 20, command = lambda: click(1) )
button_2 = Button(root, text= "2", padx = 45, pady = 20, command = lambda: click(2) )
button_3 = Button(root, text= "3", padx = 45, pady = 20, command = lambda: click(3) )
button_4 = Button(root, text= "4", padx = 45, pady = 20, command = lambda: click(4) )
button_5 = Button(root, text= "5", padx = 45, pady = 20, command = lambda: click(5) )
button_6 = Button(root, text= "6", padx = 45, pady = 20, command = lambda: click(6) )
button_7 = Button(root, text= "7", padx = 45, pady = 20, command = lambda: click(7) )
button_8 = Button(root, text= "8", padx = 45, pady = 20, command = lambda: click(8) )
button_9 = Button(root, text= "9", padx = 45, pady = 20, command = lambda: click(9) )
button_0 = Button(root, text= "0", padx = 45, pady = 20, command = lambda: click(0) )

lista_button  = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0]
 
def grid_buttons(list):

    column = 0
    controler_row = 3
    for i in range(0, 9) :
    
        row = int(controler_row / 3)
        
        list[i].grid(row = row, column = column )
        column+=1
        controler_row+=1

        if(column == 3):
            column = 0
    

grid_buttons(lista_button)
lista_button[9].grid(row = 4, column = 1 )


button_mult = Button(root, text =  "*", padx = 45, pady = 20, command = lambda: click("*"))
button_div = Button(root, text =  "/", padx = 45, pady = 20, command = lambda: click("/"))
button_sum = Button(root, text =  "+", padx = 45, pady = 20, command = lambda: click("+"))
button_neg = Button(root, text =  "-", padx = 45, pady = 20, command = lambda: click("-"))

button_div.grid(row = 1 , column = 3)
button_mult.grid(row = 2 , column = 3)
button_neg.grid(row = 3 , column = 3)
button_sum.grid(row = 4 , column = 3)

button_clear = Button(root, text = "C", padx = 45, pady = 20, command = lambda: click('del'))
button_equal = Button(root, text = "=", padx = 45, pady = 20, command = lambda: click("result"))


button_clear.grid(row = 4, column = 0 )
button_equal.grid(row = 4, column = 2 )



root.mainloop()
