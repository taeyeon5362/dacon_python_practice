"""
[문제 2]
리스트 l에서 자료형이 int인 원소만 더해서 그 값을 반환하는 함수 sum_of_ints(l)을 작성하세요.
"""
def sum_of_ints(l: list) -> int:
    result = 0
    for i in l :
        if isinstance(i, int):
            result += i
    return result
