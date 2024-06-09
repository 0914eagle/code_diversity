
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    current_frogs = 0
    last_stone = 0

    # Iterate through the stones
    for i in range(len(a)):
        # Calculate the number of frogs that can cross the current stone
        current_frogs += a[i]

        # If the current stone is within the frog's jump length, add it to the count
        if i - last_stone <= l:
            max_frogs += current_frogs

        # Update the last stone position
        last_stone = i

    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

