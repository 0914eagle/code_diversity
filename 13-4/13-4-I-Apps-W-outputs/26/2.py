
def get_min_weight(e, e_success, e_failure):
    # Initialize variables
    min_weight = 0
    max_weight = 225
    current_weight = (min_weight + max_weight) / 2
    energy_reserve = e
    
    # Binary search to find the minimum weight
    while energy_reserve > 0 and min_weight < max_weight:
        if energy_reserve - e_success >= 0:
            energy_reserve -= e_success
            min_weight = current_weight
        else:
            energy_reserve -= e_failure
            max_weight = current_weight
        current_weight = (min_weight + max_weight) / 2
    
    return min_weight

def main():
    e, e_success, e_failure = map(int, input().split())
    print(get_min_weight(e, e_success, e_failure))

if __name__ == '__main__':
    main()

