"""Test EHR classes and functions."""

import pytest
from ehr_analysis import datetime, parse_data, num_older_than, sick_patients


def test_parse_data():
    """Test parse_data function."""
    patient_dict = parse_data("PatientSampleData.txt", "LabsSampleData.txt", "\t")
    patient = patient_dict["80D356B4-F974-441F-A5F2-F95986D119A2"]
    assert patient.DOB == datetime(1938, 3, 6, 18, 24, 18, 297000)
    for i in range(len(patient.labs)):
        assert (
            patient.labs[i].lab_date
        ) == "1990-05-09 08:11:28.813" or "1990-05-09 13:29:31.897"
    assert patient.age == 84.0
    assert patient.age_at_admis == 52.17


def test_num_older_than():
    """Test num_older_than function."""
    patient_dict = parse_data("PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert num_older_than(65, patient_dict) == 4
    pass


def test_sick_patients():
    """Test sick patients function."""
    patient_dict = parse_data("PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert len(sick_patients("CBC: RDW", ">", 13.5, patient_dict)) == 2
    with pytest.raises(ValueError):
        sick_patients("CBC: RDW", "?", 12, patient_dict)
    with pytest.raises(ValueError):
        sick_patients("hello", ">", 12, patient_dict)
