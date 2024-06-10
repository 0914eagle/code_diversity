
def get_remainders(n, k):
    remainders = []
    for i in range(1, k+1):
        remainders.append(n % i)
    return remainders

def are_remainders_distinct(remainders):
    for i in range(len(remainders)):
        for j in range(i+1, len(remainders)):
            if remainders[i] == remainders[j]:
                return False
    return True

def main():
    n, k = map(int, input().split())
    remainders = get_remainders(n, k)
    if are_remainders_distinct(remainders):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

