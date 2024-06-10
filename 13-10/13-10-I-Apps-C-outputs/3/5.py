
def get_chaos(coaches, order):
    # Initialize variables
    total_chaos = 0
    coach_passengers = [0] * len(coaches)

    # Calculate the total number of passengers in each coach
    for i in range(len(coaches)):
        coach_passengers[i] = coaches[i]

    # Calculate the total chaos for each coach
    for i in range(len(coaches)):
        coach_chaos = coach_passengers[i] - coach_passengers[i] % 10
        total_chaos += coach_chaos

    # Calculate the total chaos for the entire train
    total_chaos *= len(coaches)

    # Calculate the chaos for each coach based on the order they were blown up
    for i in range(len(order)):
        coach_chaos = coach_passengers[order[i] - 1] - coach_passengers[order[i] - 1] % 10
        total_chaos -= coach_chaos

    return total_chaos

def main():
    n = int(input())
    coaches = list(map(int, input().split()))
    order = list(map(int, input().split()))
    print(get_chaos(coaches, order))

if __name__ == '__main__':
    main()

