
def get_distance(num1, num2):
    diff = abs(num1 - num2)
    return diff

def get_sum_of_distances(A, B):
    sum_of_distances = 0
    for i in range(A, B+1):
        for j in range(A, B+1):
            if i != j:
                sum_of_distances += get_distance(i, j)
    return sum_of_distances % 1000000007

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_sum_of_distances(A, B))

