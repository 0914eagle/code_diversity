
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    else:
        ap = average_temperatures[1] - average_temperatures[0]
        if all(average_temperatures[i+1] - average_temperatures[i] == ap for i in range(n-1)):
            return average_temperatures[-1] + ap
        else:
            return average_temperatures[-1]

