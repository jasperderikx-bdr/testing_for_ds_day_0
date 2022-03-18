import pytest

from src.math_functions import increment


# -- Exercise 1 --
# Make this test pass.
def test_increment_example() -> None:
    x = 10
    result = increment(x)
    expected_result = 5
    assert result == expected_result


# -- Exercise 2 --
# To avoid unexpected behaviour, we want increment() to raise an error when the input is a boolean.
# The test is written correctly. Make it pass, by expanding the implementation of increment().
def test_type_error_on_boolean() -> None:
    with pytest.raises(expected_exception=TypeError):
        increment(True)


# -- Exercise 3 --
# Similarly, we would like to test if a TypeError is raised when increment() is called with a string. Start by
# implementing this test.
# The problem that arises is that our type checker MyPy, won't accept this code. You can see this when you try to commit
# the code. Finish by making sure that MyPy ignores this (on purpose) iltyped line of code.
def test_type_error_on_string() -> None:
    pass
