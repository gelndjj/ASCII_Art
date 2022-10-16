from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pyfiglet

root =Tk()
root.geometry('700x400')
root.title('ASCII Art')

your_txt = Label(root, text='Your text : ')
your_txt.place(x=10, y=10)

field = Entry(root, bd=3, relief=RIDGE)
field.place(x=100, y=10)

txt_box = Text(root, height=22, width=90, bd=3, relief=SUNKEN)
txt_box.place(x=10, y=90)

font_list = ['3-d',
            '6x10', 
            'avatar',
            'banner4', 
            'basic',
            'big', 
            'block', 
            'bulbhead', 
            'chunky', 
            'colossal', 
            'crawford', 
            'digital',
            'doh', 
            'doom', 
            'drpepper',
            'eftirobot', 
            'epic',
            'fuzzy', 
            'graceful', 
            'isometric1', 
            'larry3d', 
            'nancyj', 
            'ogre', 
            'pawp', 
            'puffy', 
            'rectangles',
            'rev', 
            'roman',
            'rounded', 
            'shadow',
            'slant', 
            'small', 
            'smisome1', 
            'smkeyboard', 
            'smslant',
            'univers'
            ]

font_combo = ttk.Combobox(root, values=font_list, width=10)
font_combo.set('select')
font_combo.place(x=300, y=11)

def turn_to():
    if field.get() == '':

        messagebox.showinfo(title='Field empty', message='Write your text first!!!')
    
    elif font_combo.get() == 'select':

        messagebox.showinfo(title='Font unknown', message='Select your font!')

    else:

        txt_box.delete('1.0', END)
        text_to = str(field.get())
        result = pyfiglet.figlet_format(text_to, font=font_combo.get())
        txt_box.insert(END, result)

def show_me():
    if field.get() == '':

        messagebox.showinfo(title='Field empty', message='Write your text first!!!')
    
    else:

        txt_box.delete('1.0', END)
        text_to = str(field.get())

        for item in font_list:
            title = 'Font name %s \n\n' % item
            result = pyfiglet.Figlet(font=item)
            txt_box.insert(END, title + result.renderText(text_to))

def copy():
    root.clipboard_clear()
    root.clipboard_append(txt_box.get('1.0', END))

btn_do_it = Button(root, text='ASCII', command=turn_to)
btn_do_it.place(x=10, y=45)
btn_show_me = Button(root, text='Show me all fonts', command=show_me)
btn_show_me.place(x=290, y=45)
btn_copy = Button(root, text='Copy', command=copy)
btn_copy.place(x=80, y=45)

root.mainloop()
