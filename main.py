from revenue import calculate_revenue
from file_handler import read_sales,write_csvs
from validate import validate_rows

valid_rows,invalid_rows = validate_rows()

def calculate():
    valid_path = '/Users/macbook/Documents/Learning/DataProcessor/Files/Valid.csv'
    total_revenue = 0
    headers, rows = read_sales(valid_path)
    for row in rows:
        revenue  = calculate_revenue(row['quantity'],row['price'])
        row["Revenue"] = revenue
        total_revenue += revenue


    write_csvs(valid_path,headers,rows)

    print(f"Total Revenue : {total_revenue} | Valid Transactions : {valid_rows} | Invalid Transactions : {invalid_rows}")



# 6. Actually execute the function
if __name__ == "__main__":
    calculate()