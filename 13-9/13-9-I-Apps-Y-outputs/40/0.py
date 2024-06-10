
def cut_string(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            x = s[:i]
            y = s[i:j]
            count = max(count, len(set(x+y)))
    return count

def main():
    n = int(input())
    s = input()
    print(cut_string(s))

if __name__ == '__main__':
    main()

