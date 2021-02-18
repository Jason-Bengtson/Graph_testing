from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import IsolationForest


network_traffic_data = fetch_kddcup99('http', percent10=True)
network_traffic_data['data'].shape
print(network_traffic_data['DESCR'])
X = network_traffic_data['data']
y_true = network_traffic_data['target']

print(y_true)
anom = 0
normal = 0
for j in y_true:
    if j == ('normal.'):
        normal+=1
    else:
        anom+=1
print("Normal data: ", normal)
print("Anomalous data: ", anom)

clf = IsolationForest(max_samples=200, random_state=2)
clf.fit(X)
y_pred = clf.predict(X)
print(y_pred)
neg = 0
pos = 0
for i in y_pred:
    if i == 1:
        pos+=1
    else:
        neg+=1
print("Number of -1 in y_pred: ", neg)
print("Number of 1 in y_pred: ", pos)


