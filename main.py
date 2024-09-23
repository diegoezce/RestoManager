from idlelib.configdialog import font_sample_text
import tkinter as tk
from tkinter import Checkbutton

app = tk.Tk()

app.geometry('1200x630+0+0')

app.resizable(0,0)

app.title('My Resto Manager')

app.config(bg='burlywood')

#upper frame
upper_frame = tk.Frame(app, bd=1, relief=tk.FLAT)
upper_frame.pack(side=tk.TOP)

title_label = tk.Label(upper_frame, text='Manager', fg='azure4',
                    font=('Dosis', 58), bg='burlywood', width=27)
title_label.grid(row=0, column=0)

left_frame = tk.Frame(app, bd=1, relief=tk.FLAT)
left_frame.pack(side=tk.LEFT)

cost_frame = tk.Frame(left_frame, bd = 1, relief = tk.FLAT)
cost_frame.pack(side=tk.BOTTOM)

food_frame = tk.LabelFrame(left_frame, text= 'Comida', bd=1, width=27, font=('Dosis', 19), relief=tk.FLAT, fg='azure4')
food_frame.pack(side=tk.LEFT)

bev_frame = tk.LabelFrame(left_frame, text= 'Beverages', bd=1, width=27, font=('Dosis', 19), relief=tk.FLAT, fg='azure4')
bev_frame.pack(side=tk.LEFT)

deserts_frame = tk.LabelFrame(left_frame, text= 'Desserts', bd=1, width=27, font=('Dosis', 19), relief=tk.FLAT, fg='azure4')
deserts_frame.pack(side=tk.LEFT)


#panel derecha
right_panel = tk.Frame(app, bd=1, relief=tk.FLAT)
right_panel.pack(side=tk.RIGHT)

#calculator panel
calc_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
calc_panel.pack()

receipt_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
receipt_panel.pack()

buttons_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
buttons_panel.pack()

#lista products
food_list = ['chicken', 'cordero', 'kebab', 'pizza1', 'pizza2']
bev_list = ['agua', 'soda', 'jugo', 'coke', 'beer', 'wine']
des_list = ['icecream', 'flan', 'cake', 'candy']



#generate food items
food_variables = []

indx = 0

for food in food_list:
    food_variables.append('')
    food_variables[indx] = tk.IntVar()
    comida = tk.Checkbutton(food_frame, text=food.title(),
                            font=('Dosis', 19, 'bold'),
                            variable=food_variables[indx])
    comida.grid(row=indx, column=0, sticky=tk.W)
    indx += 1

#generate food items
bev_variables = []
indx = 0

for bev in bev_list:
    bev_variables.append('')
    bev_variables[indx] = tk.IntVar()
    beverage = tk.Checkbutton(bev_frame, text=bev.title(),
                            font=('Dosis', 19, 'bold'),
                            variable=bev_variables[indx])
    beverage.grid(row=indx, column=0, sticky=tk.W)
    indx += 1

des_variables = []
indx = 0

for des in des_list:
    des_variables.append('')
    des_variables[indx] = tk.IntVar()
    dessert = tk.Checkbutton(deserts_frame, text=des.title(),
                            font=('Dosis', 19, 'bold'),
                            variable=des_variables[indx])
    dessert.grid(row=indx, column=0, sticky=tk.W)
    indx += 1

app.mainloop()