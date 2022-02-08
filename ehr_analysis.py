"""Data Structures:

Each of the following data structures is a dictionary where the keys 
are each of the column headers, and the dictionary values are each of the
corresponding column values in the form of a list of lists.
    

My rationale for choosing a dictionary as the data structure was that key-value 
pairs have a similar structure to a standard table, where dictionary keys are equivalent
to table columns and dictionary values are equivalent to column values.
My rationale for the dictionary values being a list of lists was two-fold.
First, we needed each dictionary key to map to multiple values.
Second, we needed to be able to index and iterate over the list of lists
in the other two functions."""

import datetime
from typing import Dict, Union


def parse_data(filename: str, delimiter: str) -> Dict[str, Union[str, float]]:
    """Read and parse the data files. Return a dictionary.

    Assumptions:
    - the first row of the file contains the column headers

    Computational Complexity: opening the file takes constant time,
    but reading lines takes N time, where N is the number of lines in the file.
    Stripping the lines of whitespace and splitting the lines into a list
    takes N time as we are looping through all lines. The operation of appending
    to lists takes constant time, but appending to the "columns" list only
    occurs once, whereas appending to the "rows" occurs N times, and appending to
    the "records" list occurs N-1 times.  Finally, creating the empty
    dictionary takes constant time, and then we begin to iterate over the length of
    the columns and within that the length of the rows, which takes N^2 time.
    Our big-O notation is therefore O(N**2+(N-1)+3N) and after dropping the constant factor,
    we yield O(N**2) complexity.
    """
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
                columns.append(rows[i].split(delimiter))
            else:
                records.append(rows[i].split(delimiter))

        data_dict = dict()
        for i in range(len(columns[0])):
            values = []
            for j in range(len(records)):
                values.append(records[j][i])
            data_dict[columns[0][i]] = values

        return data_dict


def date_time(x:str):
    date = []
    for i in x:
        date.append(datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f"))
    return date



def num_older_than(age: float, patient_dict: Dict[str, Union[str, float]]) -> int:
    """Return the number of patients older than a given age (in years).

    Assumptions:
    - the user will pass the output of "parse_data" into this function
        as "patient_dict"
    - the file that was passed into the "parse_data" function will contain
        the fields PatientDateOfBirth and PatientID.

    Computational Complexity: creating the "dates" object takes constant time,
    and then we iterate over the length of the object, which takes N time, to
    get the date in the format we need. Creating the "today" object takes constant time.
    The operation of appending to lists takes constant time, but this occurs 2N times;
    once for the "age_days" list, and once for the "age_years" list. Moving on to the next
    step, we iterate over the length of the "patient_dict" list, which takes N time.
    The if statement happens N times as well because it is inside this loop, giving us 2N.
    Finally, we append to the "older" list N times, resulting in 3N.  Our big-O notation is therefore
    O(2N+N+3N) and after dropping the constant factor, we yield O(N) complexity.
    """

    today = datetime.datetime.today()
    age_days = []
    age_years = []
    brth_date = date_time(patient_dict["PatientDateOfBirth"])
    for i in range(len(brth_date)):
        age_days.append(today - brth_date[i])
        age_years.append(age_days[i].days / 365.25)
    patient_dict["PatientAge"] = age_years

    older = []
    for i in range(len(patient_dict["PatientAge"])):
        if patient_dict["PatientAge"][i] > age:
            older.append(patient_dict["PatientID"][i])
    return len(older)


def sick_patients(lab: str, gt_lt: str, value: float, lab_dict: Dict[str, Union[str, float]]) -> list:
    """Return a (unique) list of patients who have a given test with value
    above (">") or below ("<") a given level.

    Assumptions:
    - the user will pass the output of "parse_data" into this function
        as "lab_dict"
    - the file that was passed into the "parse_data" function will contain
        the fields PatientID, LabValue and LabName.

    Computational Complexity: this function start with an empty list which is
    constant time. Then we iterate over the length of the "lab_dict" list, which
    takes N time.  The next four if statements followed by appending to the 
    "values" list all take constant time, but each operation need to be repeated 
    for each N, because we are inside the for loops, resulting in 5N.  
    We repeat a similar process in the elif operation which adds an
    additional 4N to the total. Our big-O notation is therefore O(N+5N+4N)
    and after dropping the constant factor, we yield O(N) complexity.
    """

    values = []
    for i in range(len(lab_dict["PatientID"])):
        if lab_dict["LabName"][i] == lab:
            if gt_lt == ">":
                if lab_dict["LabValue"][i] > str(value):
                    if lab_dict["PatientID"][i] not in values:
                        values.append(lab_dict["PatientID"][i])
            elif gt_lt == "<":
                if lab_dict["LabValue"][i] < str(value):
                    if lab_dict["PatientID"][i] not in values:
                        values.append(lab_dict["PatientID"][i])
            else:
                raise ValueError("Please enter a valid operator")
    print(len(values))


def age_at_admis(patient_id:str) -> float:
    age_days = []
    age_years = []
    admis_date = date_time(lab_dict["LabDateTime"])
    brth_date = date_time(patient_dict["PatientDateOfBirth"])
    for i in range(len(admis_date)):
        for j in range(len(brth_date)):
            if lab_dict["PatientID"][i] == patient_dict["PatientID"][j]:
                age_days.append(admis_date[i] - brth_date[j])
                age_years.append(age_days[i].days/365.25)
            lab_dict["PatientAgeAtAdmission"] = age_years
    
    first_admis = datetime.datetime.today()
    for i in range(len(lab_dict["PatientID"])):
        if lab_dict["PatientID"][i] == patient_id:
            if admis_date[i] < first_admis:
                first_admis = admis_date[i]
    for i in range(len(lab_dict["PatientID"])):
        if first_admis == admis_date[i]:
            return(lab_dict["PatientAgeAtAdmission"][i])



if __name__ == "__main__":
    patient_dict = parse_data(
        "/mnt/c/Users/sdona/Documents/Duke/22Spring"
        "/821BIOSTAT/03Assignment/PatientCorePopulatedTable.txt"
    , "\t")
    lab_dict = parse_data(
        "/mnt/c/Users/sdona/Documents/Duke/22Spring"
        "/821BIOSTAT/03Assignment/LabsCorePopulatedTable.txt"
    , "\t")
    # print(num_older_than(52, patient_dict))
    # print(sick_patients("METABOLIC: ALBUMIN", ">", 5.9, lab_dict))
    print(age_at_admis("03A481F5-B32A-4A91-BD42-43EB78FEBA77"))
