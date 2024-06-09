
def get_min_seconds(n, a):
    # Initialize variables
    seconds = 0
    k = 1
    boxes = [0] * n
    for i in range(n):
        boxes[i] = a[i]

    # Keep increasing k until all boxes are divisible by k
    while not all(box % k == 0 for box in boxes):
        k += 1
        seconds += 1

        # Move chocolate pieces from box i to box i-1 or i+1 if possible
        for i in range(n):
            if boxes[i] % k == 0:
                continue
            if i > 0 and boxes[i-1] % k == 0:
                boxes[i-1] += boxes[i] % k
                boxes[i] -= boxes[i] % k
            elif i < n-1 and boxes[i+1] % k == 0:
                boxes[i+1] += boxes[i] % k
                boxes[i] -= boxes[i] % k

    return -1 if seconds == 0 else seconds

