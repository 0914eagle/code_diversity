
def find_min_total_stamina(X):
    # Sort the input array in ascending order
    X.sort()
    # Initialize the minimum total stamina to 0
    min_total_stamina = 0
    # Loop through the input array and calculate the total stamina for each meeting point
    for i in range(len(X)):
        total_stamina = 0
        for j in range(len(X)):
            total_stamina += (X[j] - X[i]) ** 2
        # If the total stamina for the current meeting point is less than the minimum total stamina, update the minimum total stamina
        if total_stamina < min_total_stamina or min_total_stamina == 0:
            min_total_stamina = total_stamina
    return min_total_stamina

