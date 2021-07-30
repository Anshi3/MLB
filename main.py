import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
import  pandas  as  pd
from  sklearn.pipeline  import  Pipeline
from  sklearn.preprocessing  import  PolynomialFeatures 
from  sklearn.linear_model  import  LinearRegression
# import pdb;pdb.set_trace()


f=open('ML_FILE.csv')

envframe=pd.read_csv(f)
value1=(envframe['Value'])
year1=(envframe['Year']) 
day1=(envframe['Day']) 
month1=(envframe['Month']) 
value_train=np.asarray(value1) 
year_train=np.asarray(year1) 
day_train=np.asarray(day1) 
month_train=np.asarray(month1)

f1=open('test.csv') 
envframe1=pd.read_csv(f1) 
value=(envframe['Value'])
year=(envframe['Year']) 
day=(envframe['Day']) 
month=(envframe['Month']) 
value_test=np.asarray(value) 
year_test=np.asarray(year) 
day_test=np.asarray(day) 
month_test=np.asarray(month)

i  =  np.vstack((year_train,month_train)).T 
j  =  np.vstack((year_test,month_test)).T

x_train = np.vstack((year_train,month_train,day_train)).T
x_test = np.vstack((year_test,month_test,day_test)).T


y_train  =	value_train 
y_test  =	value_test

model  = Pipeline([('poly', PolynomialFeatures(degree=2)),('linear', LinearRegression(fit_intercept=False))])
# model=linear_model.LinearRegression()
model.fit(x_train,y_train)
# regr.fit(x_train,y_train)
model.named_steps['linear'].coef_ 
year=np.array([int(input("enter year = "))])
day=np.array([int(input("enter day = "))])
month=np.array([int(input(" enter month = "))])

x_test1=np.stack((year,day,month)).T
# x_test1.reshape(1,-1)




value_predict=model.predict(x_test1)
print(value_predict)

n=int(input())
for i in range (0,n):
    input()


#plt.scatter(day_test,y_test,color='black') #o=np.vstack((year_train)).T
j=[]
plt.xlabel("YEARS")
plt.ylabel("VALUE")

for e in year_test:
    j.append(str(e))
print(j) 
tick_label=j



# plt.scatter(year_test,value_test,label="dots",color='black',marker= '*',s=20)
# plt.plot(year_test,value_predict,color='red',linewidth=3)

# #plt.xticks((j)) #plt.yticks((y_train)) 
# print(value_predict)
# print('Mean  Squared  Error:%.2f'  % mean_squared_error(y_test,value_predict)  )
# plt.savefig("1st_test.png") #global error error=mean_squared_error(y_test,wind_predict)