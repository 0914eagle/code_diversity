
def get_minimum_problems(c, d, n, m, k):
    # Calculate the total number of winners
    total_winners = n * m + k
    
    # Calculate the minimum number of problems needed to ensure at least total_winners people go to the finals
    minimum_problems = total_winners * (c + d)
    
    return minimum_problems

def main():
    c, d, n, m, k = map(int, input().split())
    print(get_minimum_problems(c, d, n, m, k))

if __name__ == '__main__':
    main()

