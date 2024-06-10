
def get_result(x, y, z):
    # Calculate the total number of upvotes and downvotes
    total_upvotes = x
    total_downvotes = y
    
    # Check if the result is uncertain
    if z > 0:
        # There are unknown persons, so the result may be uncertain
        return "?"
    
    # Calculate the difference between the number of upvotes and downvotes
    difference = total_upvotes - total_downvotes
    
    # Check if the result is certain
    if difference > 0:
        # There are more upvotes than downvotes, so the result is "+"
        return "+"
    elif difference < 0:
        # There are more downvotes than upvotes, so the result is "-"
        return "-"
    else:
        # The number of upvotes and downvotes are equal, so the result is "0"
        return "0"

def main():
    # Read the input
    x, y, z = map(int, input().split())
    
    # Get the result
    result = get_result(x, y, z)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

