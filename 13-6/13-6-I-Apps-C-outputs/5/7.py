
def predict_temperature(n, temperatures):
    # Check if the temperatures form an arithmetic progression
    if temperatures[n] - temperatures[n-1] == temperatures[n-1] - temperatures[n-2]:
        # If they do, return the next term of the progression
        return temperatures[n] + (temperatures[n] - temperatures[n-1])
    else:
        # If they don't, return the temperature of the previous day
        return temperatures[n-1]

