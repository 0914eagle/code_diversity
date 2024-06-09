
import sys

class Patient:
    def __init__(self, name, arrival_time, severity):
        self.name = name
        self.arrival_time = arrival_time
        self.severity = severity
        self.wait_time = 0

    def __lt__(self, other):
        return (self.severity + K * self.wait_time, self.name) < (other.severity + K * other.wait_time, other.name)

def process_patient_arrival(arrival_time, name, severity):
    patient = Patient(name, arrival_time, severity)
    patients.append(patient)

def process_doctor_ready(time):
    if not patients:
        print("doctor takes a break")
        return
    patient = patients.pop(0)
    patient.wait_time = time - patient.arrival_time
    print(patient.name)

def process_patient_leaves(time, name):
    for i in range(len(patients)):
        if patients[i].name == name:
            patients.pop(i)
            break

patients = []
K = 0

for _ in range(int(input())):
    query = input().split()
    if query[0] == "1":
        process_patient_arrival(int(query[1]), query[2], int(query[3]))
    elif query[0] == "2":
        process_doctor_ready(int(query[1]))
    else:
        process_patient_leaves(int(query[1]), query[2])


