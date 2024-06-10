
def check_winning_strategy(n, k, ancient_values):
    # Check if k is in the list of ancient values
    if k in ancient_values:
        return True
    
    # Check if there are any ancient values that divide k
    for i in range(n):
        if k % ancient_values[i] == 0:
            return True
    
    # If none of the above conditions are met, Arya cannot have a winning strategy
    return False

def main():
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print("Yes") if check_winning_strategy(n, k, ancient_values) else print("No")

if __name__ == '__main__':
    main()

