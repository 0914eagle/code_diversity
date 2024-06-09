
def get_input():
    n = int(input())
    return n

def get_array(n):
    a = list(range(1, n+1))
    a += a
    return a

def get_distances(a):
    distances = []
    for i in range(len(a)):
        x = a.index(i+1)
        y = a.index(i+1, x+1)
        distances.append(y-x)
    return distances

def get_sum(distances):
    sum = 0
    for i in range(len(distances)):
        sum += (len(distances)-i) * abs(distances[i] + i - len(distances))
    return sum

def get_optimal_array(n):
    a = get_array(n)
    distances = get_distances(a)
    sum = get_sum(distances)
    optimal_array = a
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                distances = get_distances(a)
                new_sum = get_sum(distances)
                if new_sum < sum:
                    sum = new_sum
                    optimal_array = a
    return optimal_array

def main():
    n = get_input()
    optimal_array = get_optimal_array(n)
    print(*optimal_array)

if __name__ == '__main__':
    main()

