class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answers = []
        for i in range(len(boxes)):
            ans = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    ans += abs(i - j)
            answers.append(ans)
        return answers
