
def find_binary_string(a, b, x):
    n = a + b
    s = ""
    for i in range(n):
        if i < a:
            s += "0"
        elif i < a + b:
            s += "1"
        else:
            break
    indices = set()
    while len(indices) < x:
        i = randint(1, n - 1)
        if i not in indices:
            indices.add(i)
    for i in indices:
        if s[i] == s[i - 1]:
            s = s[:i] + "0" + s[i + 1:]
        else:
            s = s[:i] + "1" + s[i + 1:]
    return s

def main():
    a, b, x = map(int, input().split())
    s = find_binary_string(a, b, x)
    print(s)

if __name__ == '__main__':
    main()

