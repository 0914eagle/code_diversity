
def get_min_time(d, k, a, b, t):
    # Calculate the time it takes to drive the first k kilometers
    drive_time = k * a
    
    # Calculate the time it takes to walk the remaining distance
    walk_time = (d - k) * b
    
    # Calculate the time it takes to repair the car
    repair_time = t
    
    # Return the minimum time it takes to reach the post office
    return drive_time + walk_time + repair_time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

