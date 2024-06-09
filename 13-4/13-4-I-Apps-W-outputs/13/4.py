
import sys
import os

class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.wait_time = 0

    def __lt__(self, other):
        if self.severity == other.severity:
            return self.name < other.name
        return self.severity > other.severity

    def __str__(self):
        return f"{self.name}: {self.severity}"

def process_patient_arrival(patient):
    patients.append(patient)

def process_doctor_ready(time):
    if not patients:
        print("doctor takes a break")
        return
    patient = patients.pop(0)
    patient.wait_time += time - patient.arrival_time
    print(patient.name)

def process_patient_left(time, name):
    for i, patient in enumerate(patients):
        if patient.name == name:
            patients.pop(i)
            break

def read_input():
    global patients, k
    n, k = map(int, input().split())
    for _ in range(n):
        q, *args = input().split()
        if q == "1":
            process_patient_arrival(Patient(*args))
        elif q == "2":
            process_doctor_ready(int(args[0]))
        elif q == "3":
            process_patient_left(int(args[0]), args[1])

if __name__ == "__main__":
    patients = []
    read_input()

