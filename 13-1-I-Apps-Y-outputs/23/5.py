
def solve(N, X, moto_needed):
    # Sort the list of moto needed in descending order
    moto_needed.sort(reverse=True)
    # Initialize the number of doughnuts that can be made to 0
    doughnuts_made = 0
    # Loop through the list of moto needed and check if the current amount of moto is greater than or equal to the amount needed for the current doughnut
    for i in range(N):
        if X >= moto_needed[i]:
            # If it is, increment the number of doughnuts made and subtract the amount of moto needed for the current doughnut from the total amount of moto
            doughnuts_made += 1
            X -= moto_needed[i]
    # Return the number of doughnuts that can be made
    return doughnuts_made

