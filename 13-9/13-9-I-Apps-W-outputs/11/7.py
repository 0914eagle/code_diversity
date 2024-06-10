
def get_min_problems(c, d, n, m, k):
    # Calculate the total number of problems needed in all rounds
    total_problems = c * m + d * (m - 1) + k
    
    # Calculate the minimum number of problems needed in each round
    min_problems = total_problems // m
    
    # Return the minimum number of problems needed in all rounds
    return min_problems

def get_main_elimination_rounds(c, m, n):
    # Calculate the number of main elimination rounds needed
    main_rounds = n // c
    
    # Calculate the number of additional elimination rounds needed
    additional_rounds = n % c
    
    # Return the number of main elimination rounds and additional elimination rounds needed
    return main_rounds, additional_rounds

def get_additional_elimination_rounds(d, m, n):
    # Calculate the number of additional elimination rounds needed
    additional_rounds = n // d
    
    # Calculate the number of main elimination rounds needed
    main_rounds = n % d
    
    # Return the number of additional elimination rounds and main elimination rounds needed
    return additional_rounds, main_rounds

def get_total_problems(c, d, m, n, k):
    # Calculate the number of main elimination rounds and additional elimination rounds needed
    main_rounds, additional_rounds = get_main_elimination_rounds(c, m, n)
    additional_rounds, main_rounds = get_additional_elimination_rounds(d, m, n)
    
    # Calculate the total number of problems needed in all rounds
    total_problems = c * main_rounds * m + d * additional_rounds * m + k
    
    # Return the total number of problems needed in all rounds
    return total_problems

def get_min_problems(c, d, m, n, k):
    # Calculate the total number of problems needed in all rounds
    total_problems = get_total_problems(c, d, m, n, k)
    
    # Calculate the minimum number of problems needed in each round
    min_problems = total_problems // m
    
    # Return the minimum number of problems needed in all rounds
    return min_problems

if __name__ == '__main__':
    c, d, n, m, k = map(int, input().split())
    print(get_min_problems(c, d, n, m, k))

