
def get_shortest_test_scheme(k, durations):
    # Sort the durations in descending order
    durations.sort(reverse=True)
    
    # Initialize the number of days as the sum of the durations
    num_days = sum(durations)
    
    # Iterate through the durations and find the minimum number of days needed to have at least one allergen active
    for i in range(k):
        if num_days - durations[i] >= 0:
            num_days -= durations[i]
        else:
            break
    
    return num_days

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()

