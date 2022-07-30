import os

import pandas
from sklearn import linear_model

v= ""
V= ""
R= ""
fF= ""

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