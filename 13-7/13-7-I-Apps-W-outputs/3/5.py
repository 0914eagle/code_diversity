
def input_slime_healths(n):
    
    healths = []
    n = int(input())
    for i in range(2**n):
        healths.append(int(input()))
    return healths

def is_possible(healths, n):
    
    # Initialize a list to store the healths of the slimes that exist in N seconds
    slime_healths = [0] * (2**n)
    # Set the health of the first slime
    slime_healths[0] = healths[0]
    # Iterate through the remaining slimes and set their healths
    for i in range(1, 2**n):
        # Find the index of the slime that will spawn the current slime
        parent_index = (i - 1) // 2
        # Set the health of the current slime to be one less than the parent slime
        slime_healths[i] = slime_healths[parent_index] - 1
        # If the health of the current slime is less than or equal to 0, return False
        if slime_healths[i] <= 0:
            return False
    # Sort the healths of the slimes that exist in N seconds
    slime_healths.sort()
    # Check if the sorted healths are equal to the input healths
    return slime_healths == healths

def main():
    # Input the healths of the first slime and the subsequent slimes
    healths = input_slime_healths(int(input()))
    # Determine if it is possible to set the healths of the first slime and the subsequent slimes spawn so that the multiset of the healths of the 2^N slimes that will exist in N seconds equals S
    if is_possible(healths, len(healths)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

