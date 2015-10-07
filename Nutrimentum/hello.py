from flask import Flask,request,redirect,render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
import random
app = Flask(__name__)


protiens=['meat','fish','eggs','dairy products','nuts','seeds','legumes']
carbohydrates=['fruits','legumes','whole grains','white rice','white bread']
fibre=['fruits','whole grains','vegetables']
fat=['butter','red meat','whole milk','cheese']
iron=['lean meats','legumes','poultry','fish','beans','fish']
zinc=['beef','pork','lamb','dark chicken meat','nuts','yeast','legumes','whole grains']
calcium=['milk','tofu','almonds','ornage juice']
vitamina=['cheese','fish oil,carrots', 'broccoli','spinach','pumpkins','milk']
vitaminb=['avocados','bananas','beans','meat','nuts','poultry','wholegrains']
vitaminc=['orange','straberries','red pepper','broccoli']

nutrients = {
    "PROTEINS" : protiens,
    "CARBOHYDRATES" : carbohydrates,
    "FIBRE" : fibre,
    "FAT" : fat,
    "IRON" : iron,
    "ZINC" : zinc,
    "CALCIUM" : calcium,
    "VITAMIN A" : vitamina,
    "VITAMIN B" : vitaminb,
    "VITAMIN C" : vitaminc
}


"""Updated the array of nutrient_name above"""


@app.route("/",methods=['GET','POST'])
def hello():
    return "HI!"

@app.route("/r/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

#     message=request.form['Body']
#     if(message== "Hi"):
#         message="Welcome to Nutrimentum"
#     if (message != "PROTEINS" or message != "CARBOHYDRATES" or message != "FAT " or message != "FIBRE" or message != "IRON" or message != "IRON" or message != "CALCIUM" or message != "VITAMIN A" or message != "VITAMIN B" or message != "VITAMIN C"):
#         message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"
#     if(message== "PROTEINS"):
#         value= random.sample(protiens,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "CARBOHYDRATES"):
#         value= random.sample(carbohydrates,3)
#         answer=""
#         for i in value:
#             answer=answer+i+ ""
#         message=answer
#     if(message== "FIBRE"):
#         value= random.sample(fibre,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "FAT"):
#         value= random.sample(fat,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "IRON"):
#         value= random.sample(iron,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "ZINC"):
#         value= random.sample(zinc,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "CALCIUM"):
#         value= random.sample(calcium,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "VITAMIN A"):
#         value= random.sample(vitamina,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "VITAMIN B"):
#         value= random.sample(vitaminb,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     if(message== "VITAMIN C"):
#         value= random.sample(vitaminc,3)
#         answer=""
#         for i in value:
#             answer=answer+i + ""
#         message=answer
#     # else:
#     #     message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"
# =======
    print("Hello")
    message=request.form['Body'].upper()
    message = response_string(message)

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

def response_string(message):
    if(message== "HI"):
        message="Hello"
    if (message not in nutrients):
        message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"
    elif(message in nutrients):
        nutrient = nutrients[message]
        value = random.sample(nutrient, 3)
        answer = ""
        for i in value:
            if (answer == ""):
                answer = i
            else:
                answer = answer + " " + i
        message = answer
    # else:
        # message="Please enter Nutrients from FAT,CALCIUM,VITAMIN A/B/C,ZINC,FIBRE,FAT,CARBOHYDRATES,PROTEINS one at a time to receive appropiate food items"

    return message



if __name__ == "__main__":
    app.run(debug=True)
