# parse-medline

From NCBI MEDILNE format:

    PMID- 14512816
    TI  - Current treatment for Alzheimer disease and future prospects.
    [etc.]

to pythonic list of records:

    [
        {
            'PMID': '14512816',
            'TI': 'Current treatment for Alzheimer disease and future prospects.',
            ...
        }
    ]

---

    git clone

python```
    from parse_medline import medline_parser
    
    records = medline_parser(medline_data)
```