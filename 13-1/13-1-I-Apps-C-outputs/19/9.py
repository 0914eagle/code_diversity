
def f1(c, n, a):
    # Initialize a list to store the number of times each object is accessed
    count = [0] * n

    # Iterate through the accesses
    for i in range(a):
        # Get the current object being accessed
        obj = input()

        # If the object is not already in the cache, insert it and increment the count
        if count[obj] == 0:
            count[obj] += 1

    # Return the least number of times an object must be read into the cache
    return min(count)

