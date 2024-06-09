
def get_shortest_test_scheme(k, durations):
    # Sort the durations in non-decreasing order
    durations.sort()
    
    # Initialize the number of days as the sum of the durations
    num_days = sum(durations)
    
    # Loop through each duration and find the minimum number of days needed to test for that allergen
    for i in range(k):
        num_days = min(num_days, durations[i] + 1)
    
    return num_days

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()

