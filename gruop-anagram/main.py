import collections
from typing import List


class Solution:
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(Solution.group_anagrams(strs))
