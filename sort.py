import csv
import sys

def sort_csv_by_first_column():
    reader = csv.reader(sys.stdin)
    header = next(reader, None)  # Read the header row if it exists
    sorted_data = sorted(reader, key=lambda row: row[0].lower())  # Sort by the first column (case-insensitive)
    writer = csv.writer(sys.stdout)

    if header:
        writer.writerow(header)  # Write the header row first
    writer.writerows(sorted_data)

if __name__ == "__main__":
    sort_csv_by_first_column()
