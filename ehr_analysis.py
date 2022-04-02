from datetime import datetime
import sqlite3
import os
from typing import List


def parse_data(
    database: sqlite3.Connection,
    patient_file: sqlite3.Connection,
    lab_file: sqlite3.Connection,
    delimiter: str,
) -> None:
    """Parses the patient and lab files and creates tables in a database."""
    os.remove(database)

    con = sqlite3.connect(database)
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS patients(
            [PatientID] TEXT PRIMARY KEY,
            [PatientGender] TEXT,
            [PatientDateofBirth] TEXT,
            [PatientRace] TEXT,
            [PatientMaritalStatus] TEXT,
            [PatientLanguage] TEXT,
            [PatientPopulationPercentageBelowPoverty] TEXT
            )"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS labs(
            [LabID] INTEGER PRIMARY KEY AUTOINCREMENT,
            [PatientID] TEXT,
            [AdmissionID] TEXT,
            [LabName] TEXT,
            [LabValue] TEXT,
            [LabUnits] TEXT,
            [LabDateTime] TEXT
            )"""
    )

    patient_data = open(patient_file, "r", encoding="UTF-8-sig").readlines()
    lab_data = open(lab_file, "r", encoding="UTF-8-sig").readlines()
    for patient_row in patient_data[1:]:
        patient_info = patient_row.strip("\n").split(delimiter)
        patient_table = cur.executemany(
            "INSERT INTO patients VALUES (?,?,?,?,?,?,?)", [patient_info]
        )
    for lab_row in lab_data[1:]:
        lab_info = lab_row.strip("\n").split(delimiter)
        lab_table = cur.executemany(
            "INSERT INTO"
            " labs(PatientID,AdmissionID,LabName,LabValue,LabUnits,LabDateTime)"
            " VALUES (?,?,?,?,?,?)",
            [lab_info],
        )

    con.commit()
    cur.close()


def date_time(date_time_field: str) -> datetime:
    """Converts a string to a datetime object."""
    return datetime.strptime(date_time_field[0][0], "%Y-%m-%d %H:%M:%S.%f")


def age(patient_id: str, database: sqlite3.Connection) -> float:
    """Returns the age of a patient."""
    con = sqlite3.connect(database)
    cur = con.cursor()
    DOB = cur.execute(
        "SELECT PatientDateofBirth FROM patients WHERE PatientID = ?", (patient_id,)
    ).fetchall()
    DOB = date_time(DOB)
    age = round((datetime.today() - DOB).days / 365.25, 2)
    con.close()
    return age


def age_at_admis(patient_id: str, database: sqlite3.Connection) -> float:
    """Returns the age of a patient at first admission."""
    con = sqlite3.connect(database)
    cur = con.cursor()
    lab_date = cur.execute(
        "SELECT min(LabDateTime) FROM labs WHERE PatientID = ?", (patient_id,)
    ).fetchall()
    DOB = cur.execute(
        "SELECT PatientDateofBirth FROM patients WHERE PatientID = ?", (patient_id,)
    ).fetchall()
    lab_date = date_time(lab_date)
    DOB = date_time(DOB)
    age_at_admis = round((lab_date - DOB).days / 365.25, 2)
    con.close()
    return age_at_admis


def num_older_than(given_age: float, database: sqlite3.Connection) -> int:
    """Returns the number of patients who are older than a given age (in years)."""
    con = sqlite3.connect(database)
    cur = con.cursor()
    patient_ids = cur.execute("SELECT DISTINCT PatientID FROM patients").fetchall()
    ages = []
    for i in range(len(patient_ids)):
        patient_age = age(patient_ids[i][0], database)
        if patient_age > given_age:
            ages.append(patient_age)
    return len(ages)


def sick_patients(
    lab: str, gt_lt: str, value: float, database: sqlite3.Connection
) -> str:
    """Returns a (unique) list of patients who have a given test with value
    above (">") or below ("<") a given level."""
    con = sqlite3.connect(database)
    cur = con.cursor()
    if gt_lt == ">":
        sick_patients = cur.execute(
            "SELECT DISTINCT PatientID FROM labs WHERE LabName = ? AND LabValue > ?",
            (lab, value),
        ).fetchall()
    elif gt_lt == "<":
        sick_patients = cur.execute(
            "SELECT DISTINCT PatientID FROM labs WHERE LabName = ? AND LabValue < ?",
            (lab, value),
        ).fetchall()
    else:
        raise ValueError("Please enter a valid operator")
    con.close()
    return sick_patients


if __name__ == "__main__":
    parse_data(
        "SampleDB.db",
        "PatientCorePopulatedTable.txt",
        "LabsCorePopulatedTable.txt",
        "\t",
    )
