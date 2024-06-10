
def get_time_and_c(n, p, s, v):
    # Define the approximation factor
    c = 15

    # Calculate the time it takes to run the algorithm
    time_algorithm = s * (1 + 1 / c) / v

    # Calculate the time it takes to distribute the keys
    time_distribution = n * (log_2(n) ** (c * sqrt(2))) / (p * 1000000000)

    # Calculate the total time
    time_total = time_algorithm + time_distribution

    return time_total, c

def main():
    n, p, s, v = map(float, input().split())
    time_total, c = get_time_and_c(n, p, s, v)
    print(f"{time_total:.6f} {c:.6f}")

if __name__ == '__main__':
    main()

