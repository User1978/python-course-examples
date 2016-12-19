"""
Write a python program that takes a CSV file
reads it line by line and prints each line
with first and second columns reversed.

Sample input:
    Shana,Sargent,shanasargent@isoswitch.com
    Witt,Hampton,witthampton@zaphire.com
    Morgan,Grant,morgangrant@lotron.com

Sample output:
    Sargent,Shana,shanasargent@isoswitch.com
    Hampton,Witt,witthampton@zaphire.com
    Grant,Morgan,morgangrant@lotron.com
"""
import sys
import re

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    for line in f:
        #I used the following example from the text book:
        #print re.sub(r'\b\w', lambda m: m.group(0).upper(), line)
        #It yields the required result, however, I'm not sure whether this is correct
        print re.sub(r'([^,]+),([^,]+)', lambda m: m.group(2) + "," + m.group(1), line)
