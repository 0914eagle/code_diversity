
def get_binary_string(a, b, x):
    n = a + b
    s = ""
    for i in range(n):
        if i < a:
            s += "0"
        elif i < n - b:
            s += "1"
        else:
            s += "0"
    for i in range(x):
        s = s[:i] + "1" + s[i + 1:]
    return s

def main():
    a, b, x = map(int, input().split())
    s = get_binary_string(a, b, x)
    print(s)

if __name__ == '__main__':
    main()

