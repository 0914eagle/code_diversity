
def get_fair_bandwidth_allocation(n, t, a, b, d):
    
    # Initialize the allocation vector
    x = [0] * n

    # Loop through each species
    for i in range(n):
        # Calculate the 'fair share' bandwidth
        y = t * d[i] / sum(d)

        # Check if the 'fair share' bandwidth is within the constraints
        if a[i] <= y <= b[i]:
            x[i] = y
        else:
            x[i] = max(a[i], min(b[i], y))

    return x

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = list(map(int, input().split()))
    x = get_fair_bandwidth_allocation(n, t, a, b, d)
    for i in range(n):
        print(x[i])

if __name__ == '__main__':
    main()

