
def get_vaccine_efficacy(vaccinated, control):
    vaccinated_infected = vaccinated["infected"].value_counts()
    control_infected = control["infected"].value_counts()
    efficacy = {}
    for strain in ["A", "B", "C"]:
        vaccinated_rate = vaccinated_infected[strain] / len(vaccinated)
        control_rate = control_infected[strain] / len(control)
        if vaccinated_rate < control_rate:
            efficacy[strain] = (control_rate - vaccinated_rate) / control_rate
        else:
            efficacy[strain] = "Not Effective"
    return efficacy

def main():
    n = int(input())
    vaccinated = pd.DataFrame(columns=["vaccinated", "infected"])
    control = pd.DataFrame(columns=["vaccinated", "infected"])
    for i in range(n):
        line = input()
        vaccinated_status, infected_status = line[0], line[1:]
        vaccinated = vaccinated.append({"vaccinated": vaccinated_status, "infected": infected_status}, ignore_index=True)
        control = control.append({"vaccinated": "N", "infected": infected_status}, ignore_index=True)
    efficacy = get_vaccine_efficacy(vaccinated, control)
    print(efficacy["A"])
    print(efficacy["B"])
    print(efficacy["C"])

if __name__ == '__main__':
    main()

