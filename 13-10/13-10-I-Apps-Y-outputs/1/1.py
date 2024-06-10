
def get_sodas_drunk(empty_bottles, empty_bottles_found, cost_per_bottle):
    total_sodas_drunk = 0
    while empty_bottles < cost_per_bottle:
        total_sodas_drunk += 1
        empty_bottles += 1
        if empty_bottles_found > 0:
            empty_bottles += empty_bottles_found
            empty_bottles_found = 0
    return total_sodas_drunk

def get_sodas_needed(empty_bottles, cost_per_bottle):
    total_sodas_needed = 0
    while empty_bottles < cost_per_bottle:
        total_sodas_needed += 1
        empty_bottles += 1
    return total_sodas_needed

if __name__ == '__main__':
    e = int(input("Enter the number of empty bottles in Tim's possession at the start of the day: "))
    f = int(input("Enter the number of empty bottles found during the day: "))
    c = int(input("Enter the number of empty bottles required to buy a new soda: "))
    print(f"Tim drank {get_sodas_drunk(e, f, c)} sodas on his extra thirsty day.")
    print(f"Tim needs {get_sodas_needed(e, c)} sodas to buy a new soda.")

