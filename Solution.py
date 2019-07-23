# -*- coding: utf-8 -*-
import bisect


class Solution1124:
    def longestWPI(self, hours):
        stack = [[0, 0]]
        res = cur = 0
        for i, h in enumerate(hours, 1):
            if h > 8:
                cur -= 1
            else:
                cur += 1
            j = bisect.bisect(stack, [cur + 1])
            if j < len(stack):
                res = max(res, i - stack[j][1])
            if stack[-1][0] < cur:
                stack.append([cur, i])
        return res, stack


if __name__ == '__main__':
    hours = [9, 9, 9, 9, 6, 0, 6, 6, 9]
    solution = Solution1124()
    result, stack = solution.longestWPI(hours)
    print(result, stack)
