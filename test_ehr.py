"""Test EHR classes and functions."""

import pytest
from ehr_analysis import (
    datetime,
    parse_data,
    date_time,
    age,
    age_at_admis,
    num_older_than,
    sick_patients,
)

database = "SampleDB.db"

def test_parse_data():
    """Test parse_data function"""
    with pytest.raises(FileNotFoundError):
        parse_data(database, "mistake.txt", "LabsSampleData.txt", "\t")
    with pytest.raises(FileNotFoundError):
        parse_data(database, "PatientSampleData.txt", "mistake.txt", "\t")


def test_age():
    """Test age function."""
    parse_data(database, "PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert age("80D356B4-F974-441F-A5F2-F95986D119A2", database) == 84.1


def test_age_at_admis():
    """Test age_at_admis function."""
    parse_data(database, "PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert age_at_admis("80D356B4-F974-441F-A5F2-F95986D119A2", database) == 52.17


def test_num_older_than():
    """Test num_older_than function."""
    parse_data(database, "PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert num_older_than(65, database) == 4


def test_sick_patients():
    """Test sick patients function."""
    parse_data(database, "PatientSampleData.txt", "LabsSampleData.txt", "\t")
    assert len(sick_patients("CBC: RDW", ">", 13.5, database)) == 2
    with pytest.raises(ValueError):
        sick_patients("CBC: RDW", "?", 13.5, database)
