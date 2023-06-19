import pandas as pd
import numpy as np
import pickle
import json
import warnings
warnings.filterwarnings('ignore')
import os
import config

class Fraud():
    def __init__(self,WeekOfMonth,AccidentArea,WeekOfMonthClaimed,Sex,MaritalStatus,Age,Fault,VehicleCategory,VehiclePrice,
                 PolicyNumber,RepNumber,Deductible,DriverRating,Days_Policy_Accident,Days_Policy_Claim,PastNumberOfClaims,
                 AgeOfVehicle,AgeOfPolicyHolder,PoliceReportFiled,WitnessPresent,AgentType,NumberOfSuppliments,AddressChange_Claim,
                 NumberOfCars,Year,Month_inp,DayOfWeek_inp,Make_inp,DayOfWeekClaimed_inp,MonthClaimed_inp):
        
        self.WeekOfMonth = WeekOfMonth
        self.AccidentArea = AccidentArea
        self.WeekOfMonthClaimed = WeekOfMonthClaimed
        self.Sex = Sex
        self.MaritalStatus = MaritalStatus
        self.Age = Age
        self.Fault = Fault
        self.VehicleCategory = VehicleCategory
        self.VehiclePrice = VehiclePrice
        self.PolicyNumber = PolicyNumber
        self.RepNumber = RepNumber
        self.Deductible = Deductible
        self.DriverRating = DriverRating
        self.Days_Policy_Accident = Days_Policy_Accident
        self.Days_Policy_Claim = Days_Policy_Claim
        self.PastNumberOfClaims = PastNumberOfClaims
        self.AgeOfVehicle = AgeOfVehicle
        self.AgeOfPolicyHolder = AgeOfPolicyHolder
        self.PoliceReportFiled = PoliceReportFiled
        self.WitnessPresent = WitnessPresent
        self.AgentType = AgentType
        self.NumberOfSuppliments = NumberOfSuppliments
        self.AddressChange_Claim = AddressChange_Claim
        self.NumberOfCars = NumberOfCars
        self.Year = Year
        self.Month_inp = Month_inp
        self.DayOfWeek_inp = DayOfWeek_inp
        self.Make_inp = Make_inp
        self.DayOfWeekClaimed_inp = DayOfWeekClaimed_inp
        self.MonthClaimed_inp = MonthClaimed_inp
        # self.PolicyType = PolicyType_inp
        # self.BasePolicy = BasePolicy_inp
        
        # Find the index of this column -->
        self.Month_col = 'Month_'+ self.Month_inp
        self.DayOfWeek_col = 'DayOfWeek_'+ self.DayOfWeek_inp
        self.Make_col = 'Make_' + self.Make_inp
        self.DayOfWeekClaimed_col = 'DayOfWeekClaimed_'+ self.DayOfWeekClaimed_inp
        self.MonthClaimed_col = 'MonthClaimed_'+ self.MonthClaimed_inp
        # self.PolicyType_col = 'PolicyType_' + self.PolicyType_inp
        # self.BasePolicy_col = 'BasePolicy_' + self.BasePolicy_inp

    def load_models(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.dt_prunning_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_prediction(self):
        self.load_models()

        test_array = np.zeros(len(self.json_data['columns']), dtype = int)
        # (test_array)

        self.Month_index = list(self.json_data['columns']).index(self.Month_col)
        self.DayOfWeek_index = list(self.json_data['columns']).index(self.DayOfWeek_col)
        self.Make_index = list(self.json_data['columns']).index(self.Make_col)
        self.DayOfWeekClaimed_index = list(self.json_data['columns']).index(self.DayOfWeekClaimed_col)
        self.MonthClaimed_index = list(self.json_data['columns']).index(self.MonthClaimed_col)
        # self.PolicyType_index = list(self.json_data['columns']).index(self.PolicyType_col)
        # self.BasePolicy_index = list(self.json_data['columns']).index(self.BasePolicy_col)


        test_array[0] = self.WeekOfMonth
        test_array[1] = self.json_data['AccidentArea'][self.AccidentArea]
        test_array[2] = self.WeekOfMonthClaimed
        test_array[3] = self.json_data['Sex'][self.Sex]
        test_array[4] = self.json_data['MaritalStatus'][self.MaritalStatus]
        test_array[5] = self.Age
        test_array[6] = self.json_data['Fault'][self.Fault]
        # test_array[7] = self.json_data['PolicyType'][self.PolicyType]
        test_array[8] = self.json_data['VehicleCategory'][self.VehicleCategory]
        test_array[9] = self.json_data['VehiclePrice'][self.VehiclePrice]
        test_array[10] = self.PolicyNumber
        test_array[11] = self.RepNumber
        test_array[12] = self.Deductible
        test_array[13] = self.DriverRating
        test_array[14] = self.json_data['Days_Policy_Accident'][self.Days_Policy_Accident]
        test_array[15] = self.json_data['Days_Policy_Claim'][self.Days_Policy_Claim]
        test_array[16] = self.json_data['PastNumberOfClaims'][self.PastNumberOfClaims]
        test_array[17] = self.json_data['AgeOfVehicle'][self.AgeOfVehicle]
        test_array[18] = self.json_data['AgeOfPolicyHolder'][self.AgeOfPolicyHolder]
        test_array[19] = self.json_data['PoliceReportFiled'][self.PoliceReportFiled]
        test_array[20] = self.json_data['WitnessPresent'][self.WitnessPresent]
        test_array[21] = self.json_data['AgentType'][self.AgentType]
        test_array[22] = self.json_data['NumberOfSuppliments'][self.NumberOfSuppliments]
        test_array[23] = self.json_data['AddressChange_Claim'][self.AddressChange_Claim]
        test_array[24] = self.json_data['NumberOfCars'][self.NumberOfCars]
        test_array[25] = self.Year
        # test_array[26]= self.json_data['BasePolicy'][self.BasePolicy]


        test_array[self.Month_index] = 1
        test_array[self.DayOfWeek_index] = 1
        test_array[self.Make_index] = 1
        test_array[self.DayOfWeekClaimed_index] = 1
        test_array[self.MonthClaimed_index] = 1
        # test_array[PolicyType_index] = 1
        # test_array[BasePolicy_index] = 1
        print(test_array)
        print(len(test_array))

        result = self.dt_prunning_model.predict([test_array])
        if result==1:
            prediction = "Fraud Insurance Claim Detected"
        else:
            prediction = "No Fraud found"

        return prediction

# if __name__ == "__main__":
#     Glucose = 141.000000
#     BloodPressure = 72.375171
#     SkinThickness = 29.153420
#     Insulin = 155.548223
#     BMI = 42.400000
#     DiabetesPedigreeFunction = 0.205000
#     Age = 29.000000

#     Diabetes =  Diabetics(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
#     prediction = Heart.get_prediction()
#     print("prediction", prediction)