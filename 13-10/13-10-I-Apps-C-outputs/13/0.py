
import itertools

def get_combinations(n, a, p):
    combinations = []
    for combination in itertools.combinations(a, n):
        if sum(combination) <= p:
            combinations.append(combination)
    return combinations

def get_average_number_of_visitors(n, a, p):
    combinations = get_combinations(n, a, p)
    return sum([len(combination) for combination in combinations]) / len(combinations)

def main():
    n, a, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_average_number_of_visitors(n, a, p))

if __name__ == '__main__':
    main()

