
def input_data():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def solve(n, k, a):
    beauty_set = set()
    detachments = []
    for i in range(k):
        c = 1
        while c <= n and sum(a[:c]) not in beauty_set:
            beauty_set.add(sum(a[:c]))
            c += 1
        detachments.append((c, a[:c]))
        a = a[c:]
    return detachments

def output_data(detachments):
    for detachment in detachments:
        print(detachment[0], *detachment[1])

if __name__ == '__main__':
    n, k, a = input_data()
    detachments = solve(n, k, a)
    output_data(detachments)

