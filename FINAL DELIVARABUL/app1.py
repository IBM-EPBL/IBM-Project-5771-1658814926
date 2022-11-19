from flask import Flask,render_template,request
import joblib
from flask import jsonify

app = Flask(__name__)
model = joblib.load('Rainfall prediction (1)')
@app.route('/',methods=['GET'])
def Home():
    return render_template('PRAVEEN.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Mintemp= int(request.form['MinTemp'])
        Maxtemp=int(request.form['MaxTemp'])
        Rainfall=int(request.form['Rainfall'])
        WindGustSpeed=int(request.form['WindGustSpeed'])
        WindSpeed9am=int(request.form['WindDir9am'])
        WindSpeed3pm=int(request.form['WindSpeed3pm'])
        Humidity9am=int(request.form['Humidity9am'])
        Humidity3pm=int(request.form['Humidity3pm'])
        Pressure9am=int(request.form['Pressure9am'])
        Pressure3pm=int(request.form['Pressure3pm'])
        Temp9am=int(request.form['Temp9am'])
        Temp3pm=int(request.form['Temp3pm'])
        RainToday_No=int(request.form['RainToday_No'])
        RainToday_Yes=int(request.form['RainToday_Yes'])

        prediction=model.predict([[Mintemp,Maxtemp, Rainfall,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm,RainToday_No,RainToday_Yes]])
        predictiontext=prediction
        if prediction==True:
            return render_template('PRAVEEN.html',prediction_text="Chance")
        else:
            return render_template('PRAVEEN.html',prediction_text="No Chance")
    else:
        return render_template('PRAVEEEN.html')

        
        if __name__=="main":
            app.run(debug=True)
