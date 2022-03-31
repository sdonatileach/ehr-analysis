## Installation
```
import datetime
from typing import Dict, Union
```

## Clone the repo
1. click Code ; click SSH ; copy the address by clicking the icon on the right that looks like a clipboard
2. In the command line type "git clone" and paste what you copied from GitHub ; Enter ; type "cd ehr-analysis" ; Enter

## File Format
Files may be in any tabular form as long as the first row of the files contain the column headers.

## API Description
parse_data():
Parses the patient and lab files and creates tables in a database.

date_time():
Converts a string to a datetime object.

age():
Returns the age of a patient.

age_at_admis():
Returns the age of a patient at first admission.

num_older_than():
Returns the number of patients older than a given age (in years).

sick_patients():
Returns a (unique) list of patients who have a given test with value above (">") or below ("<") a given level.


## Testing Instructions
testing ehr_analysis.py
- In the command line, type "pytest test_ehr.py --cov"

## Execute functions
  1. Open ehr_analysis.py
  2. Below "if \_\_name\_\_=="\_\_main\_\_":
      1. Copy/paste examples below and replace with desired patient id/values
  3. In the command line, type "python ehr_analysis.py"
      1. ValueError will appear if value entered is not valid

### Examples
    ```
    # parse_data():
    parse_data("SampleDB.db", "PatientSampleData.txt", "LabsSampleData.txt", "\t")

    # age():
    print(age("80D356B4-F974-441F-A5F2-F95986D119A2", "SampleDB.db"))

    # age_at_admis():
    print(age_at_admis("80D356B4-F974-441F-A5F2-F95986D119A2", "SampleDB.db"))
    
    # num_older_than():
    print(num_older_than(65, "SampleDB.db"))

    # sick_patients():
    print(sick_patients("CBC: RDW", ">", 13.5, "SampleDB.db"))
    ```
    
  Valid lab names for sick_patients():
  - 'CBC: ABSOLUTE LYMPHOCYTES'
  - 'CBC: ABSOLUTE NEUTROPHILS'
  - 'CBC: BASOPHILS'
  - 'CBC: EOSINOPHILS'
  - 'CBC: HEMATOCRIT'
  - 'CBC: HEMOGLOBIN'
  - 'CBC: LYMPHOCYTES'
  - 'CBC: MCH'
  - 'CBC: MCHC'
  - 'CBC: MEAN CORPUSCULAR VOLUME'
  - 'CBC: MONOCYTES'
  - 'CBC: NEUTROPHILS'
  - 'CBC: PLATELET COUNT'
  - 'CBC: RDW'
  - 'CBC: RED BLOOD CELL COUNT'
  - 'CBC: WHITE BLOOD CELL COUNT'
  - 'METABOLIC: ALBUMIN'
  - 'METABOLIC: ALK PHOS'
  - 'METABOLIC: ALT/SGPT'
  - 'METABOLIC: ANION GAP'
  - 'METABOLIC: AST/SGOT'
  - 'METABOLIC: BILI TOTAL'
  - 'METABOLIC: BUN'
  - 'METABOLIC: CALCIUM'
  - 'METABOLIC: CARBON DIOXIDE'
  - 'METABOLIC: CHLORIDE'
  - 'METABOLIC: CREATININE'
  - 'METABOLIC: GLUCOSE'
  - 'METABOLIC: POTASSIUM'
  - 'METABOLIC: SODIUM'
  - 'METABOLIC: TOTAL PROTEIN'
  - 'URINALYSIS: PH'
  - 'URINALYSIS: RED BLOOD CELLS'
  - 'URINALYSIS: SPECIFIC GRAVITY'
  - 'URINALYSIS: WHITE BLOOD CELLS'
