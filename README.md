## Installation
```
import datetime
from typing import Dict, Union
```

## Clone the repo
1. click Code ; click SSH ; copy the address by clicking the icon on the right that looks like a clipboard
2. In the command line type &quot;git clone&quot; and paste what you copied from GitHub ; Enter ; type &quot;cd ehr-analysis&quot; ; Enter

## File Format
Files may be in any tabular form as long as the first row of the files contain the column headers.

## API Description
num_older_than():
Returns the number of patients older than a given age (in years).

sick_patients():
Returns a (unique) list of patients who have a given test with value above (">") or below ("<") a given level.

age_at_admis():
Return the age at first admission of any given patient.

## Testing Instructions
  1. In the command line, type "pytest test_ehr.py --cov"

## Execute functions
1. Open ehr_analysis.py
2. Below "if \_\_name\_\_=="\_\_main\_\_":
     1. Use examples below and replace with desired values for each function argument
     2. ValueError will appear if value entered is not valid

### Examples
    ```
    # num_older_than:
    print(num_older_than(age=68, patient_dict=patient_dict))

    # sick_patients:
    print(sick_patients(lab="METABOLIC: ALBUMIN", gt_lt=">", value=5.9, lab_dict=lab_dict))

    # age_at_admis:
    print(age_at_admis(patient_id="4C201C71-CCED-40D1-9642-F9C8C485B854", lab_dict=lab_dict, patient_dict=patient_dict)))
    ```
    
  Valid lab values for sick_patients():
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
