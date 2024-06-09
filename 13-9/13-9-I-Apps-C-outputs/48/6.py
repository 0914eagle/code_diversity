
def get_predicted_temperature(temperature_sequence):
    n = len(temperature_sequence)
    if n == 1:
        return temperature_sequence[0]
    else:
        # Check if the sequence forms an arithmetic progression
        difference = temperature_sequence[1] - temperature_sequence[0]
        for i in range(2, n):
            if temperature_sequence[i] - temperature_sequence[i - 1] != difference:
                return temperature_sequence[n - 1]
        # If the sequence forms an arithmetic progression, return the next term
        return temperature_sequence[n - 1] + difference

