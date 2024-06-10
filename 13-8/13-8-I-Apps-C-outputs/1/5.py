
def get_surprise_penalty(dates):
    # Calculate the surprise penalty for the given dates
    penalty = 0
    for i in range(len(dates) - 1):
        x = dates[i + 1]
        y = dates[i]
        penalty += (x - y) ** 2
    return penalty

def get_optimal_schedule(z, f, forbidden_dates):
    # Initialize the optimal schedule as the first day of October in each year
    optimal_schedule = [10, 1, 2019]
    for i in range(1, z):
        year = 2019 + i
        # Find the first day in October that is not a forbidden date
        for j in range(1, 32):
            date = [year, 10, j]
            if date not in forbidden_dates:
                optimal_schedule.append(date)
                break
    return optimal_schedule

def main():
    z = int(input())
    f = int(input())
    forbidden_dates = []
    for i in range(f):
        year, month, day = map(int, input().split())
        forbidden_dates.append([year, month, day])
    optimal_schedule = get_optimal_schedule(z, f, forbidden_dates)
    surprise_penalty = get_surprise_penalty(optimal_schedule)
    print(surprise_penalty)
    for date in optimal_schedule:
        print(" ".join(map(str, date)))

if __name__ == '__main__':
    main()

