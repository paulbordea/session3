import pytest
from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_adunare(x, y):
    assert x + y == y + x



