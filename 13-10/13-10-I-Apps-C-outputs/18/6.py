
def get_remainders(n, k, c):
    # Function to get the remainders of x after dividing by c
    remainders = []
    for i in range(n):
        remainders.append(x % c[i])
    return remainders

def check_strategy(k, c):
    # Function to check if Arya has a winning strategy
    n = len(c)
    remainders = get_remainders(n, k, c)
    for i in range(n):
        if remainders[i] != 0:
            continue
        else:
            return "No"
    return "Yes"

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print(check_strategy(k, c))

if __name__ == '__main__':
    main()

