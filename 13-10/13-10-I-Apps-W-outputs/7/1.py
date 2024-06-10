
def get_min_charges(citizens, welfare):
    # Calculate the minimum and maximum welfare
    min_welfare = min(welfare)
    max_welfare = max(welfare)
    
    # Calculate the number of charges needed to equalize the welfare
    num_charges = max_welfare - min_welfare
    
    return num_charges

def main():
    # Read the number of citizens and their welfare from stdin
    num_citizens = int(input())
    welfare = list(map(int, input().split()))
    
    # Calculate the minimum number of charges needed to equalize the welfare
    num_charges = get_min_charges(num_citizens, welfare)
    
    # Print the result
    print(num_charges)

if __name__ == '__main__':
    main()

