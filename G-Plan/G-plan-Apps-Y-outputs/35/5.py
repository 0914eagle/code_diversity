
def parse_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours, minutes, seconds

def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def convert_to_time_format(total_seconds):
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def calculate_time_to_explosion(current_time, explosion_time):
    current_hours, current_minutes, current_seconds = parse_time(current_time)
    explosion_hours, explosion_minutes, explosion_seconds = parse_time(explosion_time)

    current_total_seconds = convert_to_seconds(current_hours, current_minutes, current_seconds)
    explosion_total_seconds = convert_to_seconds(explosion_hours, explosion_minutes, explosion_seconds)

    if explosion_total_seconds < current_total_seconds:
        explosion_total_seconds += 24 * 3600

    time_difference = explosion_total_seconds - current_total_seconds

    return convert_to_time_format(time_difference)

if __name__ == '__main__':
    current_time = input().strip()
    explosion_time = input().strip()

    result_hours, result_minutes, result_seconds = calculate_time_to_explosion(current_time, explosion_time)
    print(f"{result_hours:02d}:{result_minutes:02d}:{result_seconds:02d}")
