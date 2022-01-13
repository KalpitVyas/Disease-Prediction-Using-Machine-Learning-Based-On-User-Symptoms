from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

app = Flask(__name__)

#List of Symptoms, List_of_Disease and CSV File Code below (Testing & Training CSV files)
#TODO: List of symptoms need to be revisted just to be sure whether we have imported the correct one or not.
list_of_symptoms = ["itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering","chills","joint_pain","stomach_pain","acidity",
                    "ulcers_on_tongue","muscle_wasting","vomiting","burning_micturition","spotting_ urination","fatigue","weight_gain","anxiety",
                    "cold_hands_and_feets","mood_swings","weight_loss","restlessness","lethargy","patches_in_throat","irregular_sugar_level",
                    "cough","high_fever","sunken_eyes","breathlessness","sweating","dehydration","indigestion","headache","yellowish_skin",
                    "dark_urine","nausea","loss_of_appetite","pain_behind_the_eyes","back_pain","constipation","abdominal_pain","diarrhoea",
                    "mild_fever","yellow_urine","yellowing_of_eyes","acute_liver_failure","fluid_overload","swelling_of_stomach","swelled_lymph_nodes",
                    "malaise","blurred_and_distorted_vision","phlegm","throat_irritation","redness_of_eyes","sinus_pressure","runny_nose","congestion",
                    "chest_pain","weakness_in_limbs","fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool",
                    "irritation_in_anus","neck_pain","dizziness","cramps","bruising","obesity","swollen_legs","swollen_blood_vessels",
                    "puffy_face_and_eyes","enlarged_thyroid","brittle_nails","swollen_extremeties","excessive_hunger","extra_marital_contacts",
                    "drying_and_tingling_lips","slurred_speech","knee_pain","hip_joint_pain","muscle_weakness","stiff_neck","swelling_joints",
                    "movement_stiffness","spinning_movements","loss_of_balance","unsteadiness","weakness_of_one_body_side","loss_of_smell",
                    "bladder_discomfort","foul_smell_of urine","continuous_feel_of_urine","passage_of_gases","internal_itching","toxic_look_(typhos)",
                    "depression","irritability","muscle_pain","altered_sensorium","red_spots_over_body","belly_pain","abnormal_menstruation",
                    "dischromic _patches","watering_from_eyes","increased_appetite","polyuria","family_history","mucoid_sputum","rusty_sputum",
                    "lack_of_concentration","visual_disturbances","receiving_blood_transfusion","receiving_unsterile_injections","coma","stomach_bleeding",
                    "distention_of_abdomen","history_of_alcohol_consumption","fluid_overload","blood_in_sputum","prominent_veins_on_calf",
                    "palpitations","painful_walking","pus_filled_pimples","blackheads","scurring","skin_peeling","silver_like_dusting",
                    "small_dents_in_nails","inflammatory_nails","blister","red_sore_around_nose","yellow_crust_ooze"]

list_of_disease = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

List_Prediction=[] #Empty List L2
for x in range(0,len(list_of_symptoms)):
    List_Prediction.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")
df.replace({'prognosis':{'Jaundice':0,'Malaria':1,'Chickenpox':2,'Dengue':3,'Typhoid':4,
'Common Cold':5,'Tuberculosis':6,'Fungal Infection':7,'Diabetes':8, 'Paralysis' : 9, 'Migraine':10, 'AIDS':11 ,
'Hypertension': 12, 'Pneumonia':13, 'Vericose Veins': 14, 'Allergy': 15, 'Vertigo': 16, 'Viral Fever': 17}},inplace=True)

#print(df)
#print(df.head())

X= df[list_of_symptoms]
y = df[["prognosis"]]
np.ravel(y)
#print("Something",y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Jaundice':0,'Malaria':1,'Chickenpox':2,'Dengue':3,'Typhoid':4,
'Common Cold':5,'Tuberculosis':6,'Fungal Infection':7,'Diabetes':8, 'Paralysis' : 9, 'Migraine':10, 'AIDS':11 ,
                         'Hypertension': 12, 'Pneumonia':13, 'Vericose Veins': 14, 'Allergy': 15, 'Vertigo': 16, 'Viral Fever': 17}},inplace=True)
X_test= tr[list_of_symptoms]
y_test = tr[["prognosis"]]
np.ravel(y_test)
@app.route("/") #This will be displayed at first
def Temp():
    #temp = ['Addition', 'Subtraction', 'Multiplication', 'Division']
    #The Following Code will display the disease at home1.html and will wait for the user input.
    disease = ['Jaundice', 'Malaria', 'Chickenpox', 'Dengue', 'Typhoid', 'Common Cold', 'Tuberculosis',
               'Fungal Infection', 'Diabetes','Paralysis',
               'Migraine', 'AIDS', 'Hypertension', 'Pneumonia', 'Vericose Veins','Allergy', 'Vertigo', 'Viral Fever']
    return render_template("home1.html",Temp = disease) #home1.html Displayed with Disease List #DISEASE

@app.route("/", methods=['POST','GET'])
def home():
    GetDisease = request.form.get('DiseaseName') #Input Given from home.html will be passed here(accepting the Disease Name from home1.html)
    if GetDisease == "Jaundice":   #Checking the condition for "Jaundice" disease.
        #Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','abdominal_pain','change_in_skin_color','chills','dark_colored_urine','fever','itchiness','fatigue','weight_loss']
        Sentence = "Some Discription about the Disease" #Description
        return render_template("home.html", Symptoms = TempDisease, PutDisease1 = GetDisease) #Will Display the Symptoms for that particular disease
#HOME.HTML -> Symptoms
    elif GetDisease == "Malaria":  #Checking the condition for "Malaria" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','nausea','sweats','shivering','faster_heart_Rate','fatigue','headache','diarrhoea','fever','chills','body_aches','abdominal_pain']
        Sentence = "Symptoms of malaria can develop as quickly as 7 days after you're bitten by an infected mosquito."
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease, Sentence =  Sentence)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Chickenpox":#Checking the condition for "Chickenpox" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['red_spots_over_body', 'loss_of_appetite','lethargy','malaise','swelled_lymph_nodes','skin_rash','fatigue','itchiness','headache','fever','sore_throat']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Dengue":#Checking the condition for "Dengue" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','malaise','nausea','red_spots_over_body','loss_of_appetite','skin_rash','fatigue','pain_back_of_the_eyes','headache','fever','joint_pain','chills','abdominal_pain']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Typhoid":#Checking the condition for "Typhoid" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','muscle_weekness','weakness','nausea','skin_rash','stomach_pain','fatigue','headache','constipation','diarrhoea','fever','chills','cough','abdominal_pain']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Common Cold":#Checking the condition for "Common Cold" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['redness_of_eyes','malaise','swelled_lymph_nodes','fatigue','headache','fever','chills','watery eyes','cough','congestion','sneezing','stuffy_nose','running_nose','sore_throat']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Tuberculosis":#Checking the condition for "Tuberculosis" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['weakness','loss_of_appetite','weight_loss','sweats','fever','chills','cough','chest_pain','cough_in_Blood']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Fungal Infection":#Checking the condition for "Fungal Infection" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['weakness','redness_of_eyes','peeling skin','soft_skin','burning_ sensation','red_skin','loss_of_appetite','weight_loss','sweats','itchiness','fever','chills','cough','chest_pain']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Diabetes":#Checking the condition for "Diabetes" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['Feeling_Thirsty','Time_to_heal_injuries','Faint','weakness','weight_loss']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Paralysis":#Checking the condition for "Paralysis" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','difficulty_swallowing','loss_of_balance','loss_of_vission','Faint','anxiousness','weakness','nausea','fatigue','headache','stiff_neck']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Migraine":#Checking the condition for "Migraine" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['Urinating_often','moodiness','Irritability','anxiousness','Felling_hungry','Feeling_Thirsty','loss_of_appetite','constipation']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "AIDS":#Checking the condition for "AIDS" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['weakness','sweats','mouth_ulcers','swelled_lymph_nodes','skin_rash','fever','chills','sore_throat','body_pain']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Hypertension":#Checking the condition for "Hypertension" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['blood_in_urine','irregular_heartbeat','stiff_neck','Nose_bleed','breathing_problem','fatigue','headache','chest_pain']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Pneumonia":#Checking the condition for "Pneumonia" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','breathing_problem','Less_then_normal_temperature','nausea','shivering','fatigue','diarrhoea','cough','chest_pain','cough_phelgm']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Vericose Veins": #Checking the condition for "Vericose Veins" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['muscle_cramping','itching_vein','Irritability','pain_in_legs']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Allergy": #Checking the condition for "Allergy" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['feeling_sick','rashes','vomiting','Swollen_lips','breathing_problem','redness_of_eyes','nausea','itchiness','watery eyes','chest_tightness','cough','stuffy_nose']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Vertigo": #Checking the condition for "Vertigo" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['vomiting','dizziness','loss_of_balance','nausea']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

    elif GetDisease == "Viral Fever": #Checking the condition for "Viral Fever" disease.
        # Following List will be used to display the symptoms for the disease choosen.
        TempDisease = ['dehydration','muscle_pain','weakness','loss_of_appetite','sweats','headache','chills']
        return render_template("home.html", Symptoms=TempDisease,PutDisease1=GetDisease)  # Will Display the Symptoms for that particular disease

@app.route("/DiseasePredict", methods = ['POST', 'GET'])
def Disease():
    Get_Disease = request.form.getlist('Symptoms') #Symptoms are beign accepted here, this list of symptoms will be given as input to the Algorightm
    #Get_Disease is the common method. It will accept the symptoms selected for that disease
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X, np.ravel(y))
    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    for k in range(0, len(list_of_symptoms)):
        for z in Get_Disease:
            if (z == list_of_symptoms[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(list_of_disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        ResultSymptoms = []
        ResultSymptoms.append(list_of_disease[a])
        #t3.delete("1.0", END)
        #t3.insert(END, disease[a])
    else:
        ResultSymptoms = "Not Found"
        #t3.delete("1.0", END)
        #t3.insert(END, "Not Found")

        Get_Disease_String = Get_Disease
    return render_template("DiseasePredict.html", SelectedSymptoms = Get_Disease_String, DiseasePredicted = ResultSymptoms) #Will Display the Disease is present or not with the symptoms selected

if __name__ == '__main__':
    app.run(debug=True)

#List of Changes
"""
1. To add a for loop in the HTML code so that the Flask can display all the symptoms 
2. The above code is for Disease Search Symptoms Made back 5 months ago the changes are to convert it with Symptoms Accept
3. The Dataset looks fine, so need to focus more on Algorithms.
"""
