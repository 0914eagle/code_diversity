
def get_min_problems(c, d, n, m, k):
    # Calculate the total number of participants in the finals
    total_participants = n*m + k
    
    # Calculate the number of problems needed in the main rounds
    main_rounds_problems = c*n
    
    # Calculate the number of problems needed in the additional rounds
    additional_rounds_problems = d*m
    
    # Calculate the total number of problems needed
    total_problems = main_rounds_problems + additional_rounds_problems
    
    # Return the minimum number of problems needed
    return total_problems

def get_main_rounds(c, n):
    # Calculate the number of main rounds needed
    main_rounds = n//c
    
    # Return the number of main rounds needed
    return main_rounds

def get_additional_rounds(d, m):
    # Calculate the number of additional rounds needed
    additional_rounds = m//d
    
    # Return the number of additional rounds needed
    return additional_rounds

if __name__ == '__main__':
    c, d, n, m, k = map(int, input().split())
    total_problems = get_min_problems(c, d, n, m, k)
    main_rounds = get_main_rounds(c, n)
    additional_rounds = get_additional_rounds(d, m)
    print(total_problems)

