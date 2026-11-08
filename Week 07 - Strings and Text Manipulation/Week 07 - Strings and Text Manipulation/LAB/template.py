"""
RECORD CHECK  -  my version
===========================

Name  : Amy
Lane  : IT      (delete two)
Date  : 02/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Cleans and parses a raw line into a dictionary."""
    raw_line = raw_line.strip()
    hostname_part, rest = raw_line.split(",", 1)
    hostname = hostname_part.strip().lower()
    dict = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        value = float(value)
        dict[key.strip()] = value
    return {'hostname': hostname, 
            'used_gb': dict['used'], 
            'total_gb': dict['total']
            }
def status_of(record_dict):
    """Determines the status of a record based on its 'used' and 'total' values."""
    used = record_dict["used_gb"]
    total = record_dict["total_gb"]
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


with open("records.txt", "w") as w: 
    w.write("  Srv-01 , used=87 , total=100  \n")
    w.write("Srv-02,used=45,total=100\n")
    w.write("  Srv-03 , used=140 , total=100  \n")
    w.write("Srv-04,used=30,total=100\n")
    w.write("    Srv-05 , used=98 , total=100    \n")

records = []
with open("records.txt", "r") as f:
    for line in f:
        records.append(line)


flagged_count = 0
for record in records:
    parsed_record = parse_line(record)
    status = status_of(parsed_record)
    
    if status == "OVER LIMIT" or status == "WARNING":
        flagged_count += 1

    print(f"Record: {parsed_record}, Status: {status}")

print(f"Records flagged: {flagged_count} out of {len(records)} records")
