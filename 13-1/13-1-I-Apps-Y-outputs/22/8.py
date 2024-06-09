
def estimate_cost(cost):
    return len(str(cost))

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        cost = int(input())
        print(estimate_cost(cost))

