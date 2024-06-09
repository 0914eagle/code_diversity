
def solve(k, a):
    # Initialize variables
    day = 1
    days_spent = 0
    classes_taken = 0

    # Loop through the input array
    for i in range(len(a)):
        # If classes are held on the current day and there are still classes to take, take a class
        if a[i] == 1 and classes_taken < k:
            classes_taken += 1
        # If classes are not held on the current day or all classes have been taken, move to the next day
        else:
            day += 1
            days_spent += 1

    # Return the number of days spent in the capital of Berland
    return days_spent

