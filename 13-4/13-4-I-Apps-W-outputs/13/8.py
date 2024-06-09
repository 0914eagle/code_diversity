
import sys

class Patient:
    def __init__(self, name, arrival_time, severity):
        self.name = name
        self.arrival_time = arrival_time
        self.severity = severity
        self.priority = severity

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.name < other.name
        return self.priority > other.priority

def process_patient_arrival(patient):
    patients.append(patient)

def process_doctor_ready(time):
    if not patients:
        return "doctor takes a break"
    patient = patients.pop(0)
    patient.priority = patient.severity + K * (time - patient.arrival_time)
    patients.sort(reverse=True)
    return patient.name

def process_patient_left(time, name):
    for i in range(len(patients)):
        if patients[i].name == name:
            patients.pop(i)
            break

def main():
    global patients, K
    patients = []
    K = int(input())
    for _ in range(int(input())):
        query = input().split()
        if query[0] == "1":
            process_patient_arrival(Patient(query[2], int(query[1]), int(query[3])))
        elif query[0] == "2":
            print(process_doctor_ready(int(query[1])))
        elif query[0] == "3":
            process_patient_left(int(query[1]), query[2])

if __name__ == '__main__':
    main()

