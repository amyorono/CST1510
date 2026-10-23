"""
RECORD CHECK  -  my version
===========================

Name  :  Amy
Lane  :  AI     (delete two)
Date  :  21/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """Fills the class and calls the records for you"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Calculates the percentage and returns the status"""
        p = self.value / self.limit * 100
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

with open("records.txt", "w") as f:
    f.write("survey_2026,1187,1200\n")
    f.write("survey_2026,1300,1200\n")
    f.write("survey_2026,1000,1200\n")

def load_records(path):
    """Reads the file specified line by line"""
    records = []
    with open(path) as r:
        for line in r:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records

records = load_records("records.txt")

for record in records:
    """loops over the records to print the report and the count limit then after"""
    if record.status() == "OVER LIMIT":
        Record.over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Dataset name: {record.label}")
    print(f"Rows loaded: {record.value}")
    print(f"Rows expected: {record.limit}")
    print(f"Status: {record.status()}")
    print("=" * 34)

print(f"Number of times over limit: {Record.over_limit_count}")



