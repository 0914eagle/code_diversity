
import math
import random

def f1(n, b, d):
    # Calculate the area of the boar's body
    area_boar = math.pi * b ** 2
    
    # Initialize the probability of the boar completing its charge without hitting a tree
    prob = 1
    
    # Loop through each tree
    for i in range(n):
        # Calculate the distance between the boar and the current tree
        dist = math.sqrt((x[i] - 0) ** 2 + (y[i] - 0) ** 2)
        
        # Check if the boar's body overlaps with the current tree
        if dist < b + r[i]:
            # Calculate the area of overlap between the boar's body and the current tree
            overlap = math.pi * min(b, r[i]) ** 2
            
            # Update the probability of the boar completing its charge without hitting a tree
            prob -= overlap / area_boar
    
    # Return the probability of the boar completing its charge without hitting a tree
    return prob

def f2(n, b, d):
    # Initialize the probability of the boar completing its charge without hitting a tree
    prob = 1
    
    # Loop through each tree
    for i in range(n):
        # Calculate the distance between the boar and the current tree
        dist = math.sqrt((x[i] - 0) ** 2 + (y[i] - 0) ** 2)
        
        # Check if the boar's body overlaps with the current tree
        if dist < b + r[i]:
            # Calculate the area of overlap between the boar's body and the current tree
            overlap = math.pi * min(b, r[i]) ** 2
            
            # Update the probability of the boar completing its charge without hitting a tree
            prob -= overlap / (math.pi * b ** 2)
    
    # Return the probability of the boar completing its charge without hitting a tree
    return prob

if __name__ == '__main__':
    # Read the input
    n, b, d = map(int, input().split())
    x = []
    y = []
    r = []
    for i in range(n):
        xi, yi, ri = map(int, input().split())
        x.append(xi)
        y.append(yi)
        r.append(ri)
    
    # Calculate the probability of the boar completing its charge without hitting a tree
    prob = f1(n, b, d)
    
    # Print the probability
    print(prob)

