
def get_min_problems(c, d, n, m, k):
    # Initialize variables
    total_winners = n*m + k
    main_rounds = 0
    additional_rounds = 0
    problems_per_round = c
    
    # Calculate the number of main and additional rounds needed
    while total_winners > 0:
        if total_winners > n:
            main_rounds += 1
            total_winners -= n
        else:
            additional_rounds += 1
            total_winners -= 1
    
    # Calculate the total number of problems needed
    total_problems = main_rounds*c + additional_rounds*d
    
    return total_problems

def get_min_problems_optimized(c, d, n, m, k):
    # Initialize variables
    total_winners = n*m + k
    main_rounds = 0
    additional_rounds = 0
    problems_per_round = c
    
    # Calculate the number of main and additional rounds needed
    while total_winners > 0:
        if total_winners > n:
            main_rounds += 1
            total_winners -= n
        else:
            additional_rounds += 1
            total_winners -= 1
    
    # Calculate the total number of problems needed
    total_problems = main_rounds*c + additional_rounds*d
    
    # Optimize the number of problems by removing unnecessary rounds
    if main_rounds > 0 and additional_rounds > 0:
        total_problems -= c
    
    return total_problems

if __name__ == '__main__':
    c, d, n, m, k = map(int, input().split())
    print(get_min_problems(c, d, n, m, k))
    print(get_min_problems_optimized(c, d, n, m, k))

