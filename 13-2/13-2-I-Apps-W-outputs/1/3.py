
def f1(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1
    
    # Calculate the distance the caterpillar travels by day and night
    day_distance = a * 10
    night_distance = b * 10
    
    # Calculate the number of days it takes for the caterpillar to travel the total distance
    days = total_distance // (day_distance + night_distance)
    
    # Check if the caterpillar can get the apple on the last day
    if total_distance % (day_distance + night_distance) == 0:
        return days
    else:
        return -1
    
def f2(...):
    ...
    
if __name__ == '__main__':
    h1, h2, a, b = map(int, input().split())
    print(f1(h1, h2, a, b))

