
def find_photo(heights):
    # Sort the heights in descending order
    heights.sort(reverse=True)
    # Initialize the indices of the people in the photo
    indices = list(range(1, len(heights) + 1))
    # Find the index of Alice and Bob in the sorted heights and indices
    alice_index = indices[heights.index(2)]
    bob_index = indices[heights.index(3)]
    # Find the index of the person standing between Alice and Bob
    middle_index = indices[(alice_index + bob_index) // 2]
    # Return the indices of the people in the photo in the correct order
    return [middle_index]

