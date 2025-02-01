import pytest

@pytest.mark.smoke
def test_1(browser):
    assert True

@pytest.mark.regress
def test_2(browser):
    assert True

@pytest.mark.regress
def test_3(browser):
    assert True

@pytest.mark.regress
def test_4(browser):
    assert True