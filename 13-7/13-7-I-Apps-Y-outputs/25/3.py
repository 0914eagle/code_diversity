
def get_probability(n):
    total = 0
    odd = 0
    for i in range(1, n+1):
        total += 1
        if i % 2 == 1:
            odd += 1
    return odd / total

def main():
    n = int(input())
    print(get_probability(n))

if __name__ == '__main__':
    main()

