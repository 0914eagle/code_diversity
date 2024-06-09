
def will_turn_on_air_conditioner(temperature):
    return temperature >= 30

if __name__ == '__main__':
    temperature = int(input())
    print("Yes") if will_turn_on_air_conditioner(temperature) else print("No")

