
def get_segments(q):
    segments = []
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        segments.append((l1, r1, l2, r2))
    return segments

def find_intersection(segments):
    intersection = []
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            l1, r1, l2, r2 = segments[i]
            l3, r3, l4, r4 = segments[j]
            if l1 <= l3 <= r1 or l1 <= r3 <= r1 or l3 <= l1 <= r3 or l3 <= r1 <= r3:
                if l2 <= l4 <= r2 or l2 <= r4 <= r2 or l4 <= l2 <= r4 or l4 <= r2 <= r4:
                    intersection.append((i, j))
    return intersection

def find_solution(segments, intersection):
    solution = []
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if (i, j) not in intersection:
                l1, r1, l2, r2 = segments[i]
                l3, r3, l4, r4 = segments[j]
                a = max(l1, l2)
                b = min(r1, r2)
                c = max(l3, l4)
                d = min(r3, r4)
                if a <= c <= b and c <= d <= b:
                    solution.append((i, j))
    return solution

def main():
    q = int(input())
    segments = get_segments(q)
    intersection = find_intersection(segments)
    solution = find_solution(segments, intersection)
    for i, j in solution:
        print(segments[i][0], segments[j][2])

if __name__ == '__main__':
    main()

