
import itertools

def find_smallest_distance(m, x, y):
    def check_distance(z, m, x, y):
        for i in range(3):
            t = (x[i] - z) % m[i]
            if t > y[i] or t < -y[i]:
                return False
        return True

    for z in itertools.count():
        if check_distance(z, m, x, y):
            return z

# Input
m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Output
print(find_smallest_distance(m, x, y))
