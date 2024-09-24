from tkinter import *
import pyautogui as pau
from typing import *

app = Tk()

app.geometry('860x720+700+180')
app.title('Auto Typer 1.0')
app.resizable(0,0)

def autoTyping():
    pau.moveTo(350,500)
    pau.click()
    pau.typewrite(f'{msg.get()}', interval = interval1.get()/1000)

def quit_app():
    app.destroy()

def clear():
    pau.moveTo(350,500)
    pau.click()
    pau.hotkey('ctrl','a')
    pau.press('delete')

msg = StringVar()

interval1 = IntVar()

l1 = Label(app, text = 'interval', font = 'HY견고딕')
l1.place(relx = '0.45', rely = '0.2')

s1 = Scale(app, variable = interval1, orient = 'horizontal', showvalue = True,to = 1000, length = 660, cursor = 'cross', font = 'HY견고딕')
s1.place(relx = '0.1', rely = '0.25')

textbox = Entry(app, cursor = 'dotbox', width = 50, textvariable = msg, font = 'HY견고딕')
textbox.place(x = 410, y = 370, anchor = 'center')

b1 = Button(app, text = '입력', cursor = 'dot', font = 'HY견고딕', command = autoTyping)
b1.place(relx = '0.2', rely = '0.75')

b2 = Button(app, text = '삭제', cursor = 'dot', font = 'HY견고딕', command = clear)
b2.place(relx = '0.45', rely = '0.75')

b3 = Button(app, text = '종료', cursor = 'dot', font = 'HY견고딕', command = quit_app)
b3.place(relx = '0.7', rely = '0.75')

app.mainloop()