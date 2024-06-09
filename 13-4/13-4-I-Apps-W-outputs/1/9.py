
def get_absurdity_value(laws):
    return sum(laws)

def get_segments(laws, k):
    n = len(laws)
    segments = []
    for i in range(0, n - k + 1):
        segment = laws[i:i+k]
        segments.append(segment)
    return segments

def get_maximum_absurdity(segments):
    maximum_absurdity = 0
    for segment in segments:
        absurdity = get_absurdity_value(segment)
        if absurdity > maximum_absurdity:
            maximum_absurdity = absurdity
    return maximum_absurdity

def get_optimal_segments(laws, k):
    n = len(laws)
    segments = get_segments(laws, k)
    optimal_segments = []
    for i in range(0, n - k + 1):
        segment = segments[i]
        if get_absurdity_value(segment) == get_maximum_absurdity(segments):
            optimal_segments.append(segment)
    return optimal_segments

def get_optimal_segment_indices(laws, k):
    segments = get_optimal_segments(laws, k)
    segment_indices = []
    for segment in segments:
        segment_indices.append((laws.index(segment[0]), laws.index(segment[-1])))
    return segment_indices

def get_optimal_segment_indices_with_min_a(laws, k):
    segment_indices = get_optimal_segment_indices(laws, k)
    min_a = 1
    for segment_index in segment_indices:
        if segment_index[0] < min_a:
            min_a = segment_index[0]
    return (min_a, segment_indices[0][1])

def get_optimal_segment_indices_with_min_b(laws, k):
    segment_indices = get_optimal_segment_indices(laws, k)
    min_b = 1
    for segment_index in segment_indices:
        if segment_index[1] < min_b:
            min_b = segment_index[1]
    return (segment_indices[0][0], min_b)

def main():
    n, k = map(int, input().split())
    laws = list(map(int, input().split()))
    segment_indices = get_optimal_segment_indices_with_min_a(laws, k)
    print(segment_indices[0], segment_indices[1])

if __name__ == '__main__':
    main()

