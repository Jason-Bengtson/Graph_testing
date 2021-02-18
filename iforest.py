from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt


network_traffic_data = fetch_kddcup99('http', percent10=True)
network_traffic_data['data'].shape
print(network_traffic_data['DESCR'])
X = network_traffic_data['data']
y_true = network_traffic_data['target']

print(y_true)


myarray = []


anom = 0
normal = 0
for j in y_true:
    #print(type(j))
    # print(j)
    if j == b'normal.':
        normal+=1
        myarray.append("normal")
    else:
        anom+=1
        myarray.append("not normal")


print("Normal data: ", normal)
print("Anomalous data: ", anom)

clf = IsolationForest(max_samples=300, random_state=2)
clf.fit(X)
y_pred = clf.predict(X)
print(y_pred)
myotherarray = []

neg = 0
pos = 0
for i in y_pred:
    if i == 1:
        pos+=1
        myotherarray.append("1")
    else:
        neg+=1
        myotherarray.append("-1")

print("Number of -1 in y_pred: ", neg)
print("Number of 1 in y_pred: ", pos)



true_pos = 0
false_pos = 0
true_neg = 0
false_neg = 0

for i in range(len(myarray)):
    if myarray[i] == 'normal' and myotherarray[i] == '1':
        true_neg += 1
    elif myarray[i] == 'normal' and myotherarray[i] == '-1':
        false_neg += 1
    elif myarray[i] == 'not normal' and myotherarray[i] == '1':
        false_pos += 1
    else:
        true_pos += 1





# for k in len(y_pred):
#     if (k in y_pred == 1 and k in y_true == b'normal.'):
#         true_pos +=1
#         if 
#     elif k == 1:
#         false_pos +=1
#     elif (k in y_pred == -1  and k in y_true == b'normal.'):
#         false_neg +=1
#     else:
#         true_neg +=1
print("True positive: ", true_pos)
print("False positive: ", false_pos)
print("True negative: ", true_neg)
print("False negative: ", false_neg)

# for k in y_pred and j in y_true:
#     if k ==1:
#         if j == b'normal.':
#             true_pos+=1
#     if k ==1:
#         if j != b'normal.':
#             false_pos+=1
#     if k == -1:
#         if j != b'normal.':
#             true_neg+=1
#     else:
#         false_neg += 1


def plot(true_pos, false_pos, true_neg, false_neg):
    print()
    print("Made it into the scatter plot function")


    fig=plt.figure()
    #ax=fig.add_axes([0,0,1,1])
    # ax.scatter(x, y, color='b')
    # plt.show()
    
    x = np.arange(4)
    plt.bar(x, height=[true_pos, false_pos, true_neg, false_neg])
    plt.xticks(x, ['true positive', 'false positive', 'true negative', 'false negative'])

    plt.show()



plot(true_pos, false_pos, true_neg, false_neg)