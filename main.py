from idlelib.configdialog import font_sample_text
import tkinter as tk
from tkinter import Checkbutton
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_button (number):
    global operator
    operator = operator + number
    calc_visor.delete(0, tk.END)
    calc_visor.insert(tk.END, operator)

def delete ():
    global operator
    operator = ''
    calc_visor.delete(0, tk.END)

def get_result():
    global operator
    print(operator)
    result = str(eval(operator))
    calc_visor.delete(0, tk.END)
    calc_visor.insert(0, result)
    operator = ''

def revisar_check():
    x = 0
    for c in food_frames:
        if(food_variables[x].get() == 1):
            food_frames[x].config(state=tk.NORMAL)
            if food_frames[x].get() == '0':
                food_frames[x].delete(0, tk.END)
            food_frames[x].focus()
        else:
            food_frames[x].config(state=tk.DISABLED)
            food_text[x].set('0')
        x +=1

    x = 0
    for c in bev_frames:
        if(bev_variables[x].get() == 1):
            bev_frames[x].config(state=tk.NORMAL)
            if bev_frames[x].get() == '0':
                bev_frames[x].delete(0, tk.END)
            bev_frames[x].focus()
        else:
            bev_frames[x].config(state=tk.DISABLED)
            bev_text[x].set('0')
        x +=1

    x = 0
    for c in des_frames:
        if(des_variables[x].get() == 1):
            des_frames[x].config(state=tk.NORMAL)
            
            if des_frames[x].get() == '0':
                des_frames[x].delete(0, tk.END)
            
            des_frames[x].focus()
        else:
            des_frames[x].config(state=tk.DISABLED)
            des_text[x].set('0')
        x +=1


def total():
    sub_total_food = 0
    p = 0
    for cant in food_text:
        sub_total_food = sub_total_food + (float(cant.get()) * precios_comida[p])
        p += 1

    sub_total_bev = 0
    p = 0
    for cant in bev_text:
        sub_total_bev = sub_total_bev + (float(cant.get()) * precios_bebida[p])
        p += 1

    
    sub_total_des = 0
    p = 0
    for cant in des_text:
        sub_total_des = sub_total_des + (float(cant.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_food + sub_total_bev + sub_total_des

    taxes = sub_total * 0.07

    total = sub_total + taxes

    var_bev_cost.set(f'$ {round(sub_total_bev, 2)}')
    var_des_cost.set(f'$ {round(sub_total_des, 2)}')
    var_food_cost.set(f'$ {round(sub_total_food, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(taxes, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    rec_text.delete(1.0, tk.END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day} / {fecha.month} / {fecha.year} - {fecha.hour}:{fecha.minute}'
    rec_text.insert(tk.END, f'Datos:\t {num_recibo}\t\t{fecha_recibo}')
    rec_text.insert(tk.END, f'*' * 65 + '\n')
    rec_text.insert(tk.END, 'Items \t\tCant.\tCosto Items\n')
    rec_text.insert(tk.END, f'-' * 74 + '\n')

    x = 0
    for food in food_text:
        if food.get() != '0':
            rec_text.insert(tk.END, f'{food_list[x]}\t\t{food.get()}\t'
                                    f'$ {int(food.get()) * precios_comida[x]}\n')
        x += 1


    x = 0
    for bev in bev_text:
        if bev.get() != '0':
            rec_text.insert(tk.END, f'{bev_list[x]}\t\t{bev.get()}\t'
                                    f'$ {int(bev.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for des in des_text:
        if des.get() != '0':
            rec_text.insert(tk.END, f'{des_list[x]}\t\t{des.get()}\t'
                                    f'$ {int(des.get()) * precios_comida[x]}\n')
        x += 1


    rec_text.insert(tk.END, f'-' * 64 + '\n')
    rec_text.insert(tk.END, f' Costo comida: \t\t\t{var_food_cost.get()}\n')
    rec_text.insert(tk.END, f' Costo bebidas: \t\t\t{var_bev_cost.get()}\n')
    rec_text.insert(tk.END, f' Costo postre: \t\t\t{var_des_cost.get()}\n')
    
    rec_text.insert(tk.END, f'-' * 64 + '\n')
    rec_text.insert(tk.END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    rec_text.insert(tk.END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    rec_text.insert(tk.END, f' Total: \t\t\t{var_total.get()}')

def guardar():
    info_receipt = rec_text.get(1.0, tk.END)
    file  = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(info_receipt)
    file.close()


def reset():
    rec_text.delete(0.1, tk.END)
    for text in food_text:
        text.set('0')
    for text in bev_text:
        text.set('0')
    for text in des_text:
        text.set('0')

    for frame in food_frames:
        frame.config(state=tk.DISABLED)
    
    for frame in bev_frames:
        frame.config(state=tk.DISABLED)
    
    for frame in des_frames:
        frame.config(state=tk.DISABLED)

    for v in bev_variables:
        v.set(0)

    for v in food_variables:
        v.set(0)

    for v in des_variables:
        v.set(0)


    var_bev_cost.set('')
    var_food_cost.set('')
    var_des_cost.set('')
    var_total.set('')
    var_impuestos.set('')
    var_subtotal.set('')
    

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

cost_frame = tk.Frame(left_frame, bd = 1, relief = tk.FLAT, bg='azure4', padx= 50)
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
bev_list = ['agua', 'soda', 'jugo', 'coke', 'beer']
des_list = ['icecream', 'flan', 'cake', 'candy', 'postre2']




#generate food items

food_variables = []
food_text = []
food_frames = []
indx = 0

for food in food_list:
    food_variables.append('')
    food_variables[indx] = tk.IntVar()
    comida = tk.Checkbutton(food_frame,
                            text=food.title(),
                            font=('Dosis', 19, 'bold'),
                            variable=food_variables[indx],
                            command=revisar_check)
    comida.grid(row=indx,
                column=0,
                sticky=tk.W)

    food_frames.append('')
    food_text.append('')
    food_text[indx] = tk.StringVar()
    food_text[indx].set('0')
    food_frames[indx] = tk.Entry(food_frame,
                                 font=('Dosis', 18, 'bold'),
                                 bd =1,
                                 width=6,
                                 state= tk.DISABLED,
                                 textvariable=food_text[indx])
    food_frames[indx].grid(row=indx,
                           column = 1)



    indx += 1

#generate Beverages items
bev_variables = []
bev_text = []
bev_frames = []
indx = 0

for bev in bev_list:
    bev_variables.append('')
    bev_variables[indx] = tk.IntVar()
    beverage = tk.Checkbutton(bev_frame, 
                              text=bev.title(),
                              font=('Dosis', 19, 'bold'),
                              variable=bev_variables[indx],
                              command=revisar_check)
    beverage.grid(row=indx, 
                  column=0, 
                  sticky=tk.W)
    
    bev_frames.append('')
    bev_text.append('')
    bev_text[indx] = tk.StringVar()
    bev_text[indx].set('0')
    bev_frames[indx] = tk.Entry(bev_frame,
                                 font=('Dosis', 18, 'bold'),
                                 bd =1,
                                 width=6,
                                 state= tk.DISABLED,
                                 textvariable=bev_text[indx])
    bev_frames[indx].grid(row=indx,
                           column = 1)



    indx += 1

#generate Desserts items
des_variables = []
des_text = []
des_frames = []
indx = 0

for des in des_list:
    des_variables.append('')
    des_variables[indx] = tk.IntVar()
    dessert = tk.Checkbutton(deserts_frame, 
                             text=des.title(),
                             font=('Dosis', 19, 'bold'),
                             variable=des_variables[indx],
                             command=revisar_check)
    dessert.grid(row=indx, column=0, sticky=tk.W)

    des_frames.append('')
    des_text.append('')
    des_text[indx] = tk.StringVar()
    des_text[indx].set('0')
    des_frames[indx] = tk.Entry(deserts_frame,
                                 font=('Dosis', 18, 'bold'),
                                 bd =1,
                                 width=6,
                                 state= tk.DISABLED,
                                 textvariable=des_text[indx])
    des_frames[indx].grid(row=indx,
                           column = 1)



    indx += 1

var_food_cost = tk.StringVar()
var_bev_cost = tk.StringVar()
var_des_cost = tk.StringVar()

var_subtotal = tk.StringVar()
var_impuestos = tk.StringVar()
var_total = tk.StringVar()


#Prices / and entry fields
food_price_label = tk.Label(cost_frame,
                            text= 'Costo Comida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
food_price_label.grid(row=0, column=0, padx=41)

food_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_food_cost
                            )
food_price_text.grid(row=0,column=1)


bev_price_label = tk.Label(cost_frame,
                            text= 'Costo Bebida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
bev_price_label.grid(row=1, column=0, padx=41)

bev_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_bev_cost
                            )
bev_price_text.grid(row=1,column=1)



des_price_label = tk.Label(cost_frame,
                            text= 'Costo Postre',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
des_price_label.grid(row=2, column=0, padx=41)

des_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_des_cost
                            )
des_price_text.grid(row=2,column=1)

#SUBTOTAL

subtotal_price_label = tk.Label(cost_frame,
                            text= 'Subtotal',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
subtotal_price_label.grid(row=0, column=2, padx=41)

subtotal_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_subtotal
                            )
subtotal_price_text.grid(row=0,column=3, padx=41)

#IMPUESTOS

impuestos_price_label = tk.Label(cost_frame,
                            text= 'Impuestos',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
impuestos_price_label.grid(row=1, column=2, padx=41)

impuestos_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_impuestos
                            )
impuestos_price_text.grid(row=1,column=3, padx=41)


#TOTAL

total_price_label = tk.Label(cost_frame,
                            text= 'Total',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white'
                            )
total_price_label.grid(row=2, column=2, padx=41)

total_price_text = tk.Entry(cost_frame,
                            font=('Dosis', 12, 'bold'),
                            width=10,
                            state='readonly',
                            bd= 1,
                            textvariable=var_total
                            )
total_price_text.grid(row=2,column=3)

#BOTONES
buttons = ['total', 'recibo', 'guardar', 'resetear']
buttons_created = []



columns =0
for button in buttons:
    button = tk.Button(buttons_panel,
                       text = button.title(),
                       font=('Dosis', 12, 'bold'),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=9
                       )
    buttons_created.append(button)
    button.grid(row=0,
                column=columns
                )
    columns +=1

buttons_created[0].config(command=total)
buttons_created[1].config(command=recibo)
buttons_created[2].config(command=guardar)
buttons_created[3].config(command=reset)

#Receipt AREA

rec_text = tk.Text(receipt_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=42,
                   height=10
                   )
rec_text.grid(row=0, column=0)

 
 #CALCULADORA

calc_visor = tk.Entry(calc_panel,
                       font=('Dosis', 16,'bold'),
                       width=32,
                       bd=1)
calc_visor.grid(row=0,
                column=0,
                columnspan=4)

calc_buttons = ['7', '8', '9','+',
                '4', '5', '6', '-',
                '1','2','3','*',
                'R','B','0','/']

saved_buttons = []

row = 1
column = 0
for button in calc_buttons:
    button = tk.Button(buttons_panel,
                       text= button.title(),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=8)
    saved_buttons.append(button)
    button.grid(row=row, column=column)

    if(column == 3):
        row += 1

    column +=1

    if(column == 4):
        column = 0


saved_buttons[0].config(command=lambda : click_button('7'))
saved_buttons[1].config(command=lambda : click_button('8'))
saved_buttons[2].config(command=lambda : click_button('9'))
saved_buttons[3].config(command=lambda : click_button('+'))
saved_buttons[4].config(command=lambda : click_button('4'))
saved_buttons[5].config(command=lambda : click_button('5'))
saved_buttons[6].config(command=lambda : click_button('6'))
saved_buttons[7].config(command=lambda : click_button('-'))
saved_buttons[8].config(command=lambda : click_button('1'))
saved_buttons[9].config(command=lambda : click_button('2'))
saved_buttons[10].config(command=lambda : click_button('3'))
saved_buttons[11].config(command=lambda : click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda : click_button('0'))
saved_buttons[15].config(command=lambda : click_button('/'))





app.mainloop()
