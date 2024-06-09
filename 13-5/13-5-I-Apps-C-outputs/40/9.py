
def solve(n, firings, hirings):
    # Initialize the number of HR people needed
    k = 1
    # Initialize the HR person in charge of the firing and hiring on each day
    hr_people = [1] * n
    # Loop through each day
    for i in range(1, n):
        # Calculate the number of workers fired on the current day
        fired = firings[i]
        # Calculate the number of workers hired on the current day
        hired = hirings[i]
        # If the number of workers fired is greater than the number of workers hired,
        # then the HR person in charge of the firing and hiring on the current day
        # is the same as the previous day
        if fired > hired:
            hr_people[i] = hr_people[i-1]
        # Otherwise, the HR person in charge of the firing and hiring on the current day
        # is the next HR person in the sequence
        else:
            hr_people[i] = (hr_people[i-1] + 1) % k
            k += 1
    return k, hr_people

