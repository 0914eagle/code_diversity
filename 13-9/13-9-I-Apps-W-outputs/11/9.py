
def get_min_problems(c, d, n, m, k):
    # Calculate the total number of winners in the main and additional rounds
    total_winners = n * m + k
    
    # Calculate the minimum number of problems needed to prepare
    min_problems = c * n + d * (total_winners - n)
    
    return min_problems

def main():
    c, d, n, m, k = map(int, input().split())
    print(get_min_problems(c, d, n, m, k))

if __name__ == '__main__':
    main()

