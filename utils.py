import pickle

# LOADING THE PICKLE FILES


tokenizer=pickle.load(open("MODELS/tokenizer_vector_classifier.pkl",'rb'))
model=pickle.load(open("MODELS/model_classifier.pkl",'rb'))
def make_pred(email_text):
    tokenized_email=tokenizer.transform([email_text])
    # prediction=model.predict(tokenized_email)[0]
    prediction=model.predict(tokenized_email)
    prediction=1 if prediction==1 else-1
    return prediction