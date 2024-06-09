
import random

def solve(expression):
    tokens = expression.split('+')
    num_tokens = len(tokens)
    num_ints = num_tokens // 2 + 1
    num_plus_symbols = num_tokens - num_ints
    distinct_ints = set()

    for _ in range(num_plus_symbols):
        random.seed()
        ints = [int(tokens[i]) for i in range(0, num_ints, 2)]
        strs = [tokens[i] for i in range(1, num_ints, 2)]
        result = ints[0]
        for i in range(1, num_ints):
            if random.randint(0, 1) == 0:
                result += ints[i]
            else:
                result = str(result) + strs[i - 1]
        distinct_ints.add(result)

    return len(distinct_ints)

