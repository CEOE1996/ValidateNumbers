import re

def ValidNumber(n):
    match = re.search("^[7-9]\d{9}$", n)
    if match: return "YES"
    return "NO"

x = input("")
if not x.isnumeric() or not 0 < int(x) <= 10:
    print("Invalid Input")

else:
    result = []

    for i in range(int(x)):
        result.append(ValidNumber(input("")))

    for i in result:
        print(i)
