# Including all the necessary libraries
import csv
import numpy as np
import pandas as pd
from flask import Flask, render_template as rt, request
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
app = Flask(__name__)

# List of Symptoms will be given as Features or Defining the features from the dataset
list_of_Symptoms = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering'
    ,'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting',
    'burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets',
    'mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level',
    'cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
    'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
    'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
    'belly_pain',
    'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
    'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
    'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
    'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
    'red_sore_around_nose',
    'yellow_crust_ooze']
#print(len(list_of_Symptoms))
# Defining the Target Values
list_of_disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                   'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
                   ' Migraine', 'Cervical spondylosis',
                   'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                   'hepatitis A',
                   'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
                   'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                   'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                   'Osteoarthristis',
                   'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                   'Psoriasis',
                   'Impetigo']
#print(len(list_of_disease))
# Creating an empty list "list_temp" and storing all the values of list_of_symptoms in the the following list and appending all the values to 0.
list_Temp = []
for x in range(0, len(list_of_Symptoms)):
    list_Temp.append(0)

df = pd.read_csv("Training.csv")  # Reading the Training Dataset using Pandas Dataframe
# Here, Replacing the Target Values with their Respective index values
df.replace(
    {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                   'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                   'Hypertension ': 10,
                   'Migraine': 11, 'Cervical spondylosis': 12,
                   'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                   'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                   'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                   'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                   'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                   'Varicose veins': 30, 'Hypothyroidism': 31,
                   'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                   '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                   'Psoriasis': 39,
                   'Impetigo': 40}}, inplace=True)

# print(df.head())

X = df[list_of_Symptoms]  # Assigning the Features or list_of_symptoms to the X variable for Training the model
y = df[["prognosis"]]  # Assigning the Target values to the y variable.
# Both The Variables X and y will be used for training the model.
np.ravel(y)  # np.ravel(y):
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr = pd.read_csv("Testing.csv")  # Reading the Testing Dataset here.
# Replacing all the target values with their respective index values
tr.replace(
    {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                   'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                   'Hypertension ': 10,
                   'Migraine': 11, 'Cervical spondylosis': 12,
                   'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                   'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                   'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                   'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                   'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                   'Varicose veins': 30, 'Hypothyroidism': 31,
                   'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                   '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                   'Psoriasis': 39,
                   'Impetigo': 40}}, inplace=True)

#X_test = tr[list_of_Symptoms]  # The List of symptoms are assigned to the X_test variable for validation purpose
#y_test = tr[["prognosis"]]  # The Target values are defined to the y_test for validation purpose.
#np.ravel(y_test)  # np.ravel(y_test)
# Split Data Below
#X_train, X_test, y_train, y_test = train_test_split(X,y,train_size  = 0.80, test_size = 0.2)
#print(X_train.shape, y_train.shape, X_test.shape, y_train.shape)
@app.route('/')
def Start():
    """
    Here, We are displaying the list_of_Symptoms to the user so for that in flask, we have assigned the list_of_Symptoms list
    to the List_Symptoms variable and returning the values of List_Symptoms to InputSymptoms.html and displaying the
    Symptoms on the Webapp
    In the following function we have passed 2 parameters:
        1. The Destination File. i.e the WebApp where all the Symptoms will be displayed
        2. List_Symptoms : This variable will be used as a reference to the html page. This parameter will actually pass
                        all the values from the backend to frontend
    """
    List_Symptoms = list_of_Symptoms #Display the list of symptoms to the user at Website.
    return rt('InputSymptoms.html', List_Symptoms=List_Symptoms)


@app.route('/DiseasePredicted', methods=['POST', 'GET'])
def Get():
    """
    Accepting the input from the user from those dropdown and creating a list using the function getlist().
    in getlist() we have passed 1 parameter "InputSymptoms" so, here it will find for the HTML tags having name = "InputSymptoms"
    For now we have 4 dropdown(s) so 4 symptoms will be get called here and a list will be created.
    """
    Symptom = request.form.getlist("InputSymptoms")
    DisplaySymptom1 = Symptom[0]
    DisplaySymptom2 = Symptom[1]
    DisplaySymptom3 = Symptom[2]
    DisplaySymptom4 = Symptom[3]
    DisplaySymptom5 = Symptom[4]
    print("List of Symptoms Provided by the user : ", Symptom)  # Printing the User provided Input
    print("Symptoms Accepted. Passing the Symptoms to the Algorithms : ")
    # DecisionTreeAlgorithm
    from sklearn import tree
    import matplotlib.pyplot as plt
    DecisionTree = tree.DecisionTreeClassifier(max_depth= 40, min_samples_leaf=40)
    DecisionTree = DecisionTree.fit(X, y) #Training is done here
    from sklearn.metrics import accuracy_score
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, test_size=0.2)
    y_pred = DecisionTree.predict(X_test)
    print("****Decision Tree Accuracy Score : ", accuracy_score(y_test, y_pred))

    #tree.plot_tree(DecisionTree, feature_names= list_of_Symptoms, class_names=list_of_disease, filled=True)
    #plt.show()
    #print("Decision Tree Accuracy Score (normalize = false)", accuracy_score(y_test, y_pred, normalize=False))
    for k in range(0, len(list_of_Symptoms)):
        # print (k,)
        for z in Symptom: #inputfor User
            if z == list_of_Symptoms[k]:
                list_Temp[k] = 1
    inputtest = [list_Temp]
    print(inputtest)
    predict = DecisionTree.predict(inputtest)
    #print("Predict", predict)
    predicted = predict[0]
    print("Predicted", predicted)
    print("\n")
    h = 'no'
    for a in range(0, len(list_of_disease)):
        if (predicted == a):
            h = 'yes'
            break
    if (h == 'yes'):
        print("Predicted Disease By Decision Tree is ", list_of_disease[a])
        OutputDisease = list_of_disease[a]
        OutDecisionTree = DSP(OutputDisease)
        #print(type(OutDecisionTree))
        print("About Decision tree Disease : ", OutDecisionTree)
        print('\n')
        OutDecisionTree_Description = OutDecisionTree[0]
        OutDecisionTree_Precautions = OutDecisionTree[1]
        OutDecisionTree_Specialist = OutDecisionTree[2]
        OutDecisionTree_LabTest = OutDecisionTree[3]
        OutDecisionTree_DiseaseDoList = OutDecisionTree[4]
        OutDecisionTree_DiseaseDontList = OutDecisionTree[5]
    else:
        print("Sorry, No Prediction")
    # RandomForestAlgorithm
    from sklearn.ensemble import RandomForestClassifier
    #To avoid the overfitting in the random forest classifier we can use the following methods
    # 1. n_estemators, 2. max_features, 3. max_depth, 4. min_samples_leaf
    clf4 = RandomForestClassifier(n_estimators= 10, max_features= 40, max_depth= 40)
    clf4 = clf4.fit(X, np.ravel(y)) #Training is done here
    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    print("****Accuracy Score for Random Forest : ", accuracy_score(y_test, y_pred))
    #print("Accuracy Score for Random Forest Normalise = False: ", accuracy_score(y_test, y_pred, normalize=False))
    # --------------------------------------------------------------
    for k in range(0, len(list_of_Symptoms)):
        for z in Symptom:
            if (z == list_of_Symptoms[k]):
                list_Temp[k] = 1
    inputtest = [list_Temp]
    predict = clf4.predict(inputtest)
    predicted = predict[0]
    h = 'no'
    for a in range(0, len(list_of_disease)):
        if (predicted == a):
            h = 'yes'
            break
    if (h == 'yes'):
        print("The Disease Predicted By Random Forest Algo is", list_of_disease[a])
        RandomForestPredictor = list_of_disease[a]
        OutRandomForest = DSP(RandomForestPredictor)
        #print(type(OutRandomForest))
        print("About Random Forest Disease", OutRandomForest)
        print("\n")
        OutRandomForest_Description = OutRandomForest[0]
        OutRandomForest_Precaution = OutRandomForest[1]
        OutRandomForest_Specialist = OutRandomForest[2]
        OutRandomForest_LabTest = OutRandomForest[3]
        OutRandomForest_DiseaseDoList = OutRandomForest[4]
        OutRandomForest_DiseaseDontList = OutRandomForest[5]
    else:
        print("Sorry, No Predictions Done!")
    # Naive Basyes Algorithm :
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X, np.ravel(y)) #Training is done here
    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print("****Accuracy Score for Naive Bayes : ", accuracy_score(y_test, y_pred))
    #print("Accuracy Score for Naive Bayes Normalise = False: ", accuracy_score(y_test, y_pred, normalize=False))
    # -----------------------------------------------------
    for k in range(0, len(list_of_Symptoms)):
        for z in Symptom:
            if (z == list_of_Symptoms[k]):
                list_Temp[k] = 1
    inputtest = [list_Temp]
    predict = gnb.predict(inputtest)
    predicted = predict[0]
    h = 'no'
    for a in range(0, len(list_of_disease)):
        if (predicted == a):
            h = 'yes'
            break
    if (h == 'yes'):
        print("The Disease Predicted by Naive Bayes is ", list_of_disease[a])
        NaiveBayesPredictor = list_of_disease[a]
        OutNaiveBayes = DSP(NaiveBayesPredictor)
        print('About NaiveBayes Disease',OutNaiveBayes)
        OutNaiveBayes_Description = OutNaiveBayes[0]
        OutNaiveBayes_Precaution = OutNaiveBayes[1]
        OutNaiveBayes_SpecialistName = OutNaiveBayes[2]
        #print("***********************OutNaiveBayes_SpecialistName", OutNaiveBayes_SpecialistName)
        OutNaiveBayes_LabTest = OutNaiveBayes[3]
        OutNaiveBayes_DiseaseDoList = OutNaiveBayes[4]
        OutNaiveBayes_DiseaseDontList = OutNaiveBayes[5]
    else:
        print("Sorry, No Predictions Done!")
    return rt('Department.html', DisplaySymptom1 = DisplaySymptom1, DisplaySymptom2 = DisplaySymptom2,
    DisplaySymptom3 = DisplaySymptom3, DisplaySymptom4 = DisplaySymptom4, DisplaySymptom5 = DisplaySymptom5,
    OutputDisease=OutputDisease,RandomForestPredictor=RandomForestPredictor, NaiveBayesPredictor=NaiveBayesPredictor,

    OutNaiveBayes_Description = OutNaiveBayes_Description, OutNaiveBayes_Precaution = OutNaiveBayes_Precaution,
    OutNaiveBayes_SpecialistName = OutNaiveBayes_SpecialistName,OutNaiveBayes_LabTest = OutNaiveBayes_LabTest, OutNaiveBayes_DiseaseDoList = OutNaiveBayes_DiseaseDoList,
    OutNaiveBayes_DiseaseDontList = OutNaiveBayes_DiseaseDontList,

    OutRandomForest_Description = OutRandomForest_Description,
    OutRandomForest_Precaution = OutRandomForest_Precaution,OutRandomForest_LabTest = OutRandomForest_LabTest,OutRandomForest_Specialist = OutRandomForest_Specialist,
    OutRandomForest_DiseaseDoList = OutRandomForest_DiseaseDoList,OutRandomForest_DiseaseDontList = OutRandomForest_DiseaseDontList,

    OutDecisionTree_Description = OutDecisionTree_Description,OutDecisionTree_Precautions = OutDecisionTree_Precautions,
    OutDecisionTree_Specialist = OutDecisionTree_Specialist, OutDecisionTree_DiseaseDoList = OutDecisionTree_DiseaseDoList,
    OutDecisionTree_DiseaseDontList = OutDecisionTree_DiseaseDontList, OutDecisionTree_LabTest = OutDecisionTree_LabTest, InputSymp = Symptom)

#The Following code is to display the Disease Information such as Disease Description, Precautions, Do's and Don'ts,
#Specialist etc.
@app.route("/")
def DSP(Input): #Method for Disease Information
    DiseaseSearch = Input
    String_for_precautions = ""
    DescriptionReturn = " "  # Description of the Disease
    SpecialistName = ""  # SpecialistName
    Precautions = []
    Labtest = []
    DiseaseDoList = []
    DiseaseDontList = []
    #Opening the CSV files below :
    DescriptionFile = open("symptom_Description_f.csv")
    PrecautionFile = open("symptom_precaution_final.csv")
    SpecialistFile = open("Specialist1.csv")
    DiseaseDoFile = open("symptom_precaution_dos.csv")
    DiseaseDontFile = open("Symptom_precaution_donts.csv")
    #Reading the CSV file below :
    Description = csv.reader(DescriptionFile)
    Precaution = csv.reader(PrecautionFile)
    Specialist = csv.reader(SpecialistFile)
    DiseaseDo = csv.reader(DiseaseDoFile)
    DiseaseDont = csv.reader(DiseaseDontFile)
    for row in Description:
        for row[0] in row:
            if row[0] == DiseaseSearch:
                DescriptionReturn = row[1]
    for row in Precaution:
        for row[0] in row:
            if row[0] == DiseaseSearch:
                Precautions = [row[1], row[2], row[3], row[4], row[5], row[6]]
                #String_for_precautions = "".join(Precautions)
    for row in Specialist:
        for row[0] in row:
            if row[0] == DiseaseSearch:
                SpecialistName = row[1]
                Labtest = [row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
    for row in DiseaseDo:
        for row[0] in row:
            if row[0] == DiseaseSearch:
                DiseaseDoList = [row[1], row[2], row[3]]
    for row in DiseaseDont:
        for row[0] in row:
            if row[0] in row:
                DiseaseDontList = [row[1], row[2], row[3]]
    print("Details are below",DescriptionReturn, Precautions, SpecialistName, Labtest, DiseaseDoList, DiseaseDontList)
    return [DescriptionReturn, Precautions, SpecialistName, Labtest, DiseaseDoList, DiseaseDontList]
if __name__ == '__main__':
    app.run(debug=True)

"""
Current Problems with the Algorithms : 
1. Overfitting
<button type="button" class="collapsible">{{OutputDisease}}</button>
<div class="content">
  <p>{{DecisionTreeDSP}}</p>
   <p>{{DescriptionReturn1}}</p>
  {%for Temp in Precautions_Decision%}
      <p>{{Temp}}</p>
  {%endfor%}
  <p>Do's and Dont's</p>
</div><br><br>
<button type="button" class="collapsible">{{RandomForestPredictor}}</button>
<div class="content">
  <p>{{RandomForestDSP}}</p>
  <p>{{DescriptionReturn2}}</p>
  <p>Do's and Dont's</p>
</div><br><br>
<button type="button" class="collapsible">{{NaiveBayesPredictor}}</button>
<div class="content">
  <p>{{DSP1}}</p>
  <p>{{DescriptionReturn}}</p>
  <p>Do's and Dont's</p>
</div>
Disease Input Symptoms HTML Code below
<div class="container" style="padding-top:300px;">
<select class="form-control select2" multiple="multiple" style="width:100%; height: 100%; color: chartreuse; padding-left:15px; padding-right:15px;"></select>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"
            integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
            crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"
            integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU="
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.5/js/select2.full.min.js"></script>
    <script>
        $('.select2').select2({
            data: ["Piano", "Flute", "Guitar", "Drums", "Photography"],
            tags: true,
            maximumSelectionLength: 10,
            tokenSeparators: [',', ' '],
            placeholder: "Select or type keywords",
            //minimumInputLength: 1,
            //ajax: {
           //   url: "you url to data",
           //   dataType: 'json',
            //  quietMillis: 250,
            //  data: function (term, page) {
            //     return {
            //         q: term, // search term
            //    };
           //  },
           //  results: function (data, page) { 
           //  return { results: data.items };
          //   },
          //   cache: true
           // }
        });
    </script>
</div>
"""
