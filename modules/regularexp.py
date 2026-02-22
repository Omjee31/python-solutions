import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")

if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match:", match.group(0))
    print("Month:", match.group(1))
    print("Day:", match.group(2))
else:
    print("The regex pattern does not match.")
