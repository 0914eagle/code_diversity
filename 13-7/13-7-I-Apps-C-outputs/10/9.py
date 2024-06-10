
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def get_output(N, a, b):
    candy = []
    for i in range(N):
        if a[i] > b[i]:
            candy.append("A")
        elif a[i] < b[i]:
            candy.append("B")
        else:
            candy.append("A" if i % 2 == 0 else "B")
    return "".join(candy)

def main():
    N, a, b = get_input()
    print(get_output(N, a, b))

if __name__ == '__main__':
    main()

