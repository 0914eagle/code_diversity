
def get_consecutive_subsequences(prices, P):
    # find all consecutive subsequences in the last N days
    consecutive_subsequences = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            consecutive_subsequences.append(prices[i:j+1])
    
    # count the number of consecutive subsequences with average price greater than or equal to P
    count = 0
    for subsequence in consecutive_subsequences:
        if sum(subsequence) / len(subsequence) >= P:
            count += 1
    
    return count

def main():
    N = int(input())
    prices = list(map(int, input().split()))
    P = int(input())
    print(get_consecutive_subsequences(prices, P))

if __name__ == '__main__':
    main()

