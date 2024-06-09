
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    elif n == 2:
        return average_temperatures[1]
    else:
        ap = average_temperatures[1] - average_temperatures[0]
        if ap == average_temperatures[2] - average_temperatures[1]:
            return average_temperatures[-1] + ap
        else:
            return average_temperatures[-1]

