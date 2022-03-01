"""Test EHR classes."""

import pytest
from classes import (
    parse_data,
    datetime
)


def test_parse_data():
    """Test parse_data function."""
    patient_dict = parse_data("PatientSampleData.txt", "LabsSampleData.txt", "\t")
    patient = patient_dict["80D356B4-F974-441F-A5F2-F95986D119A2"]
    assert patient.DOB == datetime(1938, 3, 6, 18, 24, 18, 297000)
    for i in range(len(patient.labs)):
        assert(patient.labs[i].lab_date) == "1990-05-09 08:11:28.813" or \
        "1990-05-09 13:29:31.897"
    assert patient.age == 83.98
    assert patient.age_at_admis == 52.17
    
