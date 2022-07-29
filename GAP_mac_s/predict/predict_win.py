from tkinter import *

def predict_win(prediction):
    child = Tk()

    child.title("Prediction")
    child.geometry("300x200")
    child.resizable(width=False, height=False)

    Label(child, text= "Amount of CMC (g) -").place(x=30,y=50)
    Label(child, text= round(prediction[0][0],2)).place(x=210,y=50)

    Label(child, text="Amount of Water (ml) -").place(x=30, y=100)
    Label(child, text= round(prediction[0][1], 2)).place(x=210, y=100)

    Button(child, text= "OK", command= child.destroy).place(x=135,y=150)