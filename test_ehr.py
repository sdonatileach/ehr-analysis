"""Test EHR analysis."""
import pytest
from ehr_analysis import parse_data, create_data_dict, date_time, num_older_than, sick_patients, age_at_admis

patient_dict = create_data_dict("Patients.txt")
lab_dict = create_data_dict("Labs.txt")

def test_parse_data():
    """Test parse_data()."""
    # with pytest.raises(ValueError):
    #     add("hello", 5)

# patient_dict = parse_data(
# "/mnt/c/Users/sdona/Documents/Duke/22Spring"
# "/821BIOSTAT/03Assignment/PatientCorePopulatedTable.txt"
# , "\t")
# lab_dict = parse_data(
# "/mnt/c/Users/sdona/Documents/Duke/22Spring"
# "/821BIOSTAT/03Assignment/LabsCorePopulatedTable.txt"
# , "\t")

def test_date_time():
    """Test date_time()."""
    pass

def test_num_older_than():
    """Test num_older_than()."""
    pass

def test_sick_patients():
    """Test sick_patients()."""
    assert len(sick_patients(lab="METABOLIC: ALBUMIN", gt_lt=">", value= 5.9, lab_dict=lab_dict)) == 42
    assert len(sick_patients(lab="URINALYSIS: WHITE BLOOD CELLS", gt_lt ="<", value=.5, lab_dict=lab_dict)) == 86
    with pytest.raises(ValueError):
        sick_patients(lab="hello", gt_lt=">", value=5, lab_dict=lab_dict)
    with pytest.raises(ValueError):
        sick_patients(lab="METABOLIC: ALBUMIN", gt_lt="?", value= 5.9, lab_dict=lab_dict)
    


def test_age_at_admis():
    """Test age_at_admis()."""
    assert age_at_admis("03A481F5-B32A-4A91-BD42-43EB78FEBA77",lab_dict,patient_dict) == 20.8
    pass
