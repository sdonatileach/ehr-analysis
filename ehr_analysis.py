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
        data_dict = dict()
        for i in data:
            rows.append(i.strip("\n"))
        for i in range(count):
            if i == 0:
                columns.append(rows[i].split("\t"))
            else:
                records.append(rows[i].split("\t"))
        for i in range(len(columns[0])):
        values = []
        for j in range(len(records)):
            values.append(records[j][i])
        data_dict[columns[0][i]] = values
    return data_dict

def num_older_than(age: float, ???) -> int:
    """Return the number of number of patients older than a given age (in years)."""


def sick_patients(lab:str, gt_lt: str, value:float, ???) -> str:
    """Return a (unique) list of patients who have a given test with value above (">") or below ("<") a given level."""