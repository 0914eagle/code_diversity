
def construct_binary_string(a, b, x):
    n = a + b
    s = ""
    for i in range(n):
        if i < a:
            s += "0"
        elif i < a + b:
            s += "1"
    for i in range(x):
        i1 = i % n
        i2 = (i1 + 1) % n
        if s[i1] == s[i2]:
            s = s[:i1] + "0" + s[i1+1:]
    return s

def main():
    a, b, x = map(int, input().split())
    print(construct_binary_string(a, b, x))

if __name__ == '__main__':
    main()

