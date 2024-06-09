
def get_candy_values(N, a, b):
    candy_values = []
    for i in range(N):
        candy_values.append((a[i], b[i]))
    return candy_values

def get_optimal_distribution(candy_values):
    alf_candy_values = []
    beata_candy_values = []
    for candy in candy_values:
        if candy[0] > candy[1]:
            alf_candy_values.append(candy)
        else:
            beata_candy_values.append(candy)
    return alf_candy_values, beata_candy_values

def get_distribution_string(candy_values):
    distribution_string = ""
    for candy in candy_values:
        if candy[0] > candy[1]:
            distribution_string += "A"
        else:
            distribution_string += "B"
    return distribution_string

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    candy_values = get_candy_values(N, a, b)
    alf_candy_values, beata_candy_values = get_optimal_distribution(candy_values)
    distribution_string = get_distribution_string(alf_candy_values + beata_candy_values)
    print(distribution_string)

if __name__ == '__main__':
    main()

