
def get_max_segments(arr):
    n = len(arr)
    segments = 0
    for i in range(n):
        if arr[i] != 0:
            segments += 1
        if i > 0 and arr[i] != arr[i-1]:
            segments += 1
    return segments

