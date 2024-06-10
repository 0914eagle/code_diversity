
def get_min_operations(s):
    n = len(s)
    if n == 0:
        return 0
    
    # Initialize a list to store the length of the longest prefix that is also a suffix
    lps = [0] * n
    
    # Compute the length of the longest prefix that is also a suffix
    compute_lps(s, lps)
    
    # Return the minimum number of operations required to delete the string
    return n - lps[n-1]

def compute_lps(s, lps):
    n = len(s)
    lps[0] = 0
    i = 1
    l = 0
    while i < n:
        if s[i] == s[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l-1]

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_min_operations(s))

