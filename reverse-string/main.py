from typing import List


def reverse_string_by_two_pointer(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_by_pythonic_way(s: List[str]) -> None:
    s.reverse()


if __name__ == '__main__':
    str1 = ["h", "e", "l", "l", "o"]
    str2 = ["H", "a", "n", "n", "a", "h"]

    strs = [str1, str2]

    # Solve 1. Using two pointer
    print("reverse_string_by_two_pointer")
    for str in strs:
        print(str, "->", end=" ")
        reverse_string_by_two_pointer(str)
        print(str)

    # Solve 2. Using pythonic way
    print("reverse_string_by_pythonic_way")
    for str in strs:
        print(str, "->", end=" ")
        reverse_string_by_pythonic_way(str)
        print(str)