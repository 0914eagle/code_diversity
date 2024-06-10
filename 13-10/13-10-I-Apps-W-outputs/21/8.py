
def get_maximum_groups(n, m):
    # Initialize a list to store the remaining cats
    remaining_cats = list(range(1, n + 1))
    
    # Iterate through the number of cats that have left the circle
    for _ in range(m):
        # Find the index of the first cat that has left the circle
        left_cat_index = remaining_cats.index(1)
        
        # Remove the first cat that has left the circle from the list
        remaining_cats.pop(left_cat_index)
        
        # Insert a new cat at the end of the list to fill the gap
        remaining_cats.append(remaining_cats[left_cat_index - 1])
    
    # Return the maximum number of groups possible
    return len(set(remaining_cats))

def main():
    n, m = map(int, input().split())
    print(get_maximum_groups(n, m))

if __name__ == '__main__':
    main()

