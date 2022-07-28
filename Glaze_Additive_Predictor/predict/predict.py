import pandas
from sklearn import linear_model

V= ""
R= ""
fF= ""

def predict(V, R, fF):

    df = pandas.read_excel("GLAZE_DATASET.xlsx")

    X = df[['dD','fF']]
    y = df[['CMC','Water']]

    model = linear_model.LinearRegression()
    model.fit(X.values, y.values)

    V = float (V.get())
    R = float (R.get())
    fF = int (fF.get())

    dD = V - R

    prediction = model.predict([[dD, fF]])

    return prediction