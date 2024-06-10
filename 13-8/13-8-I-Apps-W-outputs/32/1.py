
def get_total_comfort(a):
    n = len(a)
    segments = []
    current_segment = []
    for i in range(n):
        if not segments or a[i] != a[i-1]:
            segments.append(current_segment)
            current_segment = []
        current_segment.append(a[i])
    segments.append(current_segment)
    
    total_comfort = 0
    for segment in segments:
        comfort = 0
        for i in range(len(segment)):
            for j in range(i+1, len(segment)):
                comfort ^= segment[j]
        total_comfort += comfort
    return total_comfort

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(get_total_comfort(a))

if __name__ == '__main__':
    main()

