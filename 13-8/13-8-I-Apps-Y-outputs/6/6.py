
def construct_binary_string(a, b, x):
    n = a + b
    s = ["0"] * n
    for i in range(x):
        while s[i] == s[i + 1]:
            s[i] = "1" if s[i] == "0" else "0"
    return "".join(s)

def main():
    a, b, x = map(int, input().split())
    print(construct_binary_string(a, b, x))

if __name__ == '__main__':
    main()

