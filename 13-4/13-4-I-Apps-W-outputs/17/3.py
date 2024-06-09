
def get_input():
    n = int(input())
    return n

def get_array(n):
    a = list(range(1, n+1))
    a.extend(a)
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

def permute_array(a):
    n = len(a)
    distance = get_distance(a)
    sum = get_sum(distance)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                distance = get_distance(a)
                new_sum = get_sum(distance)
                if new_sum < sum:
                    sum = new_sum
    return a

def main():
    n = get_input()
    a = get_array(n)
    a = permute_array(a)
    print(*a)

if __name__ == '__main__':
    main()

