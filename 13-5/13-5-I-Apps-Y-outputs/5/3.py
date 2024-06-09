
def get_input():
    N = int(input())
    values = list(map(int, input().split()))
    return N, values

def compose_ingredients(values):
    while len(values) > 1:
        values = [sum(values[i:i+2])/2 for i in range(0, len(values), 2)]
    return values[0]

def solve(N, values):
    return compose_ingredients(values)

if __name__ == '__main__':
    N, values = get_input()
    print(solve(N, values))

