from predict.predict import *
from predict.predict_win import *
from predict.about import *
from PIL import ImageTk, Image

top = Tk()

top.title("Glaze Additive Predictor")
top.geometry("430x300")
top.resizable(width=False, height=False)


menubar = Menu(top)
top.config(menu= menubar)

file_menu = Menu(menubar)

file_menu.add_command(
    label='About',
    command= about,
)
file_menu.add_command(
    label='Close',
    command= top.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

logoframe= Frame(top)
logoframe.pack(pady=15)

logo = ImageTk.PhotoImage(Image.open("abi.jpg").resize((71, 69), Image.Resampling(1)))
Label(logoframe, image= logo).pack()

vDensity = Label(top, text="Virgin Glaze Density").place(x=30,y=100)
rDensity = Label(top, text="Required Density").place(x=30,y=150)
rFluidity = Label(top, text="Required Fluidity").place(x=30,y=200)

vD = Entry(top)
vD.place(x=200,y=100)

rD = Entry(top)
rD.place(x=200,y=150)

rF = Entry(top)
rF.place(x=200,y=200)


def callback():
    prediction = predict(vD, rD, rF)
    predict_win(prediction)

b = Button(top, text= "Submit", command= callback).place(x=175,y=250)

top.mainloop()