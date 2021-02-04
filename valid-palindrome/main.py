import collections
import re
from typing import Deque


def is_palindrome_by_list(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # validate presence of palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_by_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_by_slicing(s: str) -> bool:
    s = s.lower()
    # Filtering by regex
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # slicing


if __name__ == '__main__':
    str1 = "A man, a plan, a canal: Panama"
    str2 = "race a car"
    strs = [str1, str2]

    # Solve 1. convert to list
    for str in strs:
        if is_palindrome_by_list(str):
            print(str, True)
        else:
            print(str, False)

    # Solve 2. optimization using by deque
    for str in strs:
        if is_palindrome_by_deque(str):
            print(str, True)
        else:
            print(str, False)

    # Solve 3. slicing
    for str in strs:
        if is_palindrome_by_slicing(str):
            print(str, True)
        else:
            print(str, False)
