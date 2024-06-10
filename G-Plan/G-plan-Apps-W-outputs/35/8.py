
def min_flats_to_visit(n, types):
    unique_types = set()
    start = 0
    min_flats = float('inf')

    for end in range(n):
        unique_types.add(types[end])

        while len(unique_types) == len(set(types[start:end+1])):
            min_flats = min(min_flats, end - start + 1)
            unique_types.remove(types[start])
            start += 1

    return min_flats

if __name__ == "__main__":
    n = int(input())
    types = input().strip()

    result = min_flats_to_visit(n, types)
    print(result)
