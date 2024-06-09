
def get_min_quick_changes(routines):
    # Initialize a dictionary to keep track of the dancers and their quick change status
    dancers = {}
    for routine in routines:
        for dancer in routine:
            if dancer not in dancers:
                dancers[dancer] = "normal"
            elif dancers[dancer] == "quick":
                dancers[dancer] = "normal"
    
    # Count the number of quick changes needed
    quick_changes = 0
    for dancer, status in dancers.items():
        if status == "quick":
            quick_changes += 1
    
    return quick_changes

def main():
    num_routines = int(input())
    routines = []
    for _ in range(num_routines):
        routine = input()
        routines.append(routine)
    
    print(get_min_quick_changes(routines))

if __name__ == '__main__':
    main()

