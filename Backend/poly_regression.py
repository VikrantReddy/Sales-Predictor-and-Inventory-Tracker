from sklearn.metrics import mean_squared_error, r2_score
import operator
import matplotlib.pyplot as plt
import numpy as np
import pickle
from collections import Counter
from sqldb import sqldb

def PlotGraphs(X, Y, Z):
    plt.scatter(X, Y)
    sort_axis = operator.itemgetter(0)
    sorted_zip = sorted(zip(X, Z), key=sort_axis)
    x, y_poly_pred = zip(*sorted_zip)
    plt.plot(x, y_poly_pred, color="m")
    plt.show()


def CustomPolynomialModelPredict(data, degree,training_percent):
    marker = 0
    for i in data:
        marker += 1
        if (60*training_percent)//100 <= int(i.split("-")[0]):
            break
    
    training_data = list(data.keys())[:marker]
    test_data = [i for i in list(data.keys())[marker:] if list(data.keys())[marker].split("-")[0] == i.split("-")[0]]

    normalized_training_data = {}

    for i in training_data:
        normalized_training_data[i.split("-")[1]] = normalized_training_data.get(i.split("-")[1],0) + data[i]

    c = Counter([i.split("-")[1] for i in training_data])

    for i in normalized_training_data:
        normalized_training_data.update({i:round(normalized_training_data[i]/c[i],2)})

    print(c)

    normalized_test_data = {}

    for i in test_data:
        normalized_test_data[i.split("-")[1]] = normalized_test_data.get(i.split("-")[1],0) + data[i]

    for i in normalized_test_data:
        normalized_test_data.update({i:round(normalized_test_data[i],2)})

    x = list(map(int,normalized_training_data.keys()))
    y = list(normalized_training_data.values())

    mymodel = np.poly1d(np.polyfit(x, y, degree))

    myline = np.linspace(1, 22, 100)

    x_test = list(map(int,normalized_test_data.keys()))
    y_test = list(normalized_test_data.values())

    print(y_test)

    y_predicted = list(map(mymodel,x_test))

    print(y_predicted)

    plt.scatter(x_test, y_test,c="b")
    plt.scatter(x, y,c="r")
    plt.plot(myline, mymodel(myline))
    plt.show()

    rmse = np.sqrt(mean_squared_error(y_test, y_predicted))
    r2 = r2_score(y_test, y_predicted)

    return rmse, r2


if __name__ == "__main__":
    with open("Backups/cost.pickle","rb") as file:
        data = pickle.load(file)

    print(CustomPolynomialModelPredict(data,3,90))

    #Change the way to training and testing
    #Train with a part of the data and test the next day's forecast

