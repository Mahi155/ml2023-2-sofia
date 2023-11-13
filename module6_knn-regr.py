import numpy as np

def knn_regression(N, k):
    if k > N:
        return "Error: k should be less than or equal to N."

    data = np.zeros((N, 2))

    for i in range(N):
        x = float(input(f"Enter x value for data point {i + 1}: "))
        y = float(input(f"Enter y value for data point {i + 1}: "))
        data[i] = [x, y]

    X_input = float(input("Enter the value of X for prediction: "))

    if k <= N:
        distances = np.array([np.sqrt(np.sum((X_input - point[0]) ** 2)) for point in data])
        sorted_indices = np.argsort(distances)
        k_nearest_neighbors = data[:, 1][sorted_indices[:k]]
        result = np.mean(k_nearest_neighbors)
        return f"The result of k-NN Regression for X = {X_input} is: {result}"
