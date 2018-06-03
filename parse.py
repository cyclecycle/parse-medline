import re

def medline_parser(data, clean=True):
    """Parse NCBI MEDLINE format string into a list of dictionaries:

    [
        {
            'PMID': 12345678,
            ...
        }
    ]

    Where a MEDLINE field descriptor is used multiple times in a record, the values appear in a list in the results.

    Arguments:
        data {string} -- MEDLINE data

    Keyword Arguments:
        clean {bool} -- Remove multi-spaces and newlines from text content (default: {True})

    Returns:
        [list] -- List of parsed records
    """
    data = data.lstrip('\n')
    records = data.split('\n\n')
    reg = re.compile(r'([A-Z]{2,4})\s*?-\s(.*?)(?=\n[A-Z]{2,4})', flags=re.S)  # Pattern which finds both MEDLINE tags and corresponding values
    results = []
    for record in records:
        found = reg.findall(record)
        d = {}
        for tag, val in found:
            if tag not in d:
                d[tag] = val
            elif not isinstance(d[tag], list):
                val_already = d[tag]
                del d[tag]
                d[tag] = [val_already, val]
            elif isinstance(d[tag], list):
                d[tag].append(val)
        results.append(d)
    if clean:
        def clean_string(s):
            s = s.replace('\n', '')
            s = re.sub(r'\s{2,}', ' ', s)
            return s
        cleaned = []
        for result in results:
            new_d = {}
            for key, val in result.items():
                if not isinstance(val, list):
                    new_d[key] = clean_string(val)
                elif isinstance(val, list):
                    new_d[key] = [clean_string(s) for s in val]
            cleaned.append(new_d)
        results = cleaned
    return results