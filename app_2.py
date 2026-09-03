from flask import Flask,render_template,request,jsonify
from utils import make_pred
import pickle
app=Flask(__name__)
# LOADING THE PICKLE FILES

tokenizer=pickle.load(open("MODELS/tokenizer_vector_classifier.pkl",'rb'))
model=pickle.load(open("MODELS/model_classifier.pkl",'rb'))
@app.route('/')
def home():
    return render_template('REN_html.html')
'''MAKING A APP ROUTE FOR PREDICTION'''
@app.route('/predict',methods=['POST'])
def predict():
    email_text=request.form.get('Email-content')
    prediction=make_pred(email_text)
    
    return render_template('REN_html.html',prediction=prediction,email_text=email_text)
'''MAKING OF AN API KEY'''
@app.route('/api/predict',methods=['POST'])
def predicit_api():
    data=request.get_json(force=True)
    email=data['Email-content']
    prediction=make_pred(email)
    return jsonify({'prediction':prediction,'email':email})
@app.route('/test')
def test():
    return "TEST ROUTE WORKING"

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)  
'''WE CAN CALL AN API USING TERMINAL OR AN EXTENSION CALLED AS THUNDER CLIENT INSOMINIA POSTMAN'''