from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)

@app.route("/")
def hello():


    return render_template('in.html')

@app.route("/sendsms/")
def send_page():
    return render_template('send.html')

@app.route("/t/",methods=['GET','POST'])
def send():
    number=request.form['number']
    message=request.form['message']
    account_sid = "AC028a28db5c78b421cb6f2d7ce621c58b"
    auth_token = "0d3960f5466469449b228781b54ea595"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=number, from_="+16466933151",
                                     body=message)

    ackk= "Your message has been sent to " + number + " !!!!"
    return render_template('response.html',mess=ackk)


if __name__ == "__main__":
    app.run(debug=True)
