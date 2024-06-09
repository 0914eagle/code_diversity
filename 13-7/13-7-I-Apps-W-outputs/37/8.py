
def solve(n, k, a, b):
    # Calculate the total taste and total calories of the fruits
    total_taste = sum(a)
    total_calories = sum(b)
    
    # Initialize the maximum possible sum of the taste values of the chosen fruits
    max_taste = 0
    
    # Iterate through all possible combinations of fruits
    for i in range(1, 2**n):
        # Calculate the current combination of fruits
        curr_combination = []
        for j in range(n):
            if i & (1 << j):
                curr_combination.append(j)
                
        # Calculate the total taste and total calories of the current combination of fruits
        curr_taste = sum(a[i] for i in curr_combination)
        curr_calories = sum(b[i] for i in curr_combination)
        
        # Check if the current combination of fruits fulfills Inna's principle
        if curr_taste * total_calories == k * curr_calories:
            # Update the maximum possible sum of the taste values of the chosen fruits
            max_taste = max(max_taste, curr_taste)
    
    # Return the maximum possible sum of the taste values of the chosen fruits
    return max_taste if max_taste != 0 else -1

