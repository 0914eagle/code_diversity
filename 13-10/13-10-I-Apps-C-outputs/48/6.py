
def get_substrings(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]

def rearrange_string(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    substrings = get_substrings(s, n//2)
    seen = set()
    for substring in substrings:
        if substring in seen:
            return "-1"
        seen.add(substring)
    
    return "".join(sorted(s))

def main():
    s = input("Enter a string: ")
    print(rearrange_string(s))

if __name__ == '__main__':
    main()

