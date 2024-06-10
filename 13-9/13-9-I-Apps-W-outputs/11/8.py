
def get_min_problems(c, d, n, m, k):
    # Calculate the total number of winners
    total_winners = n * m + k
    
    # Calculate the minimum number of problems needed
    min_problems = 0
    while total_winners > 0:
        if total_winners >= c:
            min_problems += c
            total_winners -= c
        else:
            min_problems += total_winners
            total_winners = 0
    
    # If there are any additional rounds, calculate the minimum number of problems needed for them
    if d > 0:
        min_problems += d * (m - 1)
    
    return min_problems

def main():
    c, d, n, m, k = map(int, input().split())
    print(get_min_problems(c, d, n, m, k))

if __name__ == '__main__':
    main()

