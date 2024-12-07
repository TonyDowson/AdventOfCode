def extrapolate_next_value(sequence):
    while True:
        differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        if all(diff == 0 for diff in differences):
            return sequence[-1] + differences[-1]
        sequence.append(0)

def predict_next_values(histories):
    next_values = []
    for history in histories:
        sequence = list(map(int, history.split()))
        next_value = extrapolate_next_value(sequence)
        next_values.append(next_value)
    return next_values

# Example input data
histories = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]

# Predict next values for each history
predicted_values = predict_next_values(histories)
print("Predicted values:", predicted_values)

# Sum of predicted next values
total_sum = sum(predicted_values)
print("Sum of predicted values:", total_sum)
