from tkinter import *

def about():
    ab= Tk()

    ab.title("About")
    ab.geometry("500x200")
    ab.resizable(width=False, height=False)

    menubar = Menu(ab)
    ab.config(menu= menubar)

    Label(ab, text= "Glaze Additive Predictor", font= ("Heveltica Neue", 20, 'bold')).pack(pady=15)
    Label(ab, text= "Copyright © 2022, Soujatya Sarkar", font= ("Heveltica Neue", 14, 'bold')).pack()
    Label(ab, text= "Computational Development and Research - Soujatya Sarkar").pack()
    Label(ab, text= "Chemical Data Collection - Tapabrata Mondal and Soujatya Sarkar").pack()
    Label(ab, text= "Supervised by - Mr. Arindam Ghosh").pack()
    Label(ab, text= "Version - 1.0.0", font= ("Heveltica Neue", 14, 'bold')).pack()