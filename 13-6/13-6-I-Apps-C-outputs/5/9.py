
def predict_temperature(n, temperatures):
    # Check if the temperatures form an arithmetic progression
    if temperatures[1] - temperatures[0] == temperatures[2] - temperatures[1]:
        # If they do, return the next term of the progression
        return temperatures[-1] + (temperatures[1] - temperatures[0])
    else:
        # If they don't, return the temperature of the last day
        return temperatures[-1]

