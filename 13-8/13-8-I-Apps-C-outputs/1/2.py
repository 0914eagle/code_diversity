
import itertools

def get_surprise_penalty(schedule):
    penalty = 0
    for i in range(len(schedule) - 1):
        penalty += (schedule[i + 1] - schedule[i]) ** 2
    return penalty

def is_valid_schedule(schedule, forbidden_dates):
    for date in schedule:
        if date in forbidden_dates:
            return False
    return True

def get_best_schedule(forbidden_dates, years):
    all_dates = []
    for year in range(2019, 2018 + years + 1):
        for day in range(1, 32):
            all_dates.append((year, 10, day))
    
    best_schedule = []
    best_penalty = float('inf')
    
    for schedule in itertools.permutations(all_dates):
        if is_valid_schedule(schedule, forbidden_dates):
            penalty = get_surprise_penalty(schedule)
            if penalty < best_penalty:
                best_penalty = penalty
                best_schedule = schedule
    
    return best_schedule

def main():
    years = int(input())
    forbidden_dates = []
    num_forbidden_dates = int(input())
    for _ in range(num_forbidden_dates):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    
    schedule = get_best_schedule(forbidden_dates, years)
    print(get_surprise_penalty(schedule))
    for date in schedule:
        print(' '.join(map(str, date)))

if __name__ == '__main__':
    main()

