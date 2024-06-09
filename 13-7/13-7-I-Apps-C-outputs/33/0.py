
import math

def get_average_number_of_visitors(n, a, p):
    # Calculate the sum of all possible permutations of the guests
    sum_of_permutations = math.factorial(n)
    
    # Initialize a list to store the number of visitors for each permutation
    num_visitors = []
    
    # Iterate over all possible permutations of the guests
    for perm in permutations(a):
        # Initialize a variable to store the number of visitors for this permutation
        num_visitors_for_this_perm = 0
        
        # Iterate over the guests in this permutation
        for i in range(n):
            # Check if the sum of the sizes of the guests in the restaurant plus the size of the current guest is less than or equal to the table length
            if sum(perm[:i+1]) <= p:
                # If it is, add the current guest to the restaurant
                num_visitors_for_this_perm += 1
            else:
                # If it is not, break the loop and move on to the next permutation
                break
        
        # Add the number of visitors for this permutation to the list
        num_visitors.append(num_visitors_for_this_perm)
    
    # Calculate the average number of visitors by dividing the sum of all permutations by the number of permutations
    average_number_of_visitors = sum(num_visitors) / sum_of_permutations
    
    return average_number_of_visitors

# Define a function to generate all permutations of a list
def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]
    permutations_list = []
    for i in range(len(my_list)):
        remaining_list = my_list[:i] + my_list[i+1:]
        for p in permutations(remaining_list):
            permutations_list.append([my_list[i]] + p)
    return permutations_list

n = int(input())
a = list(map(int, input().split()))
p = int(input())

print(get_average_number_of_visitors(n, a, p))

