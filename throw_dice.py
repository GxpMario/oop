"""Click the button to throw a dice!"""

from tkinter import *
from tkinter import ttk
import numpy as np

root = Tk()
label = ttk.Label(root, text='I am a fair and flat dice')
label.pack()
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='black', background='green')
label.config(font=('Roboto', 12, 'bold'))
button = ttk.Button(root, text='Roll me')
button.pack()


def dice():
    print(np.random.randint(1, 7))


button.config(command=dice)

root.mainloop()
