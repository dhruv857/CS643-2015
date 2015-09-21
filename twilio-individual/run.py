from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():


    return render_template('in.html')

@app.route("/r/",methods=['GET','POST'])
def hello_monkey():


    resp = twilio.twiml.Response()
    resp.message("Hello!!! This is dhruv testing")
    return str(resp)

@app.route("/sendsms/")
def send_page():
    return render_template('send.html')

@app.route("/t/",methods=['GET','POST'])
def send():
    number=request.form['number']
    message=request.form['message']
    account_sid = "***********************************"
    auth_token = "**********************************"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=number, from_="+16466933151",
                                     body=message)

    ackk= "Your message has been sent to " + number + " !!!!"
    return render_template('response.html',mess=ackk)


if __name__ == "__main__":
    app.run(debug=True)
