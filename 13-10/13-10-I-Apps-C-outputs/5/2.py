
def get_strengths(n):
    return list(map(int, input().split()))

def get_supporting_stewards(n, strengths):
    supporting_stewards = 0
    for i in range(n):
        if any(strengths[i] < strengths[j] and strengths[i] > strengths[j] for j in range(n) if j != i):
            supporting_stewards += 1
    return supporting_stewards

def main():
    n = int(input())
    strengths = get_strengths(n)
    print(get_supporting_stewards(n, strengths))

if __name__ == '__main__':
    main()

