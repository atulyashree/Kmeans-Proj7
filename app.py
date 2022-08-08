import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('proj7.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    genre = int(request.args.get('genre'))
    age = int(request.args.get('age'))
    annual_income = int(request.args.get('annual_income'))
    spending_score = int(request.args.get('spending_score'))
    prediction = classifier.predict([[genre,age,annual_income,spending_score]])
    
    print("K-means prediction",prediction)
    if prediction==[0]:
      print("cluster 0")
    elif prediction==[1]:
      print("cluster 1")
    else:
      print("cluster 2")

        
    return render_template('index.html', prediction_text='k-means cluster = {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug =True)
