
def get_minimum_problems(c, d, n, m, k):
    # Calculate the total number of people that need to go to the finals
    total_people = n * m
    
    # Calculate the number of problems needed for the main rounds
    main_rounds = total_people // c
    main_problems = main_rounds * c
    
    # Calculate the number of problems needed for the additional rounds
    additional_rounds = total_people - main_rounds
    additional_problems = additional_rounds * d
    
    # Calculate the total number of problems needed
    total_problems = main_problems + additional_problems
    
    # Return the minimum number of problems needed
    return total_problems

def main():
    c, d, n, m, k = map(int, input().split())
    print(get_minimum_problems(c, d, n, m, k))

if __name__ == '__main__':
    main()

