
def get_binary_string(a, b, x):
    n = a + b
    s = ["0"] * n
    for i in range(n):
        if s[i] == "0":
            s[i] = "1"
            a -= 1
        if a == 0 and b == 0:
            break
    for i in range(n):
        if s[i] == "1":
            s[i] = "0"
            b -= 1
        if a == 0 and b == 0:
            break
    for i in range(n):
        if s[i] == "0":
            s[i] = "1"
            x -= 1
        if x == 0:
            break
    return "".join(s)

def main():
    a, b, x = map(int, input().split())
    print(get_binary_string(a, b, x))

if __name__ == '__main__':
    main()

