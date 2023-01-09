# prediction function
import pickle
import numpy as np
from flask import Flask,render_template,request
import re
import requests
import requests_html
model=pickle.load(open('model.pkl',"rb"))
app=Flask(__name__)
@app.route('/result')
def result():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict_salary():
    experience=float(request.form.get('Years of Experience'))
    result=model.predict(np.array([experience]).reshape(1,1))
    r="the predicted value of the salary for you is "+str(result)
    return str(r)


if __name__=="__main__":
    app.run()