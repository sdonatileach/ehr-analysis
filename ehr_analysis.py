# Choose appropriate data structures such that the expected analyses (below) are efficient.
# Include a module docstring describing your rationale for choosing these data structures.
# Include a function docstring analyzing the computational complexity of the data parser.

import datetime

def parse_data(filename: str) -> dict:
    """Read and parse the data files."""
    with open(filename, "r", encoding="UTF-8-sig") as file:
        data = file.readlines()
        count = len(data)
        rows = []
        records = []
        columns = []

        for i in data:
            rows.append(i.strip("\n"))
        for i in range(count):
            if i == 0:
                columns.append(rows[i].split("\t"))
            else:
                records.append(rows[i].split("\t"))

        data_dict = dict()
        for i in range(len(columns[0])):
        values = []
        for j in range(len(records)):
            values.append(records[j][i])
        data_dict[columns[0][i]] = values
    return data_dict


def num_older_than(age: float) -> int:
    """Return the number of patients older than a given age (in years)."""
    dates = data_dict["PatientDateOfBirth"]
    dates_2 = [datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f") for i in dates]
    today = datetime.datetime.today()
    age_days = []
    age_years = []
    for i in range(len(dates_2)):
        age_days.append(today - dates_2[i])
        age_years.append(age_days[i].days/365.25)
    data_dict["PatientDateOfBirth"] = age_years

    older = []
    for i in range(len(data_dict["PatientDateOfBirth"])):
        if data_dict["PatientDateOfBirth"][i] > age:
            older.append(data_dict["PatientID"][i])
    return(len(older))


def sick_patients(lab:str, gt_lt: str, value:float, ???) -> str:
    """Return a (unique) list of patients who have a given test with value above (">") or below ("<") a given level."""