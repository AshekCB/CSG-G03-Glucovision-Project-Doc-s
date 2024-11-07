#Loading Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,BaggingClassifier,GradientBoostingClassifier,VotingClassifier,StackingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

#Loading the Dataset
df=pd.read_csv("D:\pj files upto date\Project Files\pre-processed-data.csv")

#Feature Extraction
x = df.drop('Outcome', axis=1)#Dependents
y = df['Outcome']#Independent


#model selction
log=LogisticRegression(max_iter=3500)
dt=DecisionTreeClassifier()
rf=RandomForestClassifier()
svc=SVC()
nb=GaussianNB()
knn=KNeighborsClassifier()
ada=AdaBoostClassifier(algorithm="SAMME")
bag=BaggingClassifier()
gb=GradientBoostingClassifier()
vc=VotingClassifier(estimators=2000)

models=[log,dt,rf,svc,nb,knn,ada,bag,gb]

#Data Splitting for test and train of model
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)



def predictions(df):
    predictions_list=[]
    for model in models:
        model.fit(x_train,y_train)
    y_pred=model.predict(df)
    predictions_list.append(y_pred[0])

    if predictions_list.count(0)>predictions_list.count(1):
       return 0
    else:
       return 1


#
def predictor(p,g,bp,st,ins,bmi,dpf,age):
  d={
      'Pregnancies':p,
      'Glucose':g,
      'BloodPressure':bp,
      'SkinThickness':st,
      'Insulin':ins,
      'BMI':bmi,
      'DiabetesPedigreeFunction':dpf,
      'Age':age
  }
  df=pd.DataFrame(d,index=[0])
  res=predictions(df)
  return int(res)
#print(predictor(8.5,126,90,0,0,43.4,0.583,42))
#output -->1


