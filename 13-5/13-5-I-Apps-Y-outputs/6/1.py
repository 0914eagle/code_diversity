
def get_binary_string(a, b, x):
    n = a + b
    s = ""
    for i in range(n):
        if i % 2 == 0:
            s += "0"
        else:
            s += "1"
    for i in range(x):
        ind = i % n
        if s[ind] == "0":
            s = s[:ind] + "1" + s[ind+1:]
        else:
            s = s[:ind] + "0" + s[ind+1:]
    return s

def main():
    a, b, x = map(int, input().split())
    print(get_binary_string(a, b, x))

if __name__ == '__main__':
    main()

