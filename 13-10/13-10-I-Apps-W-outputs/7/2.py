
def get_minimum_charges(n, welfare):
    # Sort the welfare of the citizens in ascending order
    welfare.sort()
    
    # Initialize the minimum charges to 0
    minimum_charges = 0
    
    # Loop through the citizens and add the difference between their welfare and the average welfare to the minimum charges
    for i in range(n):
        minimum_charges += abs(welfare[i] - welfare[n//2])
    
    return minimum_charges

def main():
    n = int(input())
    welfare = list(map(int, input().split()))
    print(get_minimum_charges(n, welfare))

if __name__ == '__main__':
    main()

