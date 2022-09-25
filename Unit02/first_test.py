# pytest working in WSL terminal
import pytest

def func(x):
    return x + 5

def test_method():
    # assert func(3) == 5 # this will cause failed test
    assert func(3) == 8
