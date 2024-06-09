
def get_absurdity_value(laws):
    return sum(laws)

def get_segments(laws, k):
    n = len(laws)
    segments = []
    for i in range(0, n - k + 1):
        segment = laws[i:i + k]
        segments.append(segment)
    return segments

def get_max_absurdity_segments(laws, k):
    segments = get_segments(laws, k)
    max_absurdity = 0
    max_segments = []
    for segment in segments:
        absurdity = get_absurdity_value(segment)
        if absurdity > max_absurdity:
            max_absurdity = absurdity
            max_segments = [segment]
        elif absurdity == max_absurdity:
            max_segments.append(segment)
    return max_segments

def get_min_a_segment(segments):
    min_a = float('inf')
    for segment in segments:
        a = segment[0]
        if a < min_a:
            min_a = a
    return min_a

def get_min_b_segment(segments):
    min_b = float('inf')
    for segment in segments:
        b = segment[-1]
        if b < min_b:
            min_b = b
    return min_b

def get_optimal_segments(laws, k):
    segments = get_max_absurdity_segments(laws, k)
    min_a = get_min_a_segment(segments)
    min_b = get_min_b_segment(segments)
    return [min_a, min_b]

def main():
    n, k = map(int, input().split())
    laws = list(map(int, input().split()))
    optimal_segments = get_optimal_segments(laws, k)
    print(optimal_segments[0], optimal_segments[1])

if __name__ == '__main__':
    main()

