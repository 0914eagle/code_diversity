
def get_secret_number(N, K):
    # Your code here
    return secret_number

def guess_number(secret_number, N):
    # Your code here
    return guess

def main():
    N, K = map(int, input().split())
    secret_number = get_secret_number(N, K)
    guess = guess_number(secret_number, N)
    if guess == secret_number:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")

if __name__ == '__main__':
    main()

