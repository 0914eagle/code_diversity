
import sys

def get_probability(prediction, n):
    probability = 1
    for i in range(n):
        if prediction[i] == 'R':
            probability *= 1/3
        elif prediction[i] == 'P':
            probability *= 1/3
        else:
            probability *= 1/3
    return probability

def get_predictions(n, s):
    predictions = []
    for i in range(s):
        prediction = sys.stdin.readline().strip()
        predictions.append((prediction, get_probability(prediction, n)))
    return sorted(predictions, key=lambda x: x[1], reverse=True)

n, s = map(int, input().split())
predictions = get_predictions(n, s)
for prediction, probability in predictions:
    print(prediction)

