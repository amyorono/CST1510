"""
RECORD CHECK  -  my version
===========================

Name  : Amy
Lane  :  IT    
Date  : 14/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns the status of the percentage calculated"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check_record(GB_used, GB_total):
    """calculates the difference and percentage"""
    difference = GB_total - GB_used
    percent = GB_used / GB_total * 100
    status = status_of(percent)
    return difference, percent, status
def print_report(hostname, GB_used, GB_total, difference, percent, status):
    """Prints Report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"GB used: {GB_used:>10.2f}")
    print(f"GB total: {GB_total:>10.2f}")
    print(f"Difference: {difference:>10.2f}")
    print(f"Percent: {percent:>10.2f}")
    print(f"Status: {status}")
    print("=" * 34)



"""Creates the file containing the data"""
with open("datafile.txt", "w") as file:
    file.write("srv-01, 87, 120\n")



def load_records(path):
    """Reads each line in the file and adds them to a dict containing key and value"""
    records = []
    with open(path) as f:
        for line in f:
            hostname, GB_used, GB_total = line.strip().split(", ")
            records.append({
                'label': hostname,
                'value': float(GB_used), 
                'limit': float(GB_total)
            })
    return records

            
records = load_records("datafile.txt")
over_limit = 0
"""Writes the file containing the data of the report and opens the file on to the terminal"""     
with open("results2.txt", "w") as t:
    for record in records:
        hostname = record['label']
        GB_used = record['value']
        GB_total = record['limit']

        difference, percent, status = check_record(GB_used, GB_total)
        print_report(hostname, GB_used, GB_total, difference, percent, status)
        if status == "OVERLIMIT":
            over_limit += 1
        t.write(f"{hostname}, {status}\n")

try:
    with open("results2.txt") as r:
        print(r.read())
except FileNotFoundError:
    print(list(), "File is missing")
print("Number of times over limit:", over_limit)
   
