
def get_heights(n, m, a):
    # Initialize a list to store the heights of the skyscrapers
    heights = []
    
    # Iterate through the list of heights
    for i in range(n):
        for j in range(m):
            # Add the height of the current skyscraper to the list
            heights.append(a[i][j])
    
    # Return the list of heights
    return heights

def get_min_height(heights):
    # Initialize a variable to store the minimum height
    min_height = 1
    
    # Iterate through the list of heights
    for height in heights:
        # If the current height is less than the minimum height, update the minimum height
        if height < min_height:
            min_height = height
    
    # Return the minimum height
    return min_height

def get_answers(n, m, a):
    # Initialize a list to store the answers
    answers = []
    
    # Iterate through the list of heights
    for i in range(n):
        for j in range(m):
            # Get the heights of the skyscrapers at the current intersection
            heights = get_heights(n, m, a)
            
            # Get the minimum height that can be used
            min_height = get_min_height(heights)
            
            # Add the minimum height to the list of answers
            answers.append(min_height)
    
    # Return the list of answers
    return answers

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    answers = get_answers(n, m, a)
    for answer in answers:
        print(answer, end=" ")

