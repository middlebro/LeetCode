from pprint import pprint
from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == '__main__':
    """
    You are given an array of logs. Each log is a space-delimited string of words, 
        where the first word is the identifier.

    There are two types of logs:
    
        1. Letter-logs: All words (except the identifier) consist of lowercase English letters.
        2. Digit-logs: All words (except the identifier) consist of digits.
        
    Reorder these logs so that:
    
        1. The letter-logs come before all digit-logs.
        2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, 
            then sort them lexicographically by their identifiers.
        3. The digit-logs maintain their relative ordering.
        
    Return the final order of the logs.
    """
    logs_1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    logs_2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    logs = [logs_1, logs_2]

    for log in logs:
        pprint(log)
        pprint(reorder_log_files(log))
