
def min_flats_to_visit(n, flats):
    types = set()
    start, end = 0, 0
    min_flats = float('inf')

    while end < n:
        types.add(flats[end])
        while len(types) == len(set(flats[start:end + 1])):
            min_flats = min(min_flats, end - start + 1)
            types.remove(flats[start])
            start += 1
        end += 1

    return min_flats

if __name__ == "__main__":
    n = int(input())
    flats = input().strip()
    result = min_flats_to_visit(n, flats)
    print(result)
