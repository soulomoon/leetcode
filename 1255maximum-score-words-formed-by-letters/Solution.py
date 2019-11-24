import collections
from collections import Counter
from typing import List


def get_score(letter, score):
    k = score[ord(letter) - ord('a')]
    return k


class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words_dict = {word: sum(get_score(l, score) for l in word) for word in words}

        def ctn(i, left_letters):
            sc = 0
            for j in range(i, len(words)):
                word_count = Counter(words[j])
                if all(word_count[k] <= left_letters[k] for k in word_count):
                    sc = max(sc, ctn(j + 1, left_letters - word_count) + words_dict[words[j]])
            return sc

        return ctn(0, Counter(letters))


if __name__ == "__main__":
    # words = ["leetcode"]
    # letters = ["l", "e", "t", "c", "o", "d"]
    # score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    # words = ["xxxz", "ax", "bx", "cx"]
    # letters = ["z", "a", "b", "c", "x", "x", "x"]
    # score = [4, 4, 4, 0, 0, 0, 0, 0,
    #          0, 0, 0, 0, 0, 0, 0, 0,
    #          0, 0, 0, 0, 0, 0, 0, 5,
    #          0, 10]

    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5,
             0, 0, 3, 0,
             0, 0, 0, 0,
             0, 0, 2, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
    print(Solution().maxScoreWords(words, letters, score))
