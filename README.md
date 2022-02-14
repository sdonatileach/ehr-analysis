## Installation
```
import datetime
from typing import Dict, Union
```

## Clone the repo
1. click Code ; click SSH ; copy the address by clicking the icon on the right that looks like a clipboard
2. In the command line type &quot;git clone&quot; and paste what you copied from GitHub ; Enter ; type &quot;cd&quot; and \"ehr-analysis\" ; Enter

## File Formats
Files may be in any tabular form, This analysis assumes the first row of the files contain the column headers.

## API Description

## Execute functions
1. In the command line type &quot;code ehr_analysis.py&quot;; Enter
2. Once open, uncomment and use lines 184, 186 and 188 of ehr_analysis accordingly
```
# num_older_than:
print(num_older_than(age=__, patient_dict=patient_dict))

# sick_patients:
print(sick_patients(lab=__, gt_lt=__, value=__, lab_dict=lab_dict))

# age_at_admis:
print(age_at_admis(patient_id=__, lab_dict=lab_dict, patient_dict=patient_dict)))
```

## Examples:

All possible lab values:
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
