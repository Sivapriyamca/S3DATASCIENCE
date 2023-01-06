import pandas as pd
from sklearn import tree,metrics,model_selection
data=pd.read_csv('car.csv',names=['buying','main','indoor','person','lug_root','safety','class'])
data.head()
data.info()
data['class'],class_names=pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())
data['buying'],_=pd.factorize(data['buying'])
data['main'],_=pd.factorize(data['main'])
data['indoor'],_=pd.factorize(data['indoor'])
data['person'],_=pd.factorize(data['person'])
data['lug_root'],_=pd.factorize(data['lug_root'])
data['safety'],_=pd.factorize(data['safety'])
data.head()
data.info()
X=data.iloc[:,:-1]
y=data.iloc[:-1]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
dtree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(X_train,y_train)
y_pred=dtree.predict(X_test)
accuracy=metrics.accuracy_score(y_test,y_pred)
print("accuracy:{:.2f}".format(accuracy))
count_mislabeled=(y_test!=y_pred)
print("mislabeled sample.{}".format(count_mislabeled))



