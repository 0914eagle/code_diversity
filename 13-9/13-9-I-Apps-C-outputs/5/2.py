
def sort_predictions(predictions):
    n = len(predictions[0])
    s = len(predictions)
    probability = [[0 for _ in range(s)] for _ in range(n)]
    for i in range(n):
        for j in range(s):
            probability[i][j] = 1
    for i in range(n-1):
        for j in range(s):
            probability[i+1][j] *= (probability[i][j] if predictions[j][i] == 'R' else 1-probability[i][j])
    for i in range(n):
        for j in range(s):
            probability[i][j] /= probability[n-1][j]
    return sorted(predictions, key=lambda x: max(probability[n-1][i] for i in range(s)), reverse=True)

