
def get_smallest_t(preference_list):
    # Initialize variables
    T = 0
    classes = []

    # Iterate through the preference list
    for i in range(len(preference_list)):
        # Get the current kid's preference list
        current_kid_preference_list = preference_list[i]

        # Find the index of the first kid in the preference list who is not in the same class as the current kid
        for j in range(len(current_kid_preference_list)):
            if current_kid_preference_list[j] not in classes[i]:
                T = max(T, j)
                break

    return T

