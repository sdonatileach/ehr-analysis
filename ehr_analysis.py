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


def num_older_than(age: float, patient_dict: Dict[str, Patient]) -> int:
    """Returns the number of patients who are older than a given age (in years).

    Computational Complexity: Assuming `N` is the number of patients, we iterate
    over the dictionary once and initialize each patient, which takes N time. We
    then check the age of each of the initialized patients is greater than the given
    age, which also takes N time. Finally, incrementing the counter takes N time.
    Our big-O notation is therefore 3N, and after dropping the constant factor, we
    are left with O(N) time complexity.
    """
    num_older = 0
    for patient in patient_dict.values():
        if patient.age > age:
            num_older += 1
    return num_older


def sick_patients(
    lab: str, gt_lt: str, value: float, patient_dict: Dict[str, Patient]
) -> set:
    """Returns a (unique) list of patients who have a given test with value
    above (">") or below ("<") a given level.

    Computational Complexity: Assuming `N` is the number of patients and
    `M` is the average number of labs per patient, we iterate over the length of the
    dictionary once and initialize each patient, which takes N time. This is followed
    by another iteration over all the labs of the initialized patients, giving us N*M
    time complexity.  The next three "if" statements all take constant time,
    but each operation need to be repeated for each N*M, because we are inside the for
    loops, resulting in 4(N*M).  We repeat a similar process in the elif operation
    which adds an additional 3(N*M) to the total. Finally, we look through the set of
    unique labs which takes constant time. Our resulting big-O notation is
    O((N*M)+4(N*M)+3(N*M)+N). After dropping the constant factor, we yield O(N*M)
    time complexity.
    """
    sick_patients = set()
    labs = set()
    for patient in patient_dict.values():
        for i in range(len(patient.labs)):
            labs.add(patient.labs[i].lab_name)
            if lab == patient.labs[i].lab_name:
                if gt_lt == ">":
                    if float(patient.labs[i].value) > value:
                        sick_patients.add(patient)
                elif gt_lt == "<":
                    if float(patient.labs[i].value) < value:
                        sick_patients.add(patient)
                else:
                    raise ValueError("Please enter a valid operator")
    if lab not in labs:
        raise ValueError("Please enter a valid lab name")
    return sick_patients


if __name__ == "__main__":
    patient_dict = parse_data(
        "PatientCorePopulatedTable.txt", "LabsCorePopulatedTable.txt", "\t"
    )
