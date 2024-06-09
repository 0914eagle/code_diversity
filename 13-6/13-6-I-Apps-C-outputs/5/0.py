
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    else:
        ap = average_temperatures[1] - average_temperatures[0]
        for i in range(2, n):
            if average_temperatures[i] - average_temperatures[i-1] != ap:
                return average_temperatures[n-1]
        return average_temperatures[n-1] + ap

