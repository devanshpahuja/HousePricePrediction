from flask import Flask, render_template, url_for, request
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods=['POST'])
def home():
    area= int(request.form['area'])
    bhk= int(request.form['bhk'])
    resale= int(request.form['resale'])
    Staff_number=int(request.form['Staff_number'])
    society= int(request.form['society'])
    intercom= int(request.form['intercom'])
    atm= int(request.form['atm'])
    security= int(request.form['security'])
    backup= int(request.form['backup'])
    parking= int(request.form['parking'])
    Staffquarter= int(request.form['Staffquarter'])
    cafe= int(request.form['cafe'])
    multipurposeroom= int(request.form['MPR'])
    hospital= int(request.form['hospital'])
    machine= int(request.form['Machine'])
    wifi= int(request.form['Wifi'])
    Vastu_complaint= int(request.form['Vastu_complaint'])
    furnished= int(request.form['fusnished'])
    mall=school=golf=0
    gas=AC=1
    
    
    if society == 1:
        gym=pool=garden=track=mall=harvesting=games=sports=lift=clubhouse=ground= 1
    else :
        gym=pool=garden=track=mall=harvesting=games=sports=clubhouse=ground=0
    
    if furnished== 1 :
        bed=microwave=TV=DT=sofa=wardrobe=fridge=1
    else:
         bed=microwave=TV=DT=sofa=wardrobe=fridge=0
            
    var = np.array([area,bhk,resale,Staff_number, gym, pool, garden, track,harvesting,games, mall,intercom, sports, atm,clubhouse,school,security, backup, parking,Staffquarter,cafe,multipurposeroom, hospital, machine,gas, AC, wifi, ground, lift, bed,Vastu_complaint,microwave,golf,TV,DT,sofa, wardrobe, fridge ])
    var= var.reshape(1,-1)
    prediction= model.predict(var)
            
    return render_template("prediction.html", prediction= int(prediction.round(3)))



@app.errorhandler(500)
def errorpage(e):
    return render_template("500.html")

@app.errorhandler(404)
def errorpage(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=False)