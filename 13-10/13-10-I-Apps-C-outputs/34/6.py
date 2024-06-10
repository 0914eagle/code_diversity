
def get_palindromic_strings(s):
    n = len(s)
    palindromic_strings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromic_strings.append(substr)
    return palindromic_strings

def count_palindromic_strings(s, n):
    palindromic_strings = get_palindromic_strings(s)
    count = 0
    for string in palindromic_strings:
        if len(string) == n:
            count += 1
    return count

def main():
    n = int(input())
    s = input()
    print(count_palindromic_strings(s, 2*n))

if __name__ == '__main__':
    main()

