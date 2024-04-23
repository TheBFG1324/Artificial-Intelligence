# Fixed increment error-correction learning rule

# Learning rate
alpha = 1

# Initial weights
weights = [0, 0, 0, 0]  # Includes w0 for the threshold

# Training data
training_data = [
    ([1, 1, 0, 0], 1),
    ([1, 0, 1, 1], 0),
    ([1, 1, 1, 0], 1),
    ([1, 1, 1, 1], 0),
    ([1, 0, 0, 1], 0),
    ([1, 1, 0, 1], 1)
]

# Train the perceptron
def train_perceptron(data, weights, alpha):
    epoch = 1
    while True:
        print(f"Epoch {epoch + 1}")
        weights_changed = False
        for inputs, target in data:
            print("data:")
            print(inputs, target)
            # Calculate the actual output
            output = 1 if sum(w * i for w, i in zip(weights, inputs)) >= 0 else 0
            print("output:")
            print(output)
            # Update weights if there's an error
            if output != target:
                weights = [w + alpha * (target - output) * i for w, i in zip(weights, inputs)]
                weights_changed = True
            print("weights")
            print(weights)
            print("--------")
        if not weights_changed:
            # If weights haven't changed this epoch, we are done
            break
        epoch += 1
    return weights, epoch

# Training the unit with the fixed increment error-correction procedure
final_weights, total_epochs = train_perceptron(training_data, weights, alpha)
print("Final weights:", final_weights)
print("Total epochs:", total_epochs)
