# parse-medline

## Overview

From NCBI MEDILNE format:

    PMID- 14512816
    TI  - Current treatment for Alzheimer disease and future prospects.
    ...

to pythonic list of records:

    [
        {
            'PMID': '14512816',
            'TI': 'Current treatment for Alzheimer disease and future prospects.',
            ...
        }
    ]

## Usage

Clone the repo:

    git clone https://github.com/cyclecycle/parse-medline.git parse_medline

Import and use:

```python
    from parse_medline import medline_parser
    
    records = medline_parser(medline_data)
```