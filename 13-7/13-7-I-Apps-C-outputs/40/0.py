
def get_shortest_test_scheme(k, durations):
    # Sort the durations in descending order
    durations.sort(reverse=True)
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Iterate through the durations and add the number of days needed for each allergen
    for duration in durations:
        num_days += duration
    
    return num_days

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()

