import csv
import sys
import re

def quote_and_trim_csv_stdin_stdout():
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)

    for row in reader:
        processed_row = []
        for field in row:
            trimmed_field = field.strip()
            processed_row.append(trimmed_field)
        writer.writerow(processed_row)

if __name__ == "__main__":
    quote_and_trim_csv_stdin_stdout()
