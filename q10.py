from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score, train_test_split
from matplotlib import pyplot as plt
x,y=datasets.load_iris(return_X_y=True)
x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size=0.25,random_state =20)
f=[]
cross=[]
for c in range(1,10):
  kNN=KNeighborsClassifier(c).fit(x_train,y_train)
  y_predict = kNN.predict(x_test)
  f_measure_score = f1_score(y_test,y_predict,average='micro')
  cross_validation_score = cross_val_score(kNN, x,y)
  f.append(f_measure_score)
  cross.append(cross_validation_score.mean())
plt.plot(range(9),cross,label = "cros - validation")
plt.plot(range(9),f,label="F-Measure")
plt.legend()
