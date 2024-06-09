
def get_max_bottles(bottles, height):
    # Initialize a list to store the heights of the shelves
    shelves = []
    # Initialize a variable to store the maximum number of bottles that can be placed
    max_bottles = 0
    # Loop through the bottles
    for bottle in bottles:
        # Check if the bottle fits on any of the existing shelves
        for i in range(len(shelves)):
            if bottle <= shelves[i]:
                # If the bottle fits, remove it from the list of bottles and increment the number of bottles placed
                bottles.remove(bottle)
                max_bottles += 1
                # Update the height of the shelf
                shelves[i] -= bottle
                break
        # If the bottle does not fit on any of the existing shelves, create a new shelf and add it to the list
        else:
            shelves.append(height - bottle)
            max_bottles += 1
            bottles.remove(bottle)
    
    # Return the maximum number of bottles that can be placed
    return max_bottles

def main():
    n, h = map(int, input().split())
    bottles = list(map(int, input().split()))
    print(get_max_bottles(bottles, h))

if __name__ == '__main__':
    main()

