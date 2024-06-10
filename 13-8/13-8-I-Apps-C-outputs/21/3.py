
def get_distance(node, fragments):
    total_distance = 0
    for fragment in fragments:
        distance = 0
        while fragment != node:
            distance += 1
            fragment = fragment // fragment // get_lowest_prime_divisor(fragment)
        total_distance += distance
    return total_distance

def get_lowest_prime_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def get_min_distance(fragments):
    min_distance = float('inf')
    for node in range(1, len(fragments) + 1):
        distance = get_distance(node, fragments)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    n = int(input())
    fragments = list(map(int, input().split()))
    print(get_min_distance(fragments))

if __name__ == '__main__':
    main()

