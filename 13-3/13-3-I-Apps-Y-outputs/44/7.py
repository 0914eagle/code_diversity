
def get_maximal_string(n, k):
    # Initialize a list to store the letters
    letters = []
    # Iterate from 1 to k
    for i in range(1, k+1):
        # Append the letter at the ith position in the alphabet to the list
        letters.append(chr(i+96))
    # Initialize a string to store the answer
    answer = ""
    # Iterate from 1 to n
    for i in range(1, n+1):
        # If the length of the list is 0, reinitialize it
        if not letters:
            letters = [chr(i+96) for i in range(1, k+1)]
        # Choose a random letter from the list
        letter = letters.pop(random.randint(0, len(letters)-1))
        # Add the letter to the answer
        answer += letter
    # Return the answer
    return answer

def f1(...):
    # Your code here
    return ...

def f2(...):
    # Your code here
    return ...

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(get_maximal_string(n, k))

