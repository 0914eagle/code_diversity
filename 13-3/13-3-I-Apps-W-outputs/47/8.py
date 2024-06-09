
def count_ways(X, N, cars):
    total_ways = 0
    for car in cars:
        free_places = [i for i, p in enumerate(car, 1) if p == "0"]
        free_compartments = [free_places[i-1:i+5] for i in range(1, len(free_places), 6)]
        for compartment in free_compartments:
            if len(compartment) >= X:
                total_ways += 1
    return total_ways

def main():
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways(X, N, cars))

if __name__ == '__main__':
    main()

