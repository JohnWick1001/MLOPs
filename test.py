#load dataset
import pandas

db=pandas.read_csv("SalaryData.csv")
print("dataset has been loaded succesfully")

#to create feature and target variable

x=db[["YearsExperience"]]
y=db["Salary"]

#To train model

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
print("model has been created")

#To save model

import joblib
joblib.dump(model, "trainmodel.pk1")
print("model has been saved ")

