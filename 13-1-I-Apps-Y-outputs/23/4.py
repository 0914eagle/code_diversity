
def solve(N, X, moto_needed):
    # Sort the list of moto needed in descending order
    moto_needed.sort(reverse=True)
    # Initialize the number of doughnuts that can be made to 0
    doughnuts_made = 0
    # Loop through the list of moto needed and try to make doughnuts
    for i in range(N):
        # Check if there is enough moto to make at least one doughnut
        if X >= moto_needed[i]:
            # Calculate the number of doughnuts that can be made with the current amount of moto
            doughnuts_made += X // moto_needed[i]
            # Subtract the amount of moto used to make the doughnuts from the total amount of moto
            X -= (X // moto_needed[i]) * moto_needed[i]
    # Return the maximum number of doughnuts that can be made
    return doughnuts_made

