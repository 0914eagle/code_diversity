
def number_of_possible_strings(message):
    n = len(message)
    count = 0
    for i in range(n):
        if message[i] == 'w':
            count += n - i
        elif message[i] == 'm':
            count += n - i
        else:
            count += 1
    return count % (10**9 + 7)

