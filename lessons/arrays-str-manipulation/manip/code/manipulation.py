def str_replace(word, bad_str, good_str):
    # use the replace to fix the mistake

    return word

bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
good_memo = str_replace(bad_memo, put_bad_str_here, put_good_str_here)

def str_split(raw_str, row_str, column_str):
    # use the split function to make rows
    csv_files_rows = use_split_for_rows_here
    # use the split function to make columns
    csv_files_columns = []
    for csv_files_row in csv_files_rows:
      csv_files_columns.append(use_split_for_columns_here)

    return csv_files_columns

raw_csv = 'Employee Name:ID:Salary\tJane Doe:4536:56000\tJack Kemp:7891:65000'
split_rows_columns_csv = str_split(raw_csv, put_row_str_here, put_column_str_here)
