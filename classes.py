from datetime import datetime
from typing import Dict, List


class Lab:
    def __init__(
        self, patient_id: str, lab_name: str, lab_value: str, units: str, lab_date: str
    ):
        self.patient_id = patient_id
        self.lab_name = lab_name
        self.value = lab_value
        self.units = units
        self.lab_date = lab_date


class Patient:
    def __init__(
        self, patient_id: str, gender: str, DOB: str, race: str, labs: List[Lab]
    ):
        self.patient_id = patient_id
        self.gender = gender
        self.DOB = datetime.strptime(str(DOB), "%Y-%m-%d %H:%M:%S.%f")
        self.race = race
        self.labs = labs

    @property
    def age(self) -> float:
        age = (datetime.today() - self.DOB).days / 365.25
        return round(age, 2)

    @property
    def age_at_admis(self) -> float:
        admis_dates = []
        for i in range(len(self.labs)):
            admis_dates.append(
                datetime.strptime(str(self.labs[i].lab_date), "%Y-%m-%d %H:%M:%S.%f")
            )
        age = (min(admis_dates) - self.DOB).days / 365.25
        return round(age, 2)


def parse_data(patient_file: str, lab_file: str, delimiter: str) -> Dict[str, Patient]:
    """Read and parse the data files. Returns a dictionary.

    Assumptions:
    - the first row of the file contains the column headers
    - the positions of the columns of interest in the files will not change

    Computational Complexity: Assuming `N` is the number of patients and
    `M` is the average number of labs per patient, opening the patient file takes
    constant time, and reading lines takes N time, where N is the number of lines
    in the file. Opening the lab file takes constant time, and reading lines takes
    N*M time because there are M labs per patient. Creating the empty dictionary
    takes constant time. Stripping the lines of whitespace and splitting the lines
    into a list takes N time as we are looping through all lines in the patient file.
    We do the same thing with the lab file, except this time it is nested inside
    the previous loop, yielding N*N*M time. The following if statement happens N*N*M
    times as well because it is inside this loop. Initializing the Lab object takes
    constant time, and appending it to the list takes constant time. This all occurs
    inside the lab loop, yielding N*N*M time. Initializing the Patient object takes
    constant time, which occcurs inside the patient loop, yielding N time. Finally,
    adding all patient information plus the list of labs to the dictionary takes
    constant time, occuring N times. Our big-O notation is therefore
    O(N+(N*M)+3(N*N*M)+2N) and after dropping the constant factor, we yield O(N*N*M)
    complexity.
    """
    patient_data = open(patient_file, "r", encoding="UTF-8-sig").readlines()
    lab_data = open(lab_file, "r", encoding="UTF-8-sig").readlines()
    patient_dict = dict()
    for i in range(len(patient_data) - 1):
        i += 1  # skip header
        patient_info = patient_data[i].strip("\n").split(delimiter)
        patient_labs = []  # list of labs to be replaced with every new patient
        for j in range(len(lab_data) - 1):
            j += 1  # skip header
            lab_info = lab_data[j].strip("\n").split(delimiter)
            if patient_info[0] == lab_info[0]:
                patient_labs.append(
                    Lab(lab_info[0], lab_info[2], lab_info[3], lab_info[4], lab_info[5])
                )  # initialize lab object and append to list
        patient = Patient(
            patient_info[0],
            patient_info[1],
            patient_info[2],
            patient_info[3],
            patient_labs,
        )  # initialize patient object with all info and list of labs
        patient_dict[
            patient_info[0]
        ] = patient  # add all patient information plus labs to dictionary
    return patient_dict


if __name__ == "__main__":
    patient_dict = parse_data(
        "PatientCorePopulatedTable.txt", "LabsCorePopulatedTable.txt", "\t"
    )
