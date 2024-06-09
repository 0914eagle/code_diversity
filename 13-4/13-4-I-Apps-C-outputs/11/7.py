
def f1(n):
    # function to find the maximum number of fruits that can be sliced with one straight-line swipe
    # given the locations of the fruits
    # n: number of fruits
    # fruits: list of tuples containing the x and y coordinates of each fruit
    
    # initialize variables
    max_fruits = 0
    fruits_sliced = 0
    
    # loop through each fruit
    for i in range(n):
        # find the number of fruits that can be sliced with the current fruit as the starting point
        fruits_sliced = f2(i, n, fruits)
        
        # update the maximum number of fruits sliced if necessary
        if fruits_sliced > max_fruits:
            max_fruits = fruits_sliced
    
    # return the maximum number of fruits sliced
    return max_fruits

def f2(i, n, fruits):
    # function to find the number of fruits that can be sliced with the ith fruit as the starting point
    # given the locations of the fruits
    # i: index of the starting fruit
    # n: number of fruits
    # fruits: list of tuples containing the x and y coordinates of each fruit
    
    # initialize variables
    fruits_sliced = 0
    j = i + 1
    
    # loop through each fruit after the starting fruit
    while j < n:
        # check if the current fruit is within the slice
        if fruits[j][0] >= fruits[i][0] and fruits[j][1] >= fruits[i][1]:
            # increment the number of fruits sliced
            fruits_sliced += 1
        
        # move to the next fruit
        j += 1
    
    # return the number of fruits sliced
    return fruits_sliced

if __name__ == '__main__':
    # take input from the user
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    
    # call the first function to find the maximum number of fruits that can be sliced
    max_fruits = f1(n, fruits)
    
    # print the output
    print(max_fruits)

