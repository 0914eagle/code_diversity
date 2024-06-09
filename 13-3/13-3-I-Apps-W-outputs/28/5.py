
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    current_frogs = 0
    current_distance = 0
    stones = []

    # Iterate through the input array
    for i in range(len(a)):
        # If the current distance is within the jump length of the frog, add the current number of stones to the list of available stones
        if current_distance + a[i] <= l:
            stones.append(a[i])
        # If the current distance is greater than the jump length of the frog, remove the first stone from the list of available stones
        elif current_distance + a[i] > l:
            stones.pop(0)
        # If there are any stones available, add the current frog to the list of frogs that have crossed the river
        if stones:
            current_frogs += 1
        # Update the maximum number of frogs if necessary
        max_frogs = max(max_frogs, current_frogs)
        # Update the current distance
        current_distance += a[i]

    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

