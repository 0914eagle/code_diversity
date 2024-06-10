
def get_time_and_c(n, p, s, v):
    # Calculate the approximate running time of the Arora-Mitchell algorithm
    approx_time = n * (log_2(n) ** (c * sqrt(2))) / (p * 10**9)
    
    # Calculate the total time it takes to distribute the keys
    total_time = s / v + approx_time
    
    # Solve for c to minimize the total time
    c = optimize.fsolve(lambda c: total_time - n * (log_2(n) ** (c * sqrt(2))) / (p * 10**9), 1)
    
    return total_time, c

def main():
    n, p, s, v = map(float, input().split())
    time, c = get_time_and_c(n, p, s, v)
    print(time, c)

if __name__ == '__main__':
    main()

