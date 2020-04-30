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

#### Evaluation

Lets test your understanding of the replace function. In the code subfolder.
```
lesson-plan
  > lessons
    > arrays-str-manipulation
      > code
        - manipulation.py
```
You will find `manipulation.py`
