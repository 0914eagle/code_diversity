
def quasibinary(n):
    # Initialize an empty list to store the quasibinary numbers
    quasibinary_nums = []
    # Loop until the sum of the quasibinary numbers is equal to n
    while sum(quasibinary_nums) < n:
        # Append the largest quasibinary number that is less than or equal to n to the list
        quasibinary_nums.append(min(i for i in range(1, n+1) if i <= n and str(i)[:1] in "01"))
    # Return the list of quasibinary numbers
    return quasibinary_nums

