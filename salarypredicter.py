import joblib
a=joblib.load("trainmodel.pk1")

#now to test model to predict salary
p=int(input("enter years of experience "))
sl=a.predict([[p]])

#now the predicted salary
print("predicted salary is : ", round(sl[0],2), "INR.")


