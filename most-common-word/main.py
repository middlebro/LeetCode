import collections
import re
from typing import List


def most_common_word_by_counter(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


def most_common_word_by_defaulit_dict(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key=counts.get)


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(most_common_word_by_defaulit_dict(paragraph, banned))
    print(most_common_word_by_counter(paragraph, banned))
