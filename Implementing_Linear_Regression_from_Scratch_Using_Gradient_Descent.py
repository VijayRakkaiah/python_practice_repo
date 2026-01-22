# given a small dataset of points:
# x = [1, 2, 3, 4, 5]
# y = [3, 5, 7, 9, 11]   # roughly y = 2x + 1

# task is to learn the parameters w (weight) and b (bias) such that:
# y_pred = w * x + b

# Tasks

# 1. Initialize w and b to 0
# 2. Define Mean Squared Error (MSE) loss
# 3. Compute gradients of loss w.r.t w and b
# 4. Update parameters using gradient descent
# 5. Train for 1000 iterations
# 6. Print final w and b

# -------------------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

w = 0.0
b = 0.0
lr = 0.01
n = len(x)

for epoch in range(1000):
    dw = 0
    db = 0

    for i in range(n):
        y_pred = w * x[i] + b
        error = y_pred - y[i]
        dw += x[i] * error
        db += error

    dw = (2 / n) * dw
    db = (2 / n) * db

    w -= lr * dw
    b -= lr * db

    if epoch % 100 == 0:
        loss = sum((w*x[i] + b - y[i])**2 for i in range(n)) / n
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

print("Final w:", w)
print("Final b:", b)

# -----------------------------------------------------------------

# OUTPUT
# w ≈ 2
# b ≈ 1
