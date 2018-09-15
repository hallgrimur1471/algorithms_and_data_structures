class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # words = ["abcw","baz","foo","bar","xtfn","abcdef"]
        if len(words) <= 1:
            return 0
        max_word_length = max(map(lambda w: len(w), words))
        counts = [[] for _ in range(0, max_word_length + 1)]
        for w in words:
            counts[len(w)].append(w)
        j = len(words) - 1
        for i in reversed(range(0, len(counts))):
            while len(counts[i]) > 0:
                words[j] = counts[i].pop()
                j -= 1
        print(words)
        j = len(words) - 1
        i = j - 1
        print(i, j)
        while has_common_char(words[i], words[j]):
            if (i == 0) and (j > 1):
                j -= 1
                i = j - 1
            elif (i == 0) and (j == 1):
                break
            elif j - i == 1:
                i -= 1
            elif (len(words[i - 1]) * len(words[j])) >= (
                len(words[j - 2]) * len(words[j - 1])
            ):
                i -= 1
            elif (len(words[i - 1]) * len(words[j])) < (
                len(words[j - 2]) * len(words[j - 1])
            ):
                j -= 1
                i = j - 1
            else:
                raise RuntimeError("Unexpected case")
        if has_common_char(words[i], words[j]):
            return 0
        print(i, j)
        return len(words[i]) * len(words[j])


def has_common_char(a, b):
    if len(b) < len(a):
        (a, b) = (b, a)
    b = set(b)
    for char in a:
        if char in b:
            return True
    return False
