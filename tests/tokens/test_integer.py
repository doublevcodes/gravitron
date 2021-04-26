from gravitron.tokens.integer import Integer
import pytest


def test_basic_integer():
    integer: Integer = Integer(1, 2)
    assert integer.val == 1
    assert integer.base == 2


def test_invalid_integer_value_on_init():
    with pytest.raises(TypeError):
        invalid_integer: Integer = Integer('foo', 10)


def test_invalid_integer_base_on_init():
    with pytest.raises(TypeError):
        invalid_integer: Integer = Integer(10, 'foo')
