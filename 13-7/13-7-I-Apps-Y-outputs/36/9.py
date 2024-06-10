
def get_longest_increasing_sequence(a):
    n = len(a)
    if n == 1:
        return 1, "R"
    
    # Initialize dp table with all -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Loop through all elements of the array
    for i in range(1, n + 1):
        # Find the maximum length ending with the current element
        max_len = 0
        for j in range(i):
            if a[i - 1] > a[j] and dp[j] > max_len:
                max_len = dp[j]
        dp[i] = max_len + 1
    
    # Find the maximum length among all elements
    max_len = 0
    for i in range(n + 1):
        if dp[i] > max_len:
            max_len = dp[i]
    
    # Backtrack to find the sequence
    seq = []
    i = n
    while i > 0:
        if dp[i] != dp[i - 1]:
            seq.append("L" if a[i - 1] < a[i] else "R")
        i -= 1
    
    return max_len, "".join(seq[::-1])

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_longest_increasing_sequence(a))

if __name__ == '__main__':
    main()

