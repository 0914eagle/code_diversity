
def longest_alternating_subsequence(string):
    # Initialize variables
    n = len(string)
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    
    # Compute the length of the longest alternating subsequence
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if string[i - 1] != string[j - 1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
    
    # Backtrack to find the longest alternating subsequence
    longest = 0
    start = 0
    end = 0
    i = n
    while i != 0:
        if dp[i] > longest:
            longest = dp[i]
            start = prev[i]
            end = i
        i = prev[i]
    
    return longest

def main():
    n = int(input())
    string = input()
    print(longest_alternating_subsequence(string))

if __name__ == '__main__':
    main()

