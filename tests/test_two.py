import pytest


@pytest.mark.parametrize('param1 param2', [
    (1, 1),
    (2, 2),
    (3, 4)
])
def test_parametrize(param1, param2):
    assert param1 == param2

