
def get_chaos(num_coaches, passengers_per_coach, coach_order):
    total_chaos = 0
    for coach in coach_order:
        num_passengers = passengers_per_coach[coach - 1]
        chaos = (num_passengers // 10 + 1) * 10
        total_chaos += chaos
    return total_chaos

def get_max_chaos(num_coaches, passengers_per_coach, coach_order):
    max_chaos = 0
    for perm in itertools.permutations(coach_order):
        chaos = get_chaos(num_coaches, passengers_per_coach, perm)
        if chaos > max_chaos:
            max_chaos = chaos
    return max_chaos

if __name__ == '__main__':
    num_coaches = int(input())
    passengers_per_coach = list(map(int, input().split()))
    coach_order = list(map(int, input().split()))
    print(get_max_chaos(num_coaches, passengers_per_coach, coach_order))

