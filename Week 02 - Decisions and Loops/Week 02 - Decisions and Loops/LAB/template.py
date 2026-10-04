"""
RECORD CHECK  -  my version
===========================

Name  :  Amy
Lane  :  Cyber     (delete two)
Date  :  2/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit = 0
while True:
    Source_IP = input("Enter the Source IP (or 'quit' to exit): ")      
    if Source_IP == "quit":
        break
    Failed_logins = float(input("Enter the Failed logins: "))     
    Total_attempts = float(input("Enter the Total attempts: "))     
    difference = Total_attempts - Failed_logins   
    percent = (Failed_logins / Total_attempts * 100)       
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    print(status)
    print("=" * 34)
    print(f"  RECORD CHECK  -  {Source_IP}")
    print(f"Failed logins: {Failed_logins:>10.2f}") 
    print(f"Total attempts: {Total_attempts:>10.2f}")
    print(f"Difference: {difference:>10.2f}")
    print(f"Percentage: {percent:>10.2f}%")
    print("=" * 34)
print("Number of records that came back over limit: ", over_limit)










#error: ZeroDivisionError: division by zero for percent

