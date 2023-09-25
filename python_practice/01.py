"""
[문제 1]
문자열 s가 주어졌을 때, n번 만큼 오른쪽으로 문자열을 회전시키는 함수 rotate_right(s, n)를 작성하세요.
예를 들면, rotate_right('abcd', 1)은 'dabc', rotate_right('abcd', 8)은 'abcd', rotate_right('abcd', -2)은 'cdab'가 됩니다.
"""
# s가 str, n이 int, 반환값이 str인 함수 rotate_right을 작성하세요

def rotate_right(s: str, n: int) -> str:
    return s[-n:] + s[:-n]

rotate_right('abcd', 1)
