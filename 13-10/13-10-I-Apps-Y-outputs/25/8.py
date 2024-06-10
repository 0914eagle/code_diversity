
import math

def get_parameter_c(n, p, s, v):
    # Calculate the time it takes to run the algorithm with parameter c = 15
    time_15 = get_time(n, p, s, v, c=15)
    
    # Calculate the time it takes to run the algorithm with parameter c = 20
    time_20 = get_time(n, p, s, v, c=20)
    
    # Calculate the time it takes to run the algorithm with parameter c = 25
    time_25 = get_time(n, p, s, v, c=25)
    
    # Find the parameter c that minimizes the time
    if time_15 < time_20 and time_15 < time_25:
        return 15, time_15
    elif time_20 < time_15 and time_20 < time_25:
        return 20, time_20
    else:
        return 25, time_25

def get_time(n, p, s, v, c):
    # Calculate the time it takes to run the algorithm with the given parameter c
    return s * (1 + 1/c) / (v * 10^9)

def main():
    n, p, s, v = map(float, input().split())
    c, time = get_parameter_c(n, p, s, v)
    print(time, c)

if __name__ == '__main__':
    main()

