import pytest
from helloworld import *

def test_hello():
    results = hello()
    assert results == "Hello"
