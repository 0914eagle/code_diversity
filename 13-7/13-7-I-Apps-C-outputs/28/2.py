
def solve(format, time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    
    if format == '12':
        if hours > 12:
            hours = hours - 12
        if hours == 0:
            hours = 12
    elif format == '24':
        if hours > 23:
            hours = hours - 24
    
    if minutes > 59:
        minutes = minutes - 60
    
    return f"{hours:02d}:{minutes:02d}"

