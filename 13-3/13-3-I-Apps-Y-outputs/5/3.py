
def is_sorted(s):
    return s == ''.join(sorted(s))

def get_coloring(s):
    n = len(s)
    coloring = [0] * n
    for i in range(n):
        if s[i] in s[:i] or s[i] in s[i+1:]:
            coloring[i] = 1
    return ''.join(map(str, coloring))

def main():
    n = int(input())
    s = input()
    if is_sorted(s):
        print("YES")
        print(get_coloring(s))
    else:
        print("NO")

if __name__ == "__main__":
    main()

