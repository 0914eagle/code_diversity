
def solve():
    N = int(input())
    T = input()
    
    # Concatenate 10^10 copies of the string 110
    S = "110" * (10**10)
    
    # Count the number of times T occurs in S as a contiguous substring
    count = 0
    for i in range(len(S) - len(T) + 1):
        if S[i:i+len(T)] == T:
            count += 1
    
    return count

