"""Test EHR analysis."""
import pytest
from ehr_analysis import parse_data, date_time, num_older_than, sick_patients, age_at_admis

def test_parse_data():
    """Test parse_data()."""
    assert len(parse_data("PatientCorePopulatedTable.txt", "\t")) == 7
    assert len(parse_data("LabsCorePopulatedTable.txt", "\t")) == 6

def test_date_time():
    """Test date_time()."""
    assert len(date_time(patient_dict["PatientDateOfBirth"])) == 100
    assert len(date_time(lab_dict["LabDateTime"])) == 111483

def test_num_older_than():
    """Test num_older_than()."""
    assert num_older_than(68, patient_dict) == 42
    assert num_older_than(100.5, patient_dict) == 3

def test_sick_patients():
    """Test sick_patients()."""
    assert len(sick_patients("METABOLIC: ALBUMIN", ">",  5.9, lab_dict)) == 42
    assert len(sick_patients("URINALYSIS: WHITE BLOOD CELLS", "<", .5, lab_dict)) == 86
    with pytest.raises(ValueError):
        sick_patients("hello", ">", 5, lab_dict)
    with pytest.raises(ValueError):
        sick_patients("METABOLIC: ALBUMIN", "?",  5.9, lab_dict)

def test_age_at_admis():
    """Test age_at_admis()."""
    assert age_at_admis("03A481F5-B32A-4A91-BD42-43EB78FEBA77",lab_dict,patient_dict) == 20.8
    with pytest.raises(ValueError):
        age_at_admis("42",lab_dict,patient_dict)


patient_dict = parse_data("PatientCorePopulatedTable.txt","\t")
lab_dict = parse_data("LabsCorePopulatedTable.txt","\t")