
def solve_cryptarithmetic_puzzle(puzzle):
    words = puzzle.split('+')
    letters = set()
    for word in words:
        letters |= set(word)
    letters = sorted(letters)
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assignments = {}
    for letter in letters:
        assignments[letter] = None
    for letter in letters:
        for digit in digits:
            if letter == words[0][0] and digit == 0:
                continue
            if letter not in assignments or assignments[letter] is None:
                assignments[letter] = digit
                break
    sum1 = 0
    for i, letter in enumerate(letters):
        sum1 += int(assignments[letter]) * (10 ** (len(letters) - i - 1))
    sum2 = 0
    for i, letter in enumerate(letters):
        sum2 += int(assignments[letter]) * (10 ** i)
    if sum1 + sum2 == int(words[1]):
        return ''.join([str(assignments[letter]) for letter in letters]) + '+' + words[1] + '=' + str(sum1 + sum2)
    else:
        return 'impossible'

