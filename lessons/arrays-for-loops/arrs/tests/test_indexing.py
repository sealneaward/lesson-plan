# test_capitalize.py

from arrs.code.indexing import indexes_of_first, indexes_of_last, names
import pytest

def test_first():
    correct_indexes = []
    for i, name in enumerate(names):
        if name[0] == 'R':
            correct_indexes.append(i)
    assert correct_indexes == indexes_of_first

def test_last():
    correct_indexes = []
    for i, name in enumerate(names):
        if name[-1] == 'r':
            correct_indexes.append(i)
    assert correct_indexes == indexes_of_last
