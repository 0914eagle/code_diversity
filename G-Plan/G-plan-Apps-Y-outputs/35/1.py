
def parse_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours, minutes, seconds

def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def time_difference(current_time, explosion_time):
    current_hours, current_minutes, current_seconds = parse_time(current_time)
    explosion_hours, explosion_minutes, explosion_seconds = parse_time(explosion_time)

    current_total_seconds = total_seconds(current_hours, current_minutes, current_seconds)
    explosion_total_seconds = total_seconds(explosion_hours, explosion_minutes, explosion_seconds)

    if explosion_total_seconds < current_total_seconds:
        explosion_total_seconds += 24 * 3600

    diff_seconds = explosion_total_seconds - current_total_seconds

    return diff_seconds // 3600, (diff_seconds % 3600) // 60, diff_seconds % 60

if __name__ == '__main__':
    current_time = input().strip()
    explosion_time = input().strip()

    result = time_difference(current_time, explosion_time)
    print(f'{result[0]:02d}:{result[1]:02d}:{result[2]:02d}')
