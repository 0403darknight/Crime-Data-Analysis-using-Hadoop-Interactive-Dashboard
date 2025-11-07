#!/usr/bin/env python3
import sys

current_type = None
total = 0

for line in sys.stdin:
    crime_type, count = line.strip().split('\t')
    count = int(count)

    if current_type == crime_type:
        total += count
    else:
        if current_type:
            print(f"{current_type},{total}")
        current_type = crime_type
        total = count

if current_type:
    print(f"{current_type},{total}")
