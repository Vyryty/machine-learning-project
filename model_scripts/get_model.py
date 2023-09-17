import os
import pickle as pk
import csv
from sklearn.neural_network import MLPClassifier

def load_model(path: str):
    result = None
    if os.path.exists(path):
        with open(path, "rb") as file:
            result = pk.load(file)
    return result

def save_model(model, path: str):
    with open(path, "wb") as file:
        pk.dump(model, file)



def read_csv(path: str) -> tuple[list[list[int]], list[int]]:
    result = ([], [])
    with open(path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            result[0].append([int(i) for i in row[:-1]])
            result[1].append(row[-1])
    return result

def test_model(model: MLPClassifier, path: str, max_print=20):
    test_X, test_Y = read_csv(path)
    results = model.predict(test_X)
    for i in range(min(len(test_X), max_print if max_print >= 0 else len(results))):
        print(f"Item {i}:")
        print(test_X[i])
        print(f"Expected: {test_Y[i]}, Predicted: {results[i]}\n")

def train_model(path: str):
    train_X, train_Y = read_csv(path)
    #for i in range(5):
    #    print(train_X[i], f"Length: {len(train_X[i])}")
    #    print(train_Y[i])

    return MLPClassifier().fit(train_X, train_Y)