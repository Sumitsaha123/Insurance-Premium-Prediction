from flask import Flask, render_template,request,flash
import pickle as pkl
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
model  = pkl.load(open('RanodmForest_Regression_model.pkl','rb'))
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoker = request.form.get('smoker')
        region = request.form.get('region')

        if sex == 'Male':
            sex = 1
        else:
            sex = 0

        if smoker == 'Yes':
            smoker = 1
        else:
            smoker = 0 

        if region =='southwest':
            region_northwest = 0
            region_southwest = 1
            region_southeast = 0
        elif region == 'northwest':
            region_northwest = 1
            region_southwest = 0
            region_southeast = 0
        elif region == 'southeast':
            region_northwest = 0
            region_southwest = 0
            region_southeast = 1
        else:
            region_northwest = 0
            region_southwest = 0
            region_southeast = 0

        prediction = model.predict([[age,sex,bmi,children,smoker,region_northwest,region_southwest,region_southeast]])
        output=round(prediction[0],2)
        flash("Your Predicted Insurance Ammount will be: "+str(output))
        
    return render_template('index.html')
               
if __name__ == "__main__":
    app.run()

