
def rearrange_strings(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    substrings = []
    for i in range(n // 2):
        substrings.append(s[i:i + n // 2])
    
    seen = set()
    for substring in substrings:
        if substring in seen:
            return "-1"
        seen.add(substring)
    
    permutation = ""
    for i in range(n // 2):
        permutation += substrings[i]
    
    return permutation

def main():
    s = input("Enter a string: ")
    print(rearrange_strings(s))

if __name__ == '__main__':
    main()

