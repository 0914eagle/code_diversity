
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
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                distance.append(j - i)
    return distance

def get_sum(distance):
    sum = 0
    for i in range(len(distance)):
        sum += (len(distance) - i) * abs(distance[i] + i - len(distance))
    return sum

def solve(n):
    a = get_permutation(n)
    distance = get_distance(a)
    sum = get_sum(distance)
    return a

if __name__ == '__main__':
    n = get_input()
    a = solve(n)
    print(*a)

