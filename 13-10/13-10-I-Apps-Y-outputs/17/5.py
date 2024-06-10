
def input_data():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    return n, p, q

def count_lexicographically_smaller(p, q):
    count = 0
    for i in range(n):
        if p[i] < q[i]:
            break
        elif p[i] > q[i]:
            count += 1
    return count

def solve(n, p, q):
    count_p = count_lexicographically_smaller(p, q)
    count_q = count_lexicographically_smaller(q, p)
    return abs(count_p - count_q)

if __name__ == '__main__':
    n, p, q = input_data()
    print(solve(n, p, q))

