
def get_chaos(coach_passengers, coach_order):
    
    # Calculate the chaos in each coach
    coach_chaos = [round_up_to_nearest_multiple_of_10(passengers) for passengers in coach_passengers]
    
    # Calculate the total chaos by summing the chaos of each coach
    total_chaos = sum(coach_chaos)
    
    # If the coaches were blown up in a specific order, calculate the maximum chaos by finding the largest sum of chaos among all possible combinations of coaches
    if coach_order:
        max_chaos = 0
        for combination in itertools.combinations(coach_chaos, len(coach_order)):
            max_chaos = max(max_chaos, sum(combination))
        total_chaos = max_chaos
    
    return total_chaos

def round_up_to_nearest_multiple_of_10(n):
    
    return int(math.ceil(n / 10.0)) * 10

if __name__ == '__main__':
    n = int(input())
    coach_passengers = list(map(int, input().split()))
    coach_order = list(map(int, input().split()))
    print(get_chaos(coach_passengers, coach_order))

