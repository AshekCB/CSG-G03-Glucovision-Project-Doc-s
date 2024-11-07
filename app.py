#Loading the needed libraries and Frameworks
'''
Flask--> MicroFrameWork
render_templte--> To Navigate from 1 page to another page
request --> to handle HTTP Requests from forms 
redirect-->to redirect the page from 1 to another
url_for('function_name')--> for creating the path for a page.
'''
from flask import Flask,render_template,request,redirect,url_for
import bmi_caluclator 
#loading the python function to caluclate bmi
import age_caluclator
#loading the python function to caluclate age
import databases as db
#loading the db connection for booking an appointments
from checking_booking import check_appointment #to check an appointments

import models as model#loading the ML Model

#Web/App Name
app=Flask(__name__)

#Home Page
@app.route("/",methods=["POST","GET"])
def home():
    return render_template("home.html")


#About Page
@app.route("/about",methods=["POST","GET"])
def about():
    return render_template("about.html")


#Bmi Caluclator Page
@app.route("/bmi",methods=["POST","GET"])
def bmi():
    if request.method=="POST":
        h=request.form['height']
        w=request.form['weight']
        result=bmi_caluclator.caluclate(float(w),float(h))
        return render_template("bmi_cal.html",result=float(result))
    else:
        return render_template("bmi_cal.html",result="")



#Age Caluclator Page
@app.route("/age",methods=["POST","GET"])
def age():
    if request.method=="POST":
        by=request.form['birthyear']
        result=age_caluclator.caluclator(int(by))
        return render_template("age.html",result=result)
    else:
        return render_template("age.html",result="")


#Appointments Booking Page
@app.route("/appointments",methods=["POST","GET"])
def appointments():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        doctor = request.form['doctor']
        desc=request.form['description']
        
        #Calling a method that initiates the database Connection and
        #  to insert the data into it.

        result=db.book_appointment(name,email,phone,date,time,doctor,desc)
        return render_template("appointments.html",result=result)
    else:
        return render_template("appointments.html")


#Booking CheckUp Page-->External Page(it is only available in Booking Page)

@app.route("/checkings",methods=["POST","GET"])
def checkings():
    if request.method=="POST":
        bid=request.form['booking_id']
        #calling the external function to check an appointment status using Booking id in DB 
        result=check_appointment(str(bid))
        return render_template("bookings.html",result=result)
    else:
        return render_template("bookings.html")


#Prediction Page

@app.route("/predictions",methods=["POST","GET"])
def predictions():
    if request.method=="POST":
        preg=request.form['pregnancies']
        gluco=request.form['glucose']
        bp=request.form['bloodPressure']
        sthick=request.form['skinThickness']
        ins=request.form['insulin']
        bmi=request.form['bmi']
        pedgree=request.form['pedigreeFunction']
        age=request.form['age']
        # using instance of model predicting the data
        result=model.predictor(int(preg),float(gluco),int(bp),float(sthick),int(ins),float(bmi),float(pedgree),int(age))
        #redirecting the result to result page
        return redirect(url_for('result', result=result))
    else:
        return render_template("predictions.html")

#Result page
@app.route("/result")
def result():
    #geting the args from predictions page through Http Request
    result = request.args.get('result', type=int)
    return render_template("result.html", result=result)


#Guard page 
@app.route("/guard",methods=["POST","GET"])
def guard():
    if request.method=="POST":
        return render_template("guard.html")
    else:
        return render_template("guard.html") 
       



#main method 
if __name__=="__main__":
    app.run(debug=True)
    #debug flag=True -- > It Shows the errors
