# Using the built-in Perceptron from scikit-learn
from sklearn.linear_model import Perceptron
import numpy as np

# --- Example Usage ---
if __name__ == '__main__':
    
    # 1. Define a simple, linearly separable dataset (Logical OR)
    # X represents the features ([input1, input2])
    # We use lists here, but numpy arrays work just as well
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    
    # y represents the target labels (0 OR 0 = 0, 0 OR 1 = 1, etc.)
    y = np.array([0, 1, 1, 1])

    print("--- Training sklearn.linear_model.Perceptron on 'OR' dataset ---")
    
    # 2. Create and train the Perceptron
    # tol=1e-3 is the stopping criterion
    # random_state=42 ensures we get the same results each time
    ppn = Perceptron(tol=1e-3, random_state=42)
    
    # Before fitting, the model is not yet initialized.
    # By default, sklearn Perceptron initializes weights and bias to zeros.
    print(f"\nInitial Weights (default): {np.zeros(X.shape[1])}")
    print(f"Initial Bias (default): {np.array([0.0])}")

    ppn.fit(X, y)

    # 3. Print the results
    # .coef_ holds the weights
    # .intercept_ holds the bias
    print(f"\nFinal Weights: {ppn.coef_}")
    print(f"Final Bias: {ppn.intercept_}")

    # 4. Test the trained model
    # Note: .predict() expects a 2D array, so [0, 0] becomes [[0, 0]]
    print("\n--- Testing the trained 'OR' model ---")
    print(f"Prediction for [0, 0] (Expected 0): {ppn.predict([[0, 0]])[0]}")
    print(f"Prediction for [0, 1] (Expected 1): {ppn.predict([[0, 1]])[0]}")
    print(f"Prediction for [1, 0] (Expected 1): {ppn.predict([[1, 0]])[0]}")
    print(f"Prediction for [1, 1] (Expected 1): {ppn.predict([[1, 1]])[0]}")

    # Example: AND dataset (also linearly separable)
    print("\n\n--- Training sklearn.linear_model.Perceptron on 'AND' dataset ---")
    y_and = np.array([0, 0, 0, 1])
    ppn_and = Perceptron(tol=1e-3, random_state=42)
    
    # Before fitting, the model is not yet initialized.
    # By default, sklearn Perceptron initializes weights and bias to zeros.
    print(f"\nInitial Weights (default): {np.zeros(X.shape[1])}")
    print(f"Initial Bias (default): {np.array([0.0])}")
    
    ppn_and.fit(X, y_and)
    
    print(f"\nFinal Weights: {ppn_and.coef_}")
    print(f"Final Bias: {ppn_and.intercept_}")

    print("\n--- Testing the 'AND' model ---")
    print(f"Prediction for [0, 0] (Expected 0): {ppn_and.predict([[0, 0]])[0]}")
    print(f"Prediction for [0, 1] (Expected 0): {ppn_and.predict([[0, 1]])[0]}")
    print(f"Prediction for [1, 0] (Expected 0): {ppn_and.predict([[1, 0]])[0]}")
    print(f"Prediction for [1, 1] (Expected 1): {ppn_and.predict([[1, 1]])[0]}")

