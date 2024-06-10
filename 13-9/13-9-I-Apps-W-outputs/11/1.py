
def get_min_problems(c, d, n, m, k):
    # Calculate the total number of winners needed in all rounds
    total_winners = n * m + k
    
    # Calculate the minimum number of problems needed in the main rounds
    min_main_problems = total_winners // n
    
    # Calculate the minimum number of problems needed in the additional rounds
    min_add_problems = total_winners - min_main_problems * n
    
    # Return the minimum number of problems needed in all rounds
    return min_main_problems * c + min_add_problems * d

def main():
    c, d, n, m, k = map(int, input().split())
    print(get_min_problems(c, d, n, m, k))

if __name__ == '__main__':
    main()

