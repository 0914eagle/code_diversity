
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    else:
        ap = is_arithmetic_progression(average_temperatures)
        if ap:
            return average_temperatures[-1] + (n + 1) * (average_temperatures[1] - average_temperatures[0])
        else:
            return average_temperatures[-1]

def is_arithmetic_progression(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return True
    else:
        common_difference = average_temperatures[1] - average_temperatures[0]
        for i in range(2, n):
            if average_temperatures[i] - average_temperatures[i - 1] != common_difference:
                return False
        return True

average_temperatures = [10, 5, 0, -5, -10]
print(predict_temperature(average_temperatures))

