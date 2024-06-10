
def get_remainders(n, k):
    remainders = []
    for i in range(1, k+1):
        remainders.append(n % i)
    return remainders

def check_distinct(remainders):
    for i in range(len(remainders)):
        for j in range(i+1, len(remainders)):
            if remainders[i] == remainders[j]:
                return "No"
    return "Yes"

def main():
    n, k = map(int, input().split())
    remainders = get_remainders(n, k)
    print(check_distinct(remainders))

if __name__ == '__main__':
    main()

