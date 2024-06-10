
def get_comfort_of_segment(segment):
    comfort = 0
    for i in range(len(segment)):
        for j in range(i+1, len(segment)):
            comfort ^= segment[i] ^ segment[j]
    return comfort

def get_maximum_comfort(cities):
    maximum_comfort = 0
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            segment = cities[i:j+1]
            comfort = get_comfort_of_segment(segment)
            maximum_comfort = max(maximum_comfort, comfort)
    return maximum_comfort

if __name__ == '__main__':
    n = int(input())
    cities = list(map(int, input().split()))
    print(get_maximum_comfort(cities))

