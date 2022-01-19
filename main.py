import tkinter
import pandas as pd
from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image


window = Tk()
col_list = ['INSTNM']
df = pd.read_csv('College_Scorecard_1-19-2021.csv', usecols = col_list)

def possibleExpansion():
    print("Still needs development")

def specificUniv():
    spec = Toplevel()
    spec.title('Details on a University')
    spec.geometry("500x350")

    lbl = Label(spec, text = "Pick a university", fg = 'red', font = ('Helvetica', 16))
    lbl.place(x = 165, y = 110)

    print(df)

    value = "{" + df + "}"

    cb = Combobox(spec, values = value, width = 50, state = 'readonly', justify = 'left')
    cb.place(x = 100, y = 150)

    btn = Button(spec, text = "Generate report", fg = 'blue')
    btn.place(x = 190, y = 200)

    spec.mainloop()


if __name__=="__main__":
    window.title('University Analysis')
    window.geometry("500x350")

    openImg = Image.open("PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x = 165, y = 0)



    btn = Button(text = "Possible Expansion", command = possibleExpansion, fg = 'blue')
    btn.place(x = 120, y = 300)

    btn1 = tkinter.Button(text = "Specific University", command = specificUniv, fg = 'blue')
    btn1.place(x = 250, y = 300)

    window.mainloop()