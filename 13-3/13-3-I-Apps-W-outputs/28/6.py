
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    prev_frogs = 0
    stones = []

    # Iterate through the array of stones
    for i in range(len(a)):
        # If there are no stones at the current distance, skip to the next iteration
        if a[i] == 0:
            continue

        # If the current distance is less than or equal to the maximum jump length, add the current distance to the list of stones
        if i <= l:
            stones.append(i)

        # If the current distance is greater than the maximum jump length, remove the first stone from the list
        if i > l:
            stones.pop(0)

        # Calculate the maximum number of frogs that can cross the river using the current list of stones
        max_frogs = max(max_frogs, len(stones))

        # If the current number of frogs is greater than the previous number of frogs, update the previous number of frogs
        if len(stones) > prev_frogs:
            prev_frogs = len(stones)

        # If the current number of frogs is equal to the previous number of frogs, update the current number of frogs
        if len(stones) == prev_frogs:
            curr_frogs += 1

    # Return the maximum number of frogs that can cross the river
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

