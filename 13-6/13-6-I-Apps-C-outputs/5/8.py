
def f(string, k):
    # Define a function that applies f to a string k times
    if k == 0:
        return string
    else:
        return f(f(string, k-1), 1)

def get_password(s, k, t):
    # Define a function that generates the password using the given strings and number of iterations
    password = s
    for i in range(k):
        password = f(password, 1)
    return password

def get_forgotten_letters(password, m, m_list):
    # Define a function that returns the forgotten letters based on the input
    forgotten_letters = []
    for i in range(m):
        forgotten_letters.append(password[m_list[i]-1])
    return forgotten_letters

if __name__ == '__main__':
    s = input()
    t = input().split()
    k = int(input())
    m = int(input())
    m_list = list(map(int, input().split()))
    password = get_password(s, k, t)
    forgotten_letters = get_forgotten_letters(password, m, m_list)
    for letter in forgotten_letters:
        print(letter)

