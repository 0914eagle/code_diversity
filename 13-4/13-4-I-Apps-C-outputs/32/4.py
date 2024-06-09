
def get_correct_times(original_time, current_time):
    original_hour, original_minute = map(int, original_time.split(':'))
    current_hour, current_minute = map(int, current_time.split(':'))
    
    correct_times = []
    for hour in range(0, 24):
        for minute in range(0, 60):
            if hour == original_hour and minute == original_minute:
                continue
            if hour == current_hour and minute == current_minute:
                continue
            correct_times.append(f"{hour:02d}:{minute:02d}")
    
    return len(correct_times), *correct_times

def main():
    original_time, current_time = input().split()
    num_correct_times, *correct_times = get_correct_times(original_time, current_time)
    print(num_correct_times)
    for correct_time in correct_times:
        print(correct_time)

if __name__ == '__main__':
    main()

