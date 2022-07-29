from predict.prediction import *
from predict.predict_win import *
from predict.about import *
from PIL import ImageTk, Image

top = Tk()

top.title("Glaze Additive Predictor")
top.geometry("430x360")
top.resizable(width=False, height=False)
top.iconbitmap("C:/Users/souja/PycharmProjects/GAP_win/abi.ico")

menubar = Menu(top)
top.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(
    label='About',
    command=about,
)
file_menu.add_command(
    label='Close',
    command=top.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

logoframe = Frame(top)
logoframe.pack(pady=15)

logo = ImageTk.PhotoImage(Image.open("C:/Users/souja/PycharmProjects/GAP_win/abi.jpg").resize((71, 69), Image.Resampling(1)))
Label(logoframe, image=logo).pack()

vVolume = Label(top, text="Virgin Glaze Volume (L)").place(x=30,y=100)
vDensity = Label(top, text="Virgin Glaze Density (g/cc)").place(x=30,y=150)
rDensity = Label(top, text="Required Density (g/cc)").place(x=30,y=200)
rFluidity = Label(top, text="Required Fluidity (°/swing)").place(x=30,y=250)

vV = Entry(top, width=30)
vV.place(x=200,y=100)

vD = Entry(top, width=30)
vD.place(x=200,y=150)

rD = Entry(top, width=30)
rD.place(x=200,y=200)

rF = Entry(top, width=30)
rF.place(x=200,y=250)


def callback():
    prediction = predict(vV, vD, rD, rF)
    predict_win(prediction)


b = Button(top, text="Submit", command=callback).place(x=175, y=300)

top.mainloop()