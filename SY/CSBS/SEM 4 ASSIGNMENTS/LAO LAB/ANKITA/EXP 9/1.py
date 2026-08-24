import pandas as pd
import numpy as np

data = pd.read_csv("breast-cancer.csv")
data = data.select_dtypes(include=[np.number])

X = data[data.columns[:-1]].values
y = data[data.columns[-1]].values.reshape(-1, 1)
X = np.hstack((np.ones((X.shape[0], 1)), X))
m, n = X.shape
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(y, y_predict):
    y_predict = np.clip(y_predict, 1e-10, 1-1e-10)
    return -(1/m) * np.sum(y*np.log(y_predict) + (1-y)*np.log(1-y_predict))

def newton_method(X, y, iterations=5):
    W = np.zeros((n, 1))
    for i in range(iterations):
        z = X @ W
        y_predict = sigmoid(z)
        grad = (1/m) * (X.T @ (y_predict - y))
        S = np.diag((y_predict * (1 - y_predict)).flatten())
        lambda_ = 1e-4
        H = (1/m) * (X.T @ S @ X) + lambda_ * np.eye(n)
        W = W - np.linalg.pinv(H) @ grad
        
        print(f"Iteration {i+1}, Cost: {cost(y, y_predict)}")
    
    return W

W = newton_method(X, y)

y_predict = sigmoid(X @ W) >= 0.5
print("\nPredictions:\n", y_predict.astype(float))
