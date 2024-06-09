
def count_types(cheeses):
    types = set()
    for cheese in cheeses:
        types.add(cheese[1])
    return len(types)

def main():
    num_cheeses = int(input())
    cheeses = []
    for i in range(num_cheeses):
        cheese = input().split()
        cheeses.append(cheese)
    print(count_types(cheeses))

if __name__ == '__main__':
    main()

