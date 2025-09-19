import csv
from pathlib import Path
import numbers

CSV_FILE = Path(__file__).with_name("numbers.csv")

if not CSV_FILE.exists():
    CSV_FILE.write_text("value\n10\n20\n5\ndrie\nhuhi\n18.59948945", encoding="utf-8")

with CSV_FILE.open(newline="",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    total = 0
    for r in reader:
        try:
            print(float(r["value"]))
            total += float(r["value"])
        except:
            print(r["value"] +  " is not a valid value, line skipped")
print("Total: ", total)

# with CSV_FILE.open(newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     total = sum(int(r["value"]) for r in reader)
# print("Total:", total)