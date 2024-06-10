
def optimal_order(probabilities):
    
    n = len(probabilities)
    opt_order = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if probabilities[opt_order[i]] < probabilities[opt_order[j]]:
                opt_order[i], opt_order[j] = opt_order[j], opt_order[i]
    return sum(i * probabilities[opt_order[i]] for i in range(n))

def main():
    n = int(input())
    probabilities = []
    for _ in range(n):
        password, probability = input().split()
        probabilities.append(float(probability))
    print(optimal_order(probabilities))

if __name__ == '__main__':
    main()

