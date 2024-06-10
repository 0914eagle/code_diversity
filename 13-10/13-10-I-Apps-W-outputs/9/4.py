
def find_smallest_n(kate_string, vasya_substring):
    # Convert the input strings to integers
    kate_int = int(kate_string)
    vasya_int = int(vasya_substring)
    
    # Find the smallest integer that is greater than or equal to vasya_int
    smallest_n = vasya_int
    while smallest_n % 10 == 0:
        smallest_n //= 10
    smallest_n += 1
    
    # Check if smallest_n is a valid solution
    if smallest_n % 10 == kate_int % 10:
        return str(smallest_n)
    
    # If not, find the next smallest integer that is a valid solution
    while True:
        smallest_n += 1
        if smallest_n % 10 == kate_int % 10:
            return str(smallest_n)

def main():
    kate_string = input()
    vasya_substring = input()
    print(find_smallest_n(kate_string, vasya_substring))

if __name__ == '__main__':
    main()

