bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
good_memo = bad_memo.replace("  ", " ")

print(good_memo)


raw_csv = 'Employee Name:ID:Salary\tJane Doe:4536:56000\tJack Kemp:7891:65000'

raw_csv_rows = raw_csv.split("\t")
raw_csv_columns = []
for x in raw_csv_rows:
    column_array = x.split(":")
    raw_csv_columns.append(column_array)


split_rows_columns_csv = raw_csv_columns

print(split_rows_columns_csv)
