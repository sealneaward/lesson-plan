# test_capitalize.py

from .manipulation import good_memo
import pytest

def test_memo():
    bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
    correct_memo = bad_memo.replace('  ', ' ')
    assert correct_memo == good_memo
