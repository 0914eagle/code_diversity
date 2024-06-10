
def get_vaccine_efficacy(vaccinated_participants, control_participants):
    vaccine_efficacy = {}
    for strain in ["A", "B", "C"]:
        vaccinated_strain_count = 0
        control_strain_count = 0
        for participant in vaccinated_participants:
            if participant[strain] == "Y":
                vaccinated_strain_count += 1
        for participant in control_participants:
            if participant[strain] == "Y":
                control_strain_count += 1
        if vaccinated_strain_count == 0 or control_strain_count == 0:
            vaccine_efficacy[strain] = "Not Effective"
        else:
            vaccine_efficacy[strain] = (vaccinated_strain_count / control_strain_count) * 100
    return vaccine_efficacy

def main():
    N = int(input())
    vaccinated_participants = []
    control_participants = []
    for i in range(N):
        participant = input()
        if participant[0] == "Y":
            vaccinated_participants.append(participant)
        else:
            control_participants.append(participant)
    vaccine_efficacy = get_vaccine_efficacy(vaccinated_participants, control_participants)
    for strain in ["A", "B", "C"]:
        print(vaccine_efficacy[strain])

if __name__ == '__main__':
    main()

