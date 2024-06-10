
def get_chaos(passengers, bomb_order):
    
    # Calculate the chaos in each coach
    chaos = [round_up_to_nearest_multiple_of_10(passengers[i]) for i in bomb_order]

    # Calculate the total chaos
    total_chaos = sum(chaos)

    return total_chaos

def round_up_to_nearest_multiple_of_10(n):
    
    return int(10 * (n // 10 + 1))

def main():
    # Read the input
    num_coaches, passengers, bomb_order = read_input()

    # Calculate the maximum chaos
    max_chaos = get_chaos(passengers, bomb_order)

    # Print the output
    print(max_chaos)

def read_input():
    
    num_coaches = int(input())
    passengers = list(map(int, input().split()))
    bomb_order = list(map(int, input().split()))
    return num_coaches, passengers, bomb_order

if __name__ == '__main__':
    main()

