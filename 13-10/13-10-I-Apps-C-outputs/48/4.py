
def rearrange_strings(S):
    N = len(S)
    if N % 2 == 1 or N > 10000:
        return "-1"
    
    substrings = []
    for i in range(N // 2):
        substrings.append(S[i:i + N // 2])
    
    seen = set()
    for substring in substrings:
        if substring in seen:
            return "-1"
        seen.add(substring)
    
    permutation = []
    for i in range(N // 2):
        permutation.append(substrings[i])
    
    return "".join(permutation)

def main():
    S = input()
    print(rearrange_strings(S))

if __name__ == '__main__':
    main()

