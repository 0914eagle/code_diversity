
def predict_temperature(average_temperatures):
    # Check if the average temperatures form an arithmetic progression
    if all(average_temperatures[i] + i == average_temperatures[i+1] for i in range(len(average_temperatures)-1)):
        # If they do, return the next term of the progression
        return average_temperatures[-1] + len(average_temperatures)
    else:
        # If they don't, return the last temperature
        return average_temperatures[-1]

