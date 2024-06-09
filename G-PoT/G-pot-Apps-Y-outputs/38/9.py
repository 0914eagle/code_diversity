
def find_opposite_car(N, i):
    return N - i + 1

N, i = map(int, input().split())
result = find_opposite_car(N, i)
print(result)
