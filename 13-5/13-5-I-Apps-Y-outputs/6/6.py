
def get_binary_string(a, b, x):
    n = a + b
    s = ["0"] * n
    for i in range(x):
        s[i] = "1"
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            s[i + 1] = "1" if s[i] == "0" else "0"
    return "".join(s)

def main():
    a, b, x = map(int, input().split())
    print(get_binary_string(a, b, x))

if __name__ == '__main__':
    main()

