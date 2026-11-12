import csv

def read_sales(filepath):
    with open(filepath) as f_read:
            reader = csv.DictReader(f_read)
            headers = list(reader.fieldnames)
            rows = list(reader)  # Loads all rows into memory before the file closes
    return headers, rows

def write_csvs(filepath,headers,rows):
      with open(filepath, 'w') as f_write:
            writer = csv.DictWriter(f_write,fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)  # Writes all rows at once