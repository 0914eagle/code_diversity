
def get_input():
    n = int(input())
    return n

def get_permutation(n):
    a = list(range(1, n+1))
    a += a
    return a

def get_distance(a):
    distance = []
    for i in range(len(a)):
        x = a.index(i+1)
        y = a.index(i+1, x+1)
        distance.append(y-x)
    return distance

def get_sum(distance):
    sum = 0
    for i in range(len(distance)):
        sum += (len(distance)-i) * abs(distance[i] + i - len(distance))
    return sum

def get_min_sum(n):
    a = get_permutation(n)
    distance = get_distance(a)
    sum = get_sum(distance)
    return a, sum

def main():
    n = get_input()
    a, sum = get_min_sum(n)
    print(*a)

if __name__ == '__main__':
    main()

