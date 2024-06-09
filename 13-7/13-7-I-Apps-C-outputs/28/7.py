
def solve(format, time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    if format == '12':
        if hours > 12:
            hours = hours - 12
        if hours == 0:
            hours = 12
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    return f'{hours}:{minutes}'

