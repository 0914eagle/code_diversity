
import math

def get_min_time(n, s, x, v, t):
    # Initialize the minimum time needed to reach point 0 and point 10^6
    min_time_0 = math.inf
    min_time_10_6 = math.inf
    
    # Loop through each person
    for i in range(n):
        # Calculate the time it takes for the person to reach point 0
        time_0 = (x[i] - 0) / v[i]
        
        # Calculate the time it takes for the person to reach point 10^6
        time_10_6 = (10**6 - x[i]) / v[i]
        
        # Check if the person can reach point 0 before the bomb is placed
        if time_0 < min_time_0:
            min_time_0 = time_0
        
        # Check if the person can reach point 10^6 before the bomb is placed
        if time_10_6 < min_time_10_6:
            min_time_10_6 = time_10_6
    
    # Calculate the time it takes for the rays to catch up with the people
    time_rays = math.ceil(s / (v[0] + v[1]))
    
    # Calculate the minimum time needed for both points 0 and 10^6 to be reached
    min_time = min(min_time_0 + time_rays, min_time_10_6 + time_rays)
    
    return min_time

def main():
    n, s = map(int, input().split())
    x = []
    v = []
    t = []
    for i in range(n):
        xi, vi, ti = map(int, input().split())
        x.append(xi)
        v.append(vi)
        t.append(ti)
    print(get_min_time(n, s, x, v, t))

if __name__ == '__main__':
    main()

