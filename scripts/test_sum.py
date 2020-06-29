import pytest

from Data.read_yml import sum_data


class TestSum:
    @pytest.mark.parametrize("a,b,c", sum_data())
    def test_sum(self, a, b, c):
        print(f"\n{a}+{b}={c}")
        assert a + b == c
