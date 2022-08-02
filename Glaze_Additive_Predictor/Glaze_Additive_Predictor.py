import sys
import platform
import os
import shutil
import pandas



from tkinter import *
from sklearn import linear_model
from PIL import ImageTk, Image


#Functions

#1 - Resource Path Mapping
def res_path(relative_path):

    if platform.system()=='Darwin':
        if (os.getcwd().__contains__("Resources")):
            base_path = os.getcwd()
        else:
            base_path = os.path.abspath("./res")
    elif platform.system()=='Windows':
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        base_path = os.path.join(base_path, 'res')

    return os.path.join(base_path, relative_path)

#2 - Checking Dependencies
def check():
    if os.path.exists(os.path.join(os.path.expanduser('~'), 'Documents', 'com.soujatya_sarkar.gap')) == False:
        os.mkdir(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'icon.ico')) == False:
        shutil.copy(res_path("icon.ico"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'logo.png')) == False:
        shutil.copy(res_path("logo.png"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'GLAZE_DATASET.xlsx')) == False:
        shutil.copy(res_path("GLAZE_DATASET.xlsx"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

#3 - About
def about():
    ab = Tk()

    ab.title("About")
    ab.geometry("500x200")
    ab.resizable(width=False, height=False)

    if platform.system() == 'Windows':
        fs = 12
        ab.iconbitmap(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap','icon.ico'))
    elif platform.system() == 'Darwin':
        fs = 14
        menubar = Menu(ab)
        ab.config(menu= menubar)

    Label(ab, text="Glaze Additive Predictor", font=("Heveltica Neue", 20, 'bold')).pack(pady=15)
    Label(ab, text="Copyright © 2022, Soujatya Sarkar, All Rights Reserved.", font=("Heveltica Neue", fs, 'bold')).pack()
    Label(ab, text="Computational Development and Research - Soujatya Sarkar").pack()
    Label(ab, text="Chemical Data Collection - Tapabrata Mondal and Soujatya Sarkar").pack()
    Label(ab, text="Author and Inventor - Soujatya Sarkar").pack()
    Label(ab, text="Version - 1.0.0", font=("Heveltica Neue", fs, 'bold')).pack()

#4 - Prediction Algorithm

def predict(v, V, R, fF):
    df = pandas.read_excel(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap','GLAZE_DATASET.xlsx'))

    X = df[['dD','fF']]
    y = df[['CMC','Water']]

    model = linear_model.LinearRegression()
    model.fit(X.values, y.values)

    v = float (v.get())
    V = float (V.get())
    R = float (R.get())
    fF = int (fF.get())

    dD = V - R

    prediction = model.predict([[dD, fF]])

    return prediction*v

#5 - Prediction
def predict_win(prediction):
    child = Tk()

    child.title("Prediction")
    child.geometry("300x200")
    child.resizable(width=False, height=False)

    if platform.system() == 'Windows':
        child.iconbitmap(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap','icon.ico'))
    elif platform.system() == 'Darwin':
        menubar = Menu(child)
        child.config(menu= menubar)

    Label(child, text= "Amount of CMC (g) -").place(x=30,y=50)
    Label(child, text= round(prediction[0][0],2)).place(x=210,y=50)

    Label(child, text="Amount of Water (ml) -").place(x=30, y=100)
    Label(child, text= round(prediction[0][1], 2)).place(x=210, y=100)

    Button(child, text= "OK", command= child.destroy).place(x=135,y=150)


#Glaze Additive Predictor

check()

top = Tk()

top.title("Glaze Additive Predictor")
top.geometry("430x360")
top.resizable(width=False, height=False)

if platform.system() == 'Windows':
    top.iconbitmap(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'icon.ico'))

menubar = Menu(top)
top.config(menu= menubar)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(
    label='About',
    command= about
)

if platform.system() == 'Darwin':
    file_menu.add_command(
        label='Close',
        command= sys.exit,
        accelerator= "Command-W"
    )

    file_menu.bind_all("<Command-w>", sys.exit)

elif platform.system() == 'Windows':
    file_menu.add_command(
        label='Close',
        command=sys.exit,
        accelerator="Ctrl+W"
    )

    file_menu.bind_all("<Control-w>", sys.exit)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

logoframe= Frame(top)
logoframe.pack(pady=15)

logo = ImageTk.PhotoImage(Image.open(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap',
                                                  'logo.png')).resize((69, 69), Image.Resampling(1)))
Label(logoframe, image= logo).pack()

vVolume = Label(top, text="Virgin Glaze Volume (L)").place(x=30,y=100)
vDensity = Label(top, text="Virgin Glaze Density (g/cc)").place(x=30,y=150)
rDensity = Label(top, text="Required Density (g/cc)").place(x=30,y=200)
rFluidity = Label(top, text="Required Fluidity (°/swing)").place(x=30,y=250)

if platform.system()=='Windows':
    w = 30
elif platform.system()=='Darwin':
    w = 20



vV = Entry(top, width = w)
vV.place(x=200,y=100)

vD = Entry(top, width = w)
vD.place(x=200,y=150)

rD = Entry(top, width = w)
rD.place(x=200,y=200)

rF = Entry(top, width = w)
rF.place(x=200,y=250)



def callback():
    prediction = predict(vV, vD, rD, rF)
    predict_win(prediction)

b = Button(top, text= "Submit", command= callback).place(x=175,y=300)

top.mainloop()