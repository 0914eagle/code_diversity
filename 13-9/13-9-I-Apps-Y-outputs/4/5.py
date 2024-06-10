
def get_earliest_day(num_trees, grow_days):
    # Sort the grow days in ascending order
    grow_days.sort()
    
    # Initialize the earliest day as the last grow day
    earliest_day = grow_days[-1]
    
    # Loop through the grow days and calculate the earliest day
    for i in range(num_trees - 1):
        earliest_day = max(earliest_day, grow_days[i] + grow_days[i + 1])
    
    return earliest_day

def main():
    num_trees = int(input())
    grow_days = list(map(int, input().split()))
    earliest_day = get_earliest_day(num_trees, grow_days)
    print(earliest_day)

if __name__ == '__main__':
    main()

