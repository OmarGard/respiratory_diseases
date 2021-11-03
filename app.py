from flask import Flask, render_template, request
import pandas as pd
import pickle
import warnings
import numpy as np
warnings.filterwarnings('ignore')
app = Flask(__name__, template_folder='templates')

with open(f'models/resp_dis_m7.pkl', 'rb') as f:
    model_7 = pickle.load(f)

with open(f'models/resp_dis_m8.pkl', 'rb') as f:
    model_8 = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    cols_m7 = ['Fgas', 'N2O', 'CH4', 'CO2', 'mean_annual_temp']
    cols_m8 = ['Fgas', 'mean_annual_temp']
    model_selected = request.form.get('models')
    data_unseen = []
    prediction = []
    if model_selected == "M7":
        fgas = request.form.get('FGas')
        n2o = request.form.get('N2O')
        ch4 = request.form.get('CH4')
        co2 = request.form.get('CO2')
        temp = request.form.get('Temp')
        if fgas == "":
            return render_template('index.html', pred=f"FGas no puede estar vacío")
        if n2o == "":
            return render_template('index.html', pred=f"N2O no puede estar vacío")
        if ch4 == "":
            return render_template('index.html', pred=f"CH4 no puede estar vacío")
        if co2 == "":
            return render_template('index.html', pred=f"CO2 no puede estar vacío")
        if temp == "":
            return render_template('index.html', pred=f"Temperatura no puede estar vacío")

        x = np.array([fgas, n2o, ch4, co2, temp])
        data_unseen = pd.DataFrame([x], columns=cols_m7)
        prediction = model_7.predict(data_unseen)
    else:
        fgas = request.form.get('FGas')
        temp = request.form.get('Temp')
        if fgas == "":
            return render_template('index.html', pred=f"FGas no puede estar vacío")
        if temp == "":
            return render_template('index.html', pred=f"Temperatura no puede estar vacío")

        x = np.array([fgas, temp])
        data_unseen = pd.DataFrame([x], columns=cols_m8)
        prediction = model_8.predict(data_unseen)

    return render_template('index.html', pred=f"El número de muertes esperadas es {prediction[0]}")
    # return render_template('index.html', pred=model_selected)


if __name__ == "__main__":
    app.run(debug=True)
