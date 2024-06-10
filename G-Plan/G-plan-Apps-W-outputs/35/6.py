
def min_flats_to_visit(n, flats):
    unique_types = set()
    start = 0
    min_flats = float('inf')

    for end in range(n):
        unique_types.add(flats[end])

        while len(unique_types) == len(set(flats[start:end+1])):
            min_flats = min(min_flats, end - start + 1)
            unique_types.remove(flats[start])
            start += 1

    return min_flats

if __name__ == "__main__":
    n = int(input())
    flats = input().strip()

    result = min_flats_to_visit(n, flats)
    print(result)
