import pytest


@pytest.mark.smoke
def test_addition():
    actual = 2 + 2
    expected = 4
    assert actual == expected


@pytest.mark.smoke
def test_string():
    assert "Jenkins" in "Jenkins QA Demo"


@pytest.mark.regression
def test_list():
    numbers = [1, 2, 3]
    assert len(numbers) == 3