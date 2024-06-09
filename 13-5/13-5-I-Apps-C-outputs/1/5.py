
import itertools

def get_composite_strings(initial_strings, k):
    return [''.join(i) for i in itertools.combinations(initial_strings, k)]

def get_sorted_composite_strings(initial_strings, k):
    return sorted(get_composite_strings(initial_strings, k))

def get_position_in_sorted_list(test_composite_string, initial_strings, k):
    sorted_composite_strings = get_sorted_composite_strings(initial_strings, k)
    return sorted_composite_strings.index(test_composite_string) % (10**9 + 7)

