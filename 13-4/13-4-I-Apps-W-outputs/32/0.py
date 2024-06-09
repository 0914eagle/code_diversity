
import sys

def get_gis_permutations(gis):
    # Initialize the number of permutations to 1
    num_permutations = 1
    # Loop through the elements of the GIS
    for i in range(len(gis)):
        # Get the current element of the GIS
        current_element = gis[i]
        # Get the number of elements to the left of the current element that are smaller than it
        num_smaller_elements = sum(1 for j in range(i) if gis[j] < current_element)
        # Get the number of elements to the right of the current element that are larger than it
        num_larger_elements = sum(1 for j in range(i+1, len(gis)) if gis[j] > current_element)
        # Calculate the number of permutations for the current element
        num_permutations *= (num_smaller_elements + 1) * (num_larger_elements + 1)
        # Modulo the number of permutations by the prime number 10^9 + 7 to avoid overflow
        num_permutations %= 1000000007
    return num_permutations

if __name__ == "__main__":
    # Read the input from stdin
    N, L = map(int, input().split())
    gis = list(map(int, input().split()))
    # Get the number of permutations with the given GIS
    num_permutations = get_gis_permutations(gis)
    # Print the number of permutations
    print(num_permutations)

