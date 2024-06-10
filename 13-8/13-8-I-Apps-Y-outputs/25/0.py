
def check_if_war_will_break_out(empire_a_cities, empire_b_cities, empire_a_capital, empire_b_capital):
    # Check if there is a common coordinate that satisfies all three conditions
    for coordinate in set(empire_a_cities + empire_b_cities):
        if coordinate < empire_a_capital <= empire_b_capital and coordinate < empire_b_capital:
            return "No War"
    return "War"

def get_input():
    num_empire_a_cities, num_empire_b_cities, empire_a_capital, empire_b_capital = map(int, input().split())
    empire_a_cities = list(map(int, input().split()))
    empire_b_cities = list(map(int, input().split()))
    return num_empire_a_cities, num_empire_b_cities, empire_a_capital, empire_b_capital, empire_a_cities, empire_b_cities

if __name__ == '__main__':
    num_empire_a_cities, num_empire_b_cities, empire_a_capital, empire_b_capital, empire_a_cities, empire_b_cities = get_input()
    print(check_if_war_will_break_out(empire_a_cities, empire_b_cities, empire_a_capital, empire_b_capital))

