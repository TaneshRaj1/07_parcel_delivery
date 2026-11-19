import pytest
from parcel_fee import delivery_fee


@pytest.mark.parametrize("weight, expected", [
    (1, 500),        # lower boundary band 1
    (500, 500),      # mid band 1
    (999, 500),
    (1000, 500),     # upper boundary band 1 (FAILS: code returns 1000)
    (1001, 1000),    # lower boundary band 2
    (10000, 1000),
    (20000, 1000),   # upper boundary band 2
])
def test_delivery_fee_valid(weight, expected):
    assert delivery_fee(weight) == expected


@pytest.mark.parametrize("weight", [0, -1, 20001])
def test_delivery_fee_out_of_range(weight):
    with pytest.raises(ValueError):
        delivery_fee(weight)


@pytest.mark.parametrize("weight", ["500", 500.0, None, True, False, [500]])
def test_delivery_fee_invalid_type(weight):
    with pytest.raises(TypeError):
        delivery_fee(weight)