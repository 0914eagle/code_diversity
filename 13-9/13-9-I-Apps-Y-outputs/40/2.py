
def get_max_different_letters(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            x = s[i:j]
            y = s[j:n] + s[:i]
            count = max(count, len(set(x) & set(y)))
    return count

def main():
    n = int(input())
    s = input()
    print(get_max_different_letters(s))

if __name__ == '__main__':
    main()

