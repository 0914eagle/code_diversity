
def check_remainders(n, k):
    remainders = []
    for i in range(1, k+1):
        remainders.append(n%i)
    return len(set(remainders)) == len(remainders)

def main():
    n, k = map(int, input().split())
    if check_remainders(n, k):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

