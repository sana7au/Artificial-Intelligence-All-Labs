import numpy as np

probs = np.array([[0.7, 0.2, 0.1],
                  [0.1, 0.6, 0.3],
                  [0.2, 0.2, 0.6],
                  [0.5, 0.3, 0.2],
                  [0.1, 0.3, 0.6]])

y_test = np.array([0, 1, 2, 1, 2])

w_true = np.array([150.0, 120.0, 200.0, 180.0])
w_pred = np.array([140.0, 130.0, 210.0, 170.0])

# Find the predicted fruit class with highest probability
y_pred = np.argmax(probs, axis=1)

print("Predicted:", y_pred)

accuracy = np.mean(y_pred == y_test)
print("Accuracy:", round(accuracy, 2))

mse = np.mean((w_true - w_pred) ** 2)
print("MSE:", mse)

# Display samples classified incorrectly
print("Wrongly predicted samples:", np.where(y_pred != y_test)[0])