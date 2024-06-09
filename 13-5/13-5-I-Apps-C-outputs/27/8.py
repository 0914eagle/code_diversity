
def get_binary_representations(n):
    representations = 0
    for i in range(n+1):
        representations += bin(i).count('1')
    return representations

def get_number_of_representations(n):
    binary_representations = get_binary_representations(n)
    number_of_representations = 0
    for i in range(binary_representations+1):
        if bin(i).count('1') == n:
            number_of_representations += 1
    return number_of_representations

if __name__ == '__main__':
    n = int(input())
    print(get_number_of_representations(n) % 1000000009)

