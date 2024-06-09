
def get_correct_time(format, time):
    if format == "12":
        return get_correct_time_12(time)
    else:
        return get_correct_time_24(time)

def get_correct_time_12(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if hours > 12:
        hours = hours - 12
    return f"{hours:02d}:{minutes:02d}"

def get_correct_time_24(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if hours > 23:
        hours = hours - 24
    return f"{hours:02d}:{minutes:02d}"

if __name__ == '__main__':
    format = input()
    time = input()
    print(get_correct_time(format, time))

