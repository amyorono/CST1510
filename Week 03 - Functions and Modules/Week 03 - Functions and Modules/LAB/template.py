"""
RECORD CHECK  -  my version
===========================

Name  : Amy
Lane  : IT
Date  : 8/10/2026

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
def check(GB_used, GB_total):
    """calculates the difference and percentage"""
    difference = GB_total - GB_used
    percent = GB_used / GB_total * 100
    return difference, percent
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


over_limit = 0
while True:
    hostname = input("Enter hostname: ")
    if hostname == "quit":
        break
    GB_used = float(input("Enter GB used: "))
    GB_total = float(input("Enter GB total: "))
    difference, percent = check(GB_used, GB_total)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit += 1
    print_report(hostname, GB_used, GB_total, difference, percent, status)

print("Number of times it was over limit: ", over_limit)


