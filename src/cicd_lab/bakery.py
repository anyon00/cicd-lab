"""빵집 가격 계산 모듈."""


def total_price(price: int, qty: int) -> int:
    """빵 가격 x 개수 = 총액."""
    if price < 0 or qty < 0:
        raise ValueError("가격과 개수는 0 이상이어야 합니다")
    return price * qty


def apply_discount(total: int, percent: int) -> int:
    """총액에 할인율(%)을 적용한 금액. 원 단위 미만은 버림."""
    if not 0 <= percent <= 100:
        raise ValueError("할인율은 0~100 사이여야 합니다")
    # return total * (100 - percent) // 100
    return total * percent // 100
