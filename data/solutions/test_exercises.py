import pytest

from src.data_model import Employee, increment


# -- Exercise 1 --
# Make this test pass.
def test_increment_example() -> None:
    x = 10
    result = increment(x)
    expected_result = 11
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
# the code. Finish by making sure that MyPy ignores this (on purpose) ill typed line of code.
def test_type_error_on_string() -> None:
    with pytest.raises(expected_exception=TypeError):
        increment("text")  # type: ignore


# -- Exercise 4 --
# For demonstration purposes we've grouped the following two tests in a class, later we'll see why this can be handy.
# Pytest discovers tests if you: prefix the filenames with "test_", prefix classes with "Test" and prefix functions and
# methods with "test_". To see all the tests that pytest has discovered, run: ```pytest --collect-only```.
# Make sure these tests also pass.
class TestEmployee:
    def test_name(self) -> None:
        name = "Anna"
        employee = Employee(name=name, age=37, salary=1000)
        assert employee.name == name

    def test_give_raise(self) -> None:
        start_salary = 1000
        employee = Employee(name="-", age=37, salary=start_salary)
        employee.give_raise()
        assert employee.salary > start_salary
