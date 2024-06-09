
def get_input():
    n = int(input())
    return n

def get_array(n):
    a = list(range(1, n+1))
    a.extend(a)
    return a

def get_distances(a):
    distances = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                distances.append(j-i)
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
            if a[i] == a[j]:
                new_distances = distances[:]
                new_distances[i] = j-i
                new_distances[j] = i-j
                new_sum = get_sum(new_distances)
                if new_sum < sum:
                    sum = new_sum
                    optimal_array = a[:]
                    optimal_array[i] = a[j]
                    optimal_array[j] = a[i]
    return optimal_array

def main():
    n = get_input()
    optimal_array = get_optimal_array(n)
    print(*optimal_array)

if __name__ == '__main__':
    main()

