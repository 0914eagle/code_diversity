
def get_chaos_per_coach(coach_passengers):
    return (coach_passengers // 10 + 1) * 10

def get_chaos_per_segment(segment_passengers):
    return sum(get_chaos_per_coach(coach_passengers) for coach_passengers in segment_passengers)

def get_maximum_chaos(number_of_coaches, coach_passengers, permutation):
    segments = [coach_passengers[permutation[i]-1] for i in range(number_of_coaches)]
    return get_chaos_per_segment(segments)

def main():
    number_of_coaches = int(input())
    coach_passengers = list(map(int, input().split()))
    permutation = list(map(int, input().split()))
    print(get_maximum_chaos(number_of_coaches, coach_passengers, permutation))

if __name__ == '__main__':
    main()

