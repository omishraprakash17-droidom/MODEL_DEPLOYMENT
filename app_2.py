from flask import Flask,render_template,request
from sklearn.ensemble import RandomForestClassifier
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
    tokenized_email=tokenizer.transform([email_text])
    # prediction=model.predict(tokenized_email)[0]
    prediction=model.predict(tokenized_email)
    prediction=1 if prediction==1 else-1
    
    return render_template('REN_html.html',prediction=prediction,email_text=email_text)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)  