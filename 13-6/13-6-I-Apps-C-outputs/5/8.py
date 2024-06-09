
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    else:
        ap = average_temperatures[n-1] - average_temperatures[n-2]
        if ap == 0:
            return average_temperatures[n-1]
        else:
            return average_temperatures[n-1] + ap

