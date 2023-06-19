from flask import Flask, jsonify, render_template, request

from project_app.utils import Fraud

# Creating instance here
app = Flask(__name__)

# Home API
@app.route("/")
def hello_flask():
    print("Welcome to Diabetics Prediction System")
    return render_template("index1.html")

@app.route("/predict_charges", methods = ["POST", "GET"])
def get_prediction():
    if request.method == "GET":
        print("We are in a GET Method")

        WeekOfMonth = request.args.get('WeekOfMonth')
        AccidentArea = request.args.get('AccidentArea')
        WeekOfMonthClaimed = request.args.get('WeekOfMonthClaimed')
        Sex = request.args.get('Sex')
        MaritalStatus = request.args.get('MaritalStatus')
        Age = request.args.get('Age')
        Fault = request.args.get('Fault')
        VehicleCategory = request.args.get('VehicleCategory')
        VehiclePrice = request.args.get('VehiclePrice')
        PolicyNumber = request.args.get('PolicyNumber')
        RepNumber = request.args.get('RepNumber')
        Deductible = request.args.get('Deductible')
        DriverRating = request.args.get('DriverRating')
        Days_Policy_Accident = request.args.get('Days_Policy_Accident')
        Days_Policy_Claim = request.args.get('Days_Policy_Claim')
        PastNumberOfClaims = request.args.get('PastNumberOfClaims')
        AgeOfVehicle = request.args.get('AgeOfVehicle')
        AgeOfPolicyHolder = request.args.get('AgeOfPolicyHolder')
        PoliceReportFiled = request.args.get('PoliceReportFiled')
        WitnessPresent = request.args.get('WitnessPresent')
        AgentType = request.args.get('AgentType')
        NumberOfSuppliments = request.args.get('NumberOfSuppliments')
        AddressChange_Claim = request.args.get('AddressChange_Claim')
        NumberOfCars = request.args.get('NumberOfCars')
        Year = request.args.get('Year')
        Month_inp = str(request.args.get('Month_inp'))
        DayOfWeek_inp = str(request.args.get('DayOfWeek_inp'))
        Make_inp = str(request.args.get('Make_inp'))
        DayOfWeekClaimed_inp = str(request.args.get('DayOfWeekClaimed_inp'))
        MonthClaimed_inp = str(request.args.get('MonthClaimed_inp'))
        # PolicyType = str(request.args.get('PolicyType_inp'))
        # BasePolicy = str(request.args.get('BasePolicy_inp'))

        # PolicyType_inp = PolicyType_inp1.replace(" - ",'_')
    print(WeekOfMonth,AccidentArea,WeekOfMonthClaimed,Sex,MaritalStatus,Age,Fault,VehicleCategory,VehiclePrice,
                 PolicyNumber,RepNumber,Deductible,DriverRating,Days_Policy_Accident,Days_Policy_Claim,PastNumberOfClaims,
                 AgeOfVehicle,AgeOfPolicyHolder,PoliceReportFiled,WitnessPresent,AgentType,NumberOfSuppliments,AddressChange_Claim,
                 NumberOfCars,Year,Month_inp,DayOfWeek_inp,Make_inp,DayOfWeekClaimed_inp,MonthClaimed_inp)

    fraud =  Fraud(WeekOfMonth,AccidentArea,WeekOfMonthClaimed,Sex,MaritalStatus,Age,Fault,VehicleCategory,VehiclePrice,
                 PolicyNumber,RepNumber,Deductible,DriverRating,Days_Policy_Accident,Days_Policy_Claim,PastNumberOfClaims,
                 AgeOfVehicle,AgeOfPolicyHolder,PoliceReportFiled,WitnessPresent,AgentType,NumberOfSuppliments,AddressChange_Claim,
                 NumberOfCars,Year,Month_inp,DayOfWeek_inp,Make_inp,DayOfWeekClaimed_inp,MonthClaimed_inp)

    prediction = fraud.get_prediction()

    return render_template("index1.html", prediction = prediction)
    # print("prediction", prediction)
    # return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."}) #postman test

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters