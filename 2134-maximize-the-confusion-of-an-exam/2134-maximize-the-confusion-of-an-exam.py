class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutive(ch: str) -> int:
            left = 0
            flips = 0
            max_len = 0
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    flips += 1
                while flips > k:
                    if answerKey[left] != ch:
                        flips -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len

        return max(maxConsecutive('T'), maxConsecutive('F'))
