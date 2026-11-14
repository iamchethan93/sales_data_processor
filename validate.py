from revenue import calculate_revenue
from file_handler import read_sales,write_csvs

sales_path = '/Users/macbook/Documents/Learning/DataProcessor/Files/sales.csv'
valid_path = '/Users/macbook/Documents/Learning/DataProcessor/Files/Valid.csv'
invalid_path = '/Users/macbook/Documents/Learning/DataProcessor/Files/InValid.csv'
    
def validate_rows():
    
# 1. Call read_sales() and unpack the returned tuple
    headers, rows = read_sales(sales_path)

# 2. Initialize counters and storage lists before the loop
    valid_transactions,invalid_transactions = 0,0
    valid_rows = []
    invalid_rows = []

# 3. Process all rows in memory
    for row in rows:
        try:
            if int(row['quantity']) > 0 and int(row['price']) >= 0:
                # revenue = calculate_revenue(row['quantity'],row['price'])
                # row["Revenue"]= revenue
                # total_revenue += revenue
                valid_transactions += 1
                valid_rows.append(row)
            else:
                print(f"Invalid transaction: {row['transaction_id']} | Quantity : {row['quantity']}")
                row["Reason"] = 'Quantity must be greater than 0, price cannot be negative'
                invalid_transactions += 1
                invalid_rows.append(row)
                
        except ValueError:
            print(f"Invalid transaction: {row['transaction_id']} | Quantity : {row['quantity']}")
            row["Reason"] = 'Qudntity or price is not numeric'
            invalid_transactions += 1
            invalid_rows.append(row)           

# 4. Write all collected rows once after the loop finishes
    write_csvs(valid_path, headers + ["Revenue"], valid_rows)
    write_csvs(invalid_path, headers + ["Reason"], invalid_rows)
    return valid_transactions , invalid_transactions