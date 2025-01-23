# test_main.py
from main import fizzbuzz

def test_fizz():
    assert fizzbuzz(3) == "Fizz"  # Input 3 should return "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"  # Input 5 should return "Buzz"
