
def predict_temperature(n, temperatures):
    # Check if the temperatures form an arithmetic progression
    difference = temperatures[1] - temperatures[0]
    for i in range(2, n):
        if temperatures[i] - temperatures[i-1] != difference:
            return temperatures[n-1]
    
    # If they form an arithmetic progression, return the next term
    return temperatures[n-1] + difference

