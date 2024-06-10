
def construct_binary_string(a, b, x):
    n = a + b
    s = ""
    for i in range(n):
        if i % 2 == 0:
            s += "0"
        else:
            s += "1"
    for i in range(x):
        index = i + 1
        if index < n:
            s = s[:index] + "0" + s[index:]
    return s

def main():
    a, b, x = map(int, input().split())
    print(construct_binary_string(a, b, x))

if __name__ == '__main__':
    main()

