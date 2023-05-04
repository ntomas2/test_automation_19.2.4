import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.division(self, 1, 0)
