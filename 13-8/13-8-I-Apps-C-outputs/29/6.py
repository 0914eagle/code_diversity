
def get_smallest_T(preference_lists):
    # Initialize the variable T to be the maximum size of the preference lists
    T = len(preference_lists[0])
    # Iterate through each preference list
    for preference_list in preference_lists:
        # Check if the size of the preference list is smaller than T
        if len(preference_list) < T:
            # If so, update the value of T
            T = len(preference_list)
    # Return the value of T
    return T

