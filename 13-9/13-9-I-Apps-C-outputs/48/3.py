
def predict_temperature(average_temperatures):
    n = len(average_temperatures)
    if n == 1:
        return average_temperatures[0]
    else:
        arith_progression = True
        for i in range(n-1):
            if average_temperatures[i] + (n-i-1) != average_temperatures[i+1]:
                arith_progression = False
                break
        if arith_progression:
            return average_temperatures[0] + (n+1) * (average_temperatures[n-1] - average_temperatures[0]) // n
        else:
            return average_temperatures[n-1]

