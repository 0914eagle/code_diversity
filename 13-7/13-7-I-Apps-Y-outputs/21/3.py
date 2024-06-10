
def get_min_snacks(A, B):
    # Find the smaller value between A and B
    smaller = min(A, B)
    # Find the larger value between A and B
    larger = max(A, B)
    # Calculate the minimum number of snacks needed to distribute evenly
    min_snacks = smaller * (larger // smaller)
    return min_snacks

def main():
    A, B = map(int, input().split())
    print(get_min_snacks(A, B))

if __name__ == '__main__':
    main()

