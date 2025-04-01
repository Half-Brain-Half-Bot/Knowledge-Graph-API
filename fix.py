import csv
import sys

def fix_knowledge_object_prefix_stdin_stdout():
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)
    processed_lines = 0
    modified_lines = 0

    for row in reader:
        processed_lines += 1
        if row:
            first_column = row[0].strip()
            if not first_column.startswith("Knowledge Object: "):
                row[0] = "Knowledge Object: " + first_column
                modified_lines += 1
        writer.writerow(row)

    print(f"Processed {processed_lines} lines.", file=sys.stderr)
    print(f"Modified {modified_lines} lines.", file=sys.stderr)

if __name__ == "__main__":
    fix_knowledge_object_prefix_stdin_stdout()
