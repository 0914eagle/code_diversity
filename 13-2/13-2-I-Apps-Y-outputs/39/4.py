
def count_anagrams(strings):
    n = len(strings)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if sorted(strings[i]) == sorted(strings[j]):
                count += 1
    return count

def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    print(count_anagrams(strings))

if __name__ == '__main__':
    main()

