from flask import Flask,render_template,request
# CREATING INSTANCE OF THE FLASK
'''name is refering to the current file name'''
app=Flask(__name__)
# REGESTIERING A ROUTE BY USING A DECORATOR
'''NOW THE SLASH DEFINES THE ROUTE HOME PAGE OF A WEB '''
'''WE ARE GOING TO GIVE IT METHODS AS IT TAKE TWO METHODS AS GET AND POST'''
@app.route('/',methods=['GET','POST'])

def home():
    '''USING RENDER_TEMPLATE FOR ACCESSING HTML FILE'''
    # return render_template('REN_html.html')
    # CREATING A TEXT
    text=""
    # USING REQUEST >METHOD FOR TO SEEK POST OR GET PART FROM HTML
    if request.method=='POST':
        text=request.form.get('Email-content')
    return render_template('REN_html.html',text=text)


''''WE WILL WE DISPLAYING IT BY USING app.run'''
if __name__=='__main__':
    '''IF DEBUG IS NOT TRUE THAN THE PAGE WILL NOT BE UPDATED'''
    app.run(host='0.0.0.0',debug=True)
    


