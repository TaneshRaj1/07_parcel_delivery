import pytest
from parcel_acceptance import is_parcel_accepted


@pytest.mark.parametrize("weight, length", [
    (1, 1),          # both lower boundaries
    (20000, 199),
    (20000, 200),    # both upper boundaries (FAILS: code rejects 200)
    (10000, 100),
    (1, 200),        # length upper boundary (FAILS)
])
def test_accepted(weight, length):
    assert is_parcel_accepted(weight, length) is True


@pytest.mark.parametrize("weight, length", [
    (0, 50), 
    (50, 0), 
    (0, 0),     # zero values
    (20001, 50), 
    (50, 201),       # above limits
    (20001, 201),
])
def test_rejected(weight, length):
    assert is_parcel_accepted(weight, length) is False


@pytest.mark.parametrize("weight, length", [(-1, 50), (50, -1), (-1, -1)])
def test_negative_raises_value_error(weight, length):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight, length)


@pytest.mark.parametrize("weight, length", [
    ("100", 50), (100, "50"), (100.5, 50), (100, 50.5),
    (None, 50), (True, 50), (100, False),
])
def test_invalid_type_raises_type_error(weight, length):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight, length)


def test_returns_bool():
    assert isinstance(is_parcel_accepted(100, 100), bool)