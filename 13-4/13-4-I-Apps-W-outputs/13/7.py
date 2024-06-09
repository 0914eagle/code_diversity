
import sys

class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.waiting_time = 0

    def __lt__(self, other):
        if self.severity == other.severity:
            return self.name < other.name
        return self.severity > other.severity

def f1(query):
    global patients, current_time
    query = query.split()
    if query[0] == "1":
        arrival_time = int(query[1])
        name = query[2]
        severity = int(query[3])
        patient = Patient(name, severity, arrival_time)
        patients.append(patient)
    elif query[0] == "2":
        current_time = int(query[1])
        patients.sort(key=lambda x: x.severity + x.waiting_time)
        if patients:
            patient = patients.pop(0)
            patient.waiting_time += current_time - patient.arrival_time
            return patient.name
        else:
            return "doctor takes a break"
    elif query[0] == "3":
        name = query[2]
        for patient in patients:
            if patient.name == name:
                patients.remove(patient)
                break

def f2(query):
    global patients, current_time
    query = query.split()
    if query[0] == "1":
        arrival_time = int(query[1])
        name = query[2]
        severity = int(query[3])
        patient = Patient(name, severity, arrival_time)
        patients.append(patient)
    elif query[0] == "2":
        current_time = int(query[1])
        patients.sort(key=lambda x: x.severity + x.waiting_time)
        if patients:
            patient = patients.pop(0)
            patient.waiting_time += current_time - patient.arrival_time
            return patient.name
        else:
            return "doctor takes a break"
    elif query[0] == "3":
        name = query[2]
        for patient in patients:
            if patient.name == name:
                patients.remove(patient)
                break

def main():
    global patients, current_time, k
    patients = []
    current_time = 0
    k = int(input())
    for _ in range(int(input())):
        query = input()
        if query[0] == "1":
            arrival_time = int(query[1])
            name = query[2]
            severity = int(query[3])
            patient = Patient(name, severity, arrival_time)
            patients.append(patient)
        elif query[0] == "2":
            current_time = int(query[1])
            patients.sort(key=lambda x: x.severity + x.waiting_time)
            if patients:
                patient = patients.pop(0)
                patient.waiting_time += current_time - patient.arrival_time
                print(patient.name)
            else:
                print("doctor takes a break")
        elif query[0] == "3":
            name = query[2]
            for patient in patients:
                if patient.name == name:
                    patients.remove(patient)
                    break

if __name__ == '__main__':
    main()

