
def solve(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a dictionary to store the frequency of each substring
    freq = {}
    for i in range(n // 2):
        substr = s[i:i + n // 2]
        if substr not in freq:
            freq[substr] = 1
        else:
            freq[substr] += 1
    
    # if there is a substring with frequency greater than 1, it is not possible to rearrange the string
    for val in freq.values():
        if val > 1:
            return "-1"
    
    # if all substrings are unique, return the original string
    return s

def main():
    s = input()
    print(solve(s))

if __name__ == '__main__':
    main()

