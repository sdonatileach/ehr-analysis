"""Test EHR analysis."""
import pytest
from ehr_analysis import (
    parse_data,
    date_time,
    num_older_than,
    sick_patients,
    age_at_admis,
)


def test_parse_data():
    """Test parse_data()."""
    assert len(parse_data("PatientSampleData.txt", "\t")) == 7
    assert len(parse_data("LabsSampleData.txt", "\t")) == 6


def test_date_time():
    """Test date_time()."""
    assert len(date_time(patient_dict["PatientDateOfBirth"])) == 5
    assert len(date_time(lab_dict["LabDateTime"])) == 10


def test_num_older_than():
    """Test num_older_than()."""
    assert num_older_than(51.2, patient_dict) == 5


def test_sick_patients():
    """Test sick_patients()."""
    assert len(sick_patients("CBC: RDW", ">", 0.5, lab_dict)) == 3
    with pytest.raises(ValueError):
        sick_patients("hello", ">", 0.5, lab_dict)
    with pytest.raises(ValueError):
        sick_patients("CBC: RDW", "?", 0.5, lab_dict)


def test_age_at_admis():
    """Test age_at_admis()."""
    assert (
        age_at_admis("4C201C71-CCED-40D1-9642-F9C8C485B854", lab_dict, patient_dict)
        == 29.41
    )
    with pytest.raises(ValueError):
        age_at_admis("42", lab_dict, patient_dict)


patient_dict = parse_data("PatientSampleData.txt", "\t")
lab_dict = parse_data("LabsSampleData.txt", "\t")
