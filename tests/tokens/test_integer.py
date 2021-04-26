from gravitron.tokens.integer import Integer
import pytest
import random

test_val_and_base = [[random.randint(1, 10000), random.randint(1, 10000)] for i in range(10)]


@pytest.mark.parametrize('val, base', test_val_and_base)
def test_basic_integer(val: int, base: int) -> None:
    integer: Integer = Integer(1, 2)
    assert integer.val == 1
    assert integer.base == 2
    return


def test_invalid_integer_value_on_init() -> None:
    with pytest.raises(TypeError):
        invalid_integer: Integer = Integer('foo', 10)
    return


def test_invalid_integer_base_on_init() -> None:
    with pytest.raises(TypeError):
        invalid_integer: Integer = Integer(10, 'foo')
    return
