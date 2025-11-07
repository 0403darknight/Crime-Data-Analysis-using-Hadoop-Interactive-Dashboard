#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)
for row in reader:
    if len(row) >= 6:
        crime_type = row[5]
        print(f"{crime_type}\t1")
