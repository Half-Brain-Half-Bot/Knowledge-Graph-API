import csv
import sys
import re

def extract_sort_key(label):
    label = label.removeprefix("Knowledge Object: ").strip()
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', label)]

def sort_csv_by_first_column():
    reader = csv.reader(sys.stdin)
    sorted_data = sorted(reader, key=lambda row: extract_sort_key(row[0]))
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
    writer.writerows(sorted_data)

if __name__ == "__main__":
    sort_csv_by_first_column()
