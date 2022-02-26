import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
from PIL import ImageTk, Image
#import matplotlib.pylot as plt
import numpy as np
from tkinter import filedialog
import shutil
import os



def possibleExpansion(root):
    framePossEx = Frame(root, height=350)
    framePossEx.pack(side=TOP, fill=X)

def generateExpansion(root):
    genExp  = Toplevel()
    genExp.geometry('500x500')
    selectedUni = cb.get()
    genExp.title(selectedUni)
    lblReport = Label(genExp, text="Report for " + selectedUni, fg='red', font=('Helvetica',16))
    lblReport.place(x=50, y=25)

    gradRate = np.array()


def specificUniv(root):
    frameSpUniv = Frame(root, height=350)
    frameSpUniv.pack(side=TOP, fill=X)
    root.title('Details on University')
    print(data)
    lbl = Label(root, text="Pick a university", fg='red', font=('Helvetica', 16))
    lbl.place(x=165, y=110)

    global univ
    univ = df['INSTNM'].tolist()

    global cb
    cb = Combobox(root, values=univ, width=30, state='readonly', justify='left')
    cb.place(x=150, y=150)

    btn = Button(root, text="Generate report", fg='blue', command = lambda:generateExpansion(root))
    btn.place(x=190, y=200)


def dataBase():
    dataWindow = Toplevel()
    dataWindow.geometry('500x350')
    dataWindow.title("Database Options")

    btnBrowse = Button(dataWindow, text="Select Database", fg='blue', command = lambda:browseFiles())
    btnBrowse.place(x = 350, y = 200)

    btnUpload = Button(dataWindow, text="Upload Database", fg='blue', command=lambda: uploadNewDatabase())
    btnUpload.place(x=250, y=200)

    btnClose =Button(dataWindow, text="Close Window", fg='blue', command= lambda : dataWindow.destroy())
    btnClose.place(x = 150, y = 200)

def uploadNewDatabase():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("CSV files",
                                                      ".csv"),
                                                     ("all files",
                                                      ".")))
    directory = filedialog.askdirectory(initialdir="/",
                                        title="Select a Directory")
    shutil.move(filename, directory)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("CSV files",
                                                      ".csv"),
                                                     ("all files",
                                                      ".")))
    data = filename



def home(root):
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma Expansion Tool')

    openImg = Image.open("PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=165, y=0)

    btn = Button(text="Possible Expansion", command=lambda: possibleExpansion(root), fg='blue')
    btn.place(x=75, y=300)

    btn1 = tkinter.Button(text="Specific University", command=lambda: specificUniv(root), fg='blue')
    btn1.place(x=300, y=300)

    btn2 = tkinter.Button(text="Database", command=lambda: dataBase(), fg='blue')
    btn2.place(x=210, y=300)

if __name__=="__main__":
    root = Tk()
    global data
    global filename
    data = filename
    df = pd.read_csv(data)
    home(root)
    root.mainloop()