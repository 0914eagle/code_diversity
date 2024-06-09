
def get_largest_element(my_list):
    return max(my_list)

def get_base_and_xor_language(element):
    if element == 1:
        return "ABRACADABRA"
    else:
        return "BASE"

def get_string(element):
    if element == 1:
        return "SAYING"
    else:
        return "STRING"

def get_array(element):
    if element == 1:
        return "I HAVE NO ARRAY"
    else:
        return "ARRAY"

def get_west_hyperspace(element):
    if element == 1:
        return "ELEMENTS MAY NOT BE STORED"
    else:
        return "WEST HYPERSPACE"

def get_magic(element):
    if element == 1:
        return "WITHOUT A MAGIC"
    else:
        return "MAGIC"

def get_rupture(element):
    if element == 1:
        return "THE LAST STACK RUPTURES"
    else:
        return "RUPTURE"

def get_embarrassment(element):
    if element == 1:
        return "OH, THE EMBARRASSMENT!"
    else:
        return "EMBARRASSMENT"

def get_dont_byte(element):
    if element == 1:
        return "DON'T BYTE OF MORE THAN YOU CAN CHEW"
    else:
        return "BYTE"

def get_mathematics(element):
    if element == 1:
        return "YOU CAN ONLY DISTORT THE LARGEST OF MATHEMATICS SO FAR"
    else:
        return "MATHEMATICS"

def get_chew(element):
    if element == 1:
        return "CHEW"
    else:
        return "CHEW"

def get_solution(my_list):
    largest_element = get_largest_element(my_list)
    base_and_xor_language = get_base_and_xor_language(largest_element)
    string = get_string(largest_element)
    array = get_array(largest_element)
    west_hyperspace = get_west_hyperspace(largest_element)
    magic = get_magic(largest_element)
    rupture = get_rupture(largest_element)
    embarrassment = get_embarrassment(largest_element)
    dont_byte = get_dont_byte(largest_element)
    mathematics = get_mathematics(largest_element)
    chew = get_chew(largest_element)
    solution = f"{base_and_xor_language} {string} {array} {west_hyperspace} {magic} {rupture} {embarrassment} {dont_byte} {mathematics} {chew}"
    return solution

if __name__ == '__main__':
    n = int(input())
    my_list = list(map(int, input().split()))
    print(get_solution(my_list))

