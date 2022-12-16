# this is how it works 
# KNN is the supervised type of K-mean
# Both works on Euclidean distance
# Both compute the distance 
#select to whom they are minimuim 
# below is the code
import math
import pandas as pd

from sklearn.model_selection import train_test_split

def euclidian_dist(p1, p2):
    dim, sum_ = len(p1), 0
    for index in range(dim - 1):
        sum_ += math.pow(p1[index] - p2[index], 2)
    return math.sqrt(sum_)

from statistics import mode
def knn(i,testing_data,listData,k):
    e_dis = []
    
    index = 0
    for j in testing_data:
        e_dis.append([index,euclidian_dist(i,j)])
        index += 1
    
    e_dis.sort(key = lambda row: row[1] ,reverse = True)
    top_dis = e_dis[0:k]
    
    temp = []
    for k in top_dis:
        k.append(listData[k[0]][4])
        temp.append(listData[k[0]][4])
    return mode(temp)    
    
data = pd.read_csv("Desktop/iris.data")
data.head()

listOfData = data.values.tolist()

data.columns = ["x1","x2","x3","x4","y"]
train , test = train_test_split(listOfData, test_size = 0.30)

testing_data = []

for i in test:
    temp = i[0:4]
    testing_data.append(temp)

# final_data = []
# for i in testing_data:
#     final_data.append(knn(i,testing_data,listOfData,3))
    
final_data = []
for i in testing_data:
    final_data.append(knn(i,testing_data,test,3))
    
counter = 0
for k in range(len(final_data)):
    if final_data[k] == listOfData[k][4]:
        counter += 1
        
perc = (counter/len(final_data)) * 100
print(perc)