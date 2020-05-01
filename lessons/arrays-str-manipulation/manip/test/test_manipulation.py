# test_capitalize.py

from manip.code.manipulation import good_memo
from manip.code.manipulation import split_rows_columns_csv
import pytest

def test_memo():
    bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
    correct_memo = bad_memo.replace('  ', ' ')
    assert correct_memo == good_memo

def test_csv():
    raw_csv = 'Employee Name:ID:Salary\tJane Doe:4536:56000\tJack Kemp:7891:65000'
    rows = raw_csv.split('\t')
    correct_columns = []
    for row in rows:
        correct_columns.append(row.split(':'))
    assert correct_columns == split_rows_columns_csv
