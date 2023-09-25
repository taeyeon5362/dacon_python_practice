"""
[문제 3]
빈칸을 채워넣어 다음을 충족하는 함수 positive_negative(n1, n2, both_is_negative)를 작성하세요.
both_is_negative가 True인 경우, n1과 n2가 모두 음수인 경우 True를 반환하고 그렇지 않은 경우 False를 반환하세요.
both_is_negative가 False인 경우, n1과 n2 둘 중 하나만 음수인 경우 True를 반환하고 그렇지 않은 경우 False를 반환하세요.
"""
def positive_negative(n1: int, n2: int, both_is_negative: bool) -> bool:
    if both_is_negative:
        return n1 < 0 and n2 < 0
    else:
        return (not n1 < 0 and n2 < 0) or (n1 < 0 and not n2 < 0)

positive_negative(-1, -1, False)
