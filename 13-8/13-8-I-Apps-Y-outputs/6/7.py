
def get_binary_string(a, b, x):
    n = a + b
    s = ["0"] * n
    s[0] = "1"
    for i in range(1, n):
        if s[i - 1] == "0":
            s[i] = "1"
        else:
            s[i] = "0"
    for i in range(x):
        while s[i] == s[i - 1]:
            s[i] = "1" if s[i] == "0" else "0"
    return "".join(s)

def main():
    a, b, x = map(int, input().split())
    print(get_binary_string(a, b, x))

if __name__ == '__main__':
    main()

