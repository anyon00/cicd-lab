import pytest

from cicd_lab.bakery import apply_discount, total_price


def test_total_price():
    assert total_price(3000, 2) == 6000


def test_total_price_zero():
    assert total_price(3000, 0) == 0


def test_total_price_negative():
    with pytest.raises(ValueError):
        total_price(3000, -1)


def test_apply_discount():
    assert apply_discount(10000, 10) == 9000


def test_apply_discount_invalid():
    with pytest.raises(ValueError):
        apply_discount(10000, 150)
