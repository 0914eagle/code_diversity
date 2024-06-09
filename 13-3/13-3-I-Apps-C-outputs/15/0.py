
def solve(a):
    # Convert the input string to a list of digits
    digits = [int(digit) for digit in str(a)]
    
    # Create a list to store the permutations
    permutations = []
    
    # Iterate over the digits and create all possible permutations
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            permutations.append(digits[i] * 1000 + digits[j] * 100 + digits[i] * 10 + digits[j])
    
    # Iterate over the permutations and check if they are divisible by 7
    for permutation in permutations:
        if permutation % 7 == 0:
            return str(permutation)
    
    # If no permutation is divisible by 7, return 0
    return "0"

