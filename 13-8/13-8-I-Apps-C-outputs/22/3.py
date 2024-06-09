
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice with the first friend
    optimal_choice = [probabilities[0]]
    # Iterate over the remaining friends
    for i in range(1, n):
        # Calculate the probability that Andrey will get upset if he chooses this friend
        upset_probability = 1 - probabilities[i]
        # Calculate the probability that Andrey will get exactly one problem if he chooses this friend and the current optimal choice
        one_problem_probability = optimal_choice[0] * probabilities[i]
        # If the probability of getting exactly one problem is greater than the probability of getting upset, add this friend to the optimal choice
        if one_problem_probability > upset_probability:
            optimal_choice.append(probabilities[i])
    # Return the probability of Andrey not getting upset at the optimal choice of friends
    return sum(optimal_choice)

