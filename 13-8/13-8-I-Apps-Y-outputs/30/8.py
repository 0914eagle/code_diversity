
def get_vaccine_efficacy(vaccinated_participants, control_participants):
    vaccine_efficacy = {}
    for strain in ["A", "B", "C"]:
        vaccinated_infected = 0
        control_infected = 0
        for participant in vaccinated_participants:
            if participant[strain] == "Y":
                vaccinated_infected += 1
        for participant in control_participants:
            if participant[strain] == "Y":
                control_infected += 1
        if vaccinated_infected < control_infected:
            vaccine_efficacy[strain] = (control_infected - vaccinated_infected) / control_infected
        else:
            vaccine_efficacy[strain] = "Not Effective"
    return vaccine_efficacy

def main():
    num_participants = int(input())
    vaccinated_participants = []
    control_participants = []
    for _ in range(num_participants):
        participant = input()
        vaccinated = participant[0]
        strain_a = participant[1]
        strain_b = participant[2]
        strain_c = participant[3]
        if vaccinated == "Y":
            vaccinated_participants.append({"A": strain_a, "B": strain_b, "C": strain_c})
        else:
            control_participants.append({"A": strain_a, "B": strain_b, "C": strain_c})
    vaccine_efficacy = get_vaccine_efficacy(vaccinated_participants, control_participants)
    print(vaccine_efficacy["A"])
    print(vaccine_efficacy["B"])
    print(vaccine_efficacy["C"])

if __name__ == '__main__':
    main()

