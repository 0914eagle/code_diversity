
def count_non_equivalence_relations(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i != j:
                count += 1
    return count

def main():
    n = int(input())
    print(count_non_equivalence_relations(n) % (10**9 + 7))

if __name__ == '__main__':
    main()

