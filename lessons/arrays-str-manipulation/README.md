# String Manipulation

With Strings, there are many functions that can be used to manipulate the contents to reach and end goal. There may be restrictions on data, where only lowercase characters are acceptable in a username, or where we cannot have spaces in the name of a github repository.

As you go on further and further with Python, you will see the need for data manipulation on a larger scale, but for today, we are going to learn about String manipulation, formatting, concatenation, etc.

### Manipulation

Have you used Microsoft Word before when preparing an essay? Chances are you use Spell Check in Word to correct some words that you miss spelled. You either fixed a single misspelled word, or you may have fixed a word that was misspelled multiple times throughout your document.

In Python, fixing or `manipulating` Strings is very straight forward and easy. With standard String function build into the language, you can easily change Strings to have the content or the formatting expected.

The most common form of String manipulation is replacing.
Say you are editing your colleagues work and noticed that they double spaced the start of each sentence after a period, you can easily edit that document and replace those double spaces with single spaces in Python using the `replace()` method.

The replace method can be relatively described in this definition.
This is a rough description in sudo code.
```py
def replace(self, bad_str, good_str):
  for all occurences of bad_str in self:
    replace bad_str with good_str
  return self
```

```py
incorrect_memo = `Memo to all staff.  We ran out of toilet paper and need more.  My cat may have ate it all`

# We can now use the replace() method to make changes to the string and place it in a new variables.
correct_memo = incorrect_memo.replace('  ', ' ')
```

Here, we identified the incorrect sequence of Characters as `  ` and gave the `replace()` method the correct sequence of Characters as ` ` to replace it with.

There are very few restrictions on the `replace()` method, as long as both arguments given are Strings, then you are fine.

### Splitting

Splitting a String is another common form of String manipulation. Splitting Strings is the practice of creating an Array of Strings from a single String. In order to split a String, you must first determine the sequence of Characters/String that will use to denote the seperation.

If you are familiar with different Microsoft Excel file types, a common data sheet file name is `CSV`. CSV, or Comma Seperated Values, is a file in which the data in columns is seperated by a comma `,` and the rows are usually seperated by a newline character `\n`.

For example, this can be considered a CSV file.

```
Employee Name, ID, Salary \n
Sally Jones, 1234, 60000 \n
Mike Smith, 4567, 55000 \n
```

Using the split method, we can seperate the rows, then separate the columns.
This is a rough description in sudo code.
```py
def split(self, split_str):
  split_arr = []
  for all occurences of split_str in self:
    add string up to occurence in split_array
  return split_arr
```

```py
# this is a sample input read from a .csv file
csv_file_str = 'Employee Name,ID,Salary\nSally Jones,1234,60000\nMike Smith, 4567,55000\n'

# we now get an array of rows [ 'Employee Name,ID,Salary', 'Sally Jones, 1234,60000', '...']
csv_files_rows = csv_file_str.split('\n')
print('These are the rows: ' + csv_files_rows)

# we can create a 2D array with rows and columns filled with data from rows
# append is the action of adding a single object to an array
csv_files_columns = []
for csv_files_row in csv_files_rows:
  csv_files_columns.append(csv_files_row.split(','))

# we now get an array of rows  and columns  [['Employee Name','ID','Salary'], ['Sally Jones','1234','60000'], ['...', '...']]
print('These are the rows and columns: ' + csv_files_rows)
```

# Evaluation

Lets test your understanding of the replace function and the split function.
In order to properly trigger the automated tests, you will need to clone this repository and checkout a specific branch to commit your changes to.

1. Clone the repository

```
git clone git@github.com:sealneaward/lesson-plan.git
```

2. Checkout the branch to make your changes on.

```
git checkout arrays-str-manipulation
```

In the code subfolder.
```
lesson-plan
  > lessons
    > arrays-str-manipulation
      > manip
        > code
          - manipulation.py
```
You will find `manipulation.py`

### Replace Evaluation

In `manipulation.py`, edit the code to replace the double spaces with single spaces.

```py
def str_replace(word, bad_str, good_str):
    # use the replace to fix the mistake

    return word

bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
good_memo = str_replace(bad_memo, put_bad_str_here, put_good_str_here)
```

### Split Evaluation

In `manipulation.py` edit the code to create a `CSV` like 2D array with columns and spaces, make sure to use the specific characters that are delimiting the rows and columns.

```py
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
```

### Finishing

Once you are finished, you will need to commit and push your code to the `arrays-str-manipulation` branch. Use a unique commit message so you can track it in the tests results. Once done, you can visit the [action page](https://github.com/sealneaward/lesson-plan/actions) to view your test results.
